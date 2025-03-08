from cryptography.fernet import Fernet
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
import pytest

from Payload.login import Login
from Payload.security import generate_key, save_credentials_to_file, encrypt_message, load_credentials_from_file
from Payload.new_hire import NewHire
from utils.config import BASE_URL, USERNAME, CredentilasPath_A
from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger()


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser


def test_setup(browser):
    mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_A)
    decrypted_password = mpologin.decrypt_message(encrypted_password, key)

    logger.info("Starting test: test_valid_login")

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

    page.wait_for_load_state("load")  # ✅ Ensuring the page is fully loaded

    # Verify successful login
    try:
        page.wait_for_timeout(1000)  # ✅ Small delay before checking title
        assert "Dashboard" in page.title(), "Login failed: Dashboard not found"
        logger.info("Successfully logged in.")
    except Exception as e:
        page.screenshot(path="failed_login.png")
        assert False, f"Login failed with error: {e}"

    # Verify New Hire Setup
    userPayload = NewHire(page)
    userPayload.setFirstName("CharlesCR")
    assert userPayload.getFirstName() == "CharlesCR"
    logger.info("New Hire Setup verified successfully.")

    # List of pages to visit and verify
    pages_to_visit = [
        ("/Sys/Employee/EmployeeCareerProfile.aspx", "Employee Career Profile"),
        ('/Sys/Employee/DirectDeposit.aspx',"Direct Deposit"),
        ('/Sys/Employee/EmployeeEducation.aspx',"Employee Education"),
        ('/Sys/Employee/EmployeeEmergencyContact.aspx',"Emergency Contacts"),
        ('/Sys/Employee/EmployeeEquipments.aspx',"Equipment"),
        ('/Sys/Employee/I9/I9.aspx',"Form I-9"),
        ('/Sys/Employee/EmployeeLicenses.aspx',"Licenses"),
        ('/Sys/Employee/EmployeeNotes.aspx',"Employee Notes"),
        ('/Sys/Employee/EmployeeSkills.aspx',"Employee Skills"),
        ('/Sys/Employee/EmployeeUserAccounts.aspx',"Employee User Accounts"),
        ('/Sys/Employee/TaxForms/TaxForms.aspx',"Tax Forms"),
        ('/Sys/Employee/EmployeeTaxInformation.aspx',"Employee Tax Information"),
        ('/Sys/Employee/EmployeePayStub.aspx',"Employee Pay Checks"),
        ('/Sys/Employee/Demographics.aspx',"Demographics"),
        ('/Sys/Employer/Onboarding/EmployeeOnboardingStepInfo.aspx',"Employee Onboarding Step Info"),
        ('/Sys/Common/Benefits/EnrollmentWizard/BenefitEnrollmentWizard.aspx',"Benefit Enrollment Wizard"),
        ('/Sys/Common/Benefits/LifeEvents/EmployeeLifeEvents.aspx',"Life Events"),
        ('/Sys/Common/Benefits/Reports/EnrollmentsSummaryReport.aspx',"Enrollment Summary Report"),
        ('/Sys/Employee/HR/EmployeePerformanceReviewDashboard.aspx',"Employee Performance Review Dashboard"),
        ('/Sys/Employee/HR/PerformanceReviewJournal.aspx',"Performance Journal"),
        ('/Sys/Employee/FAQ/KnowledgeBase.aspx',"Knowledge Base"),
        ('/Sys/Common/Kudos/ManageKudos.aspx',"Kudos"),
        ('/Sys/Employee/HR/PerformanceReviewGoals.aspx',"Objective & Key Results"),
        ('/Sys/Employee/HR/CompanyHolidays.aspx',"Company Holidays"),
        ('/Sys/Employee/Succession.aspx',"Succession"),
        ('/Sys/Employee/HR/EmployeeWarnings.aspx',"Employee Warnings"),
        ('/Sys/Employee/HR/EmployeeSuggestions.aspx',"Suggestions"),
        ('/Sys/Employee/TimeoffManagement/EmployeeTimeoffRequest.aspx',"Time Off Request"),
        ('/Sys/Employee/TimeoffManagement/EmployeeTimeoffReport.aspx',"Time Off Approval/Denial Report"),
        ('/Sys/Employee/FileCabinet/FileCabinet.aspx',"File Cabinet"),
        ('/Sys/Employee/Files/EmployeeForms/MyEmployeeForms.aspx',"My Employee Forms"),
        ('/Sys/Employee/Payroll/Timesheet.aspx',"Time Sheet"),
        ('/Sys/Common/Tasks/Kanban.aspx',"Task Board"),
        ('/Sys/Common/Tasks/Task.aspx',"Task"),
        ('/Sys/Common/Tasks/TaskGroup.aspx',"Task Group"),
        ('/Sys/Common/Tasks/TaskList.aspx',"Task List"),
        ('/Sys/Employee/ScheduleManagement/EmployeeSchedulePreference.aspx',"Schedule Preference"),
        ('/Sys/Employee/ScheduleManagement/EmployeeSchedule.aspx', "Schedule"),
        ('/Sys/Employee/ScheduleManagement/EmployeeTradeShifts.aspx',"Trade/Give Away Shift"),
        ('/Sys/Common/MessageCenter/Messages.aspx',"Messages"),
        ('/Sys/UserProfile.aspx',"User Profile"),
        ('/Sys/Logoff.aspx',"Sign In"),














    ]

    # Navigate and verify each page
    for url, expected_title in pages_to_visit:
        page.goto(BASE_URL + url)
        page.wait_for_load_state("load")  # ✅ Ensuring page load completion

        try:
            page.wait_for_timeout(1000)  # ✅ Small delay before checking title
            assert expected_title in page.title(), f"Page validation failed: Expected '{expected_title}'"
            logger.info(f"Successfully verified: {expected_title}")
        except Exception as e:
            page.screenshot(path=f"{expected_title.replace(' ', '_')}.png")
            assert False, f"Page validation failed for {expected_title} with error: {e}"

    logger.info("Test completed successfully.")
    browser.close()
