import time
import csv
import pytest
from playwright.sync_api import sync_playwright
from utils.logger import setup_logger
from utils.config import BASE_URL, USERNAME, CredentilasPath_A
from Payload.login import Login
from Payload.new_hire import NewHire
from pages.login_page import LoginPage

logger = setup_logger()

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser

def measure_page_load(page, url):
    """Measure page load time and return it."""
    start_time = time.time()
    page.goto(url, wait_until="load")
    load_time = time.time() - start_time
    logger.info(f"Loaded: {url} | Time: {load_time:.2f}s")
    return url, load_time

def write_load_times_to_csv(role, load_times):
    """Save page load times to a CSV file."""
    filename = f"{role}_page_load_times.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Load Time (seconds)"])
        writer.writerows(load_times)
    logger.info(f"Load times saved to {filename}")

def run_test(browser, role, role_name, urls):
    """Generic function to test Employer, Manager, or Employee role."""
    mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_A)
    decrypted_password = mpologin.decrypt_message(encrypted_password, key)

    logger.info(f"Setting up the test environment for {role_name}")
    page = browser.new_page()
    page.goto(BASE_URL + "/login.aspx")

    login_page = LoginPage(page)
    login_page.enter_username(USERNAME)
    login_page.enter_password(decrypted_password)
    login_page.click_login()
    login_page.clik_ee_role()
    login_page.enter_employer(role_name)
    login_page.press_enter()
    login_page.click_go_button()
    time.sleep(10)
    assert "Dashboard" in page.title(), f"Failed to load Dashboard for {role_name}"

    # Measure page load times
    load_times = []
    for url in urls:
        load_times.append(measure_page_load(page, url))

    # Save load times to CSV
    write_load_times_to_csv(role, load_times)

    # Logout
    page.goto(BASE_URL + "/Sys/logoff.aspx")

def test_Employer(browser):
    urls = [
        "/Sys/EmployerManager/Employees/NewHireReport.aspx",
        "/Sys/EmployerManager/Employees/EditEmployees.aspx",
        "/Sys/EmployerManager/Employees/TerminateEmployee.aspx",
        "/Sys/EmployerManager/Employees/TerminationReport.aspx",
        "/Sys/Common/UserManagement/ManagerAssignment.aspx",
        "/Sys/Common/CompanyManagement/CompanyLevelsHierarchy.aspx",
        "/Sys/Employer/Employees/JobTitles.aspx",
        "/Sys/Employer/WelcomeEmail/WelcomeEmailReport.aspx",
        "/Sys/Employer/Onboarding/OnboardingReport.aspx",
        "/Sys/Employer/Onboarding/OnboardingTemplateSettings.aspx",
        "/Sys/UserProfile.aspx",
    ]
    run_test(browser, "Employer", "Employer", [BASE_URL + url for url in urls])

def test_Manager(browser):
    urls = [
        "/Sys/EmployerManager/Employees/NewHire.aspx",
        "/Sys/EmployerManager/Employees/NewHireReport.aspx",
        "/Sys/Manager/HR/EmployeeNotesReport.aspx",
        "/Sys/Manager/HR/EquipmentReport.aspx",
        "/Sys/UserProfile.aspx",
    ]
    run_test(browser, "Manager", "Manager", [BASE_URL + url for url in urls])

def test_Employee(browser):
    urls = [
        "/Sys/Employee/EmployeeNotes.aspx",
        "/Sys/Employee/EmployeeSkills.aspx",
        "/Sys/Employee/EmployeeUserAccounts.aspx",
        "/Sys/Employee/Demographics.aspx",
        "/Sys/Common/MessageCenter/Messages.aspx",
        "/Sys/UserProfile.aspx",
    ]
    run_test(browser, "Employee", "Employee", [BASE_URL + url for url in urls])
