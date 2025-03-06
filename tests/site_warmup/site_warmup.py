
from utils.logger import setup_logger
logger = setup_logger()
from playwright.sync_api import sync_playwright
import pytest
from utils.config import CredentilasPath_A
from utils.config import CredentilasPath_H
from Payload.login import Login
from Payload.new_hire import NewHire
from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from utils.logger import setup_logger
import time

logger = setup_logger()

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser


def test_Employer(browser):
    mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_A)

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)

    logger.info("Setting up the test environment(ER)")
    page = browser.new_page()
    page.goto(BASE_URL + '/login.aspx')

    login_page = LoginPage(page)

    login_page.enter_username(USERNAME)
    login_page.enter_password(decrypted_password)
    login_page.click_login()

    login_page.clik_ee_role()
    login_page.enter_employer("Employer")
    login_page.press_enter()
    login_page.click_go_button()
    logger.info("Completed test: test_valid_login")

    time.sleep(10)

    assert "Dashboard" in page.title()
    userPayload = NewHire(page)
    userPayload.setFirstName("CharlesCR")
    assert userPayload.getFirstName() == "CharlesCR"

    logger.info("Starting test: test_Page_Crashes")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/NewHireReport.aspx")

    if "New Hire Report" not in page.title():
        page.screenshot(path="New_Hire_Report.png")
        assert False, "Title does not contain 'New Hire Report'"


    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/EditEmployees.aspx")

    if "Edit Employees" not in page.title():
        page.screenshot(path="Edit_Employees.png")
        assert False, "Title does not contain 'Edit Employees'"

    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/TerminateEmployee.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/TerminationReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/UserManagement/ManagerAssignment.aspx")
    page.goto(BASE_URL + "/Sys/Common/CompanyManagement/CompanyLevelsHierarchy.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Employees/JobTitles.aspx")
    page.goto(BASE_URL + "/Sys/Employer/WelcomeEmail/WelcomeEmailReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Onboarding/OnboardingReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Onboarding/OnboardingTemplateSettings.aspx")
    page.goto(BASE_URL + "/Sys/UserProfile.aspx")
    page.goto(BASE_URL + "/Sys/logoff.aspx")
    #<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Manager>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def test_Manager(browser):
    mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_A)

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)

    logger.info("Setting up the test environment(Manager)")
    page = browser.new_page()
    page.goto(BASE_URL + '/login.aspx')

    login_page = LoginPage(page)

    login_page.enter_username(USERNAME)
    login_page.enter_password(decrypted_password)
    login_page.click_login()

    login_page.clik_ee_role()
    login_page.enter_employer("Manager")
    login_page.press_enter()
    login_page.click_go_button()

    logger.info("Completed test: test_valid_login")

    time.sleep(10)

    assert "Dashboard" in page.title()
    userPayload = NewHire(page)
    userPayload.setFirstName("CharlesCR")
    assert userPayload.getFirstName() == "CharlesCR"
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/NewHire.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/NewHireReport.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/EmployeeNotesReport.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/EquipmentReport.aspx")
    page.goto(BASE_URL + "/Sys/UserProfile.aspx")
    page.goto(BASE_URL + "/Sys/logoff.aspx")

 #<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Employee>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def test_Employee(browser):
    #with SoftAssertContext() as soft_assert:

    mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_A)

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)

    logger.info("Setting up the test environment(Demo)")
    page = browser.new_page()
    page.goto(BASE_URL + '/login.aspx')

    login_page = LoginPage(page)

    login_page.enter_username(USERNAME)
    login_page.enter_password(decrypted_password)
    login_page.click_login()

    login_page.clik_ee_role()
    login_page.enter_employer("Employee")
    login_page.press_enter()
    login_page.click_go_button()
    logger.info("Completed test: test_valid_login")

    time.sleep(10)

    assert "Dashboard" in page.title()
    userPayload = NewHire(page)
    userPayload.setFirstName("CharlesCR")
    assert userPayload.getFirstName() == "CharlesCR"
    page.goto(BASE_URL + '/Sys/Employee/EmployeeNotes.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeSkills.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeUserAccounts.aspx')
    page.goto(BASE_URL + '/Sys/Employee/Demographics.aspx')
    page.goto(BASE_URL + '/Sys/Common/MessageCenter/Messages.aspx')
    page.goto(BASE_URL + '/Sys/UserProfile.aspx')
    page.goto(BASE_URL + '/Sys/Logoff.aspx')





