from cryptography.fernet import Fernet
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
import pytest

from MPOPlayWright.Payload.login import Login
from MPOPlayWright.Payload.new_hire import NewHire
from MPOPlayWright.utils.config import BASE_URL
from MPOPlayWright.utils.config import USERNAME
from MPOPlayWright.Payload.security import generate_key, save_credentials_to_file, encrypt_message, load_credentials_from_file
from MPOPlayWright.pages.login_page import LoginPage
from MPOPlayWright.utils.logger import setup_logger
import time

logger = setup_logger()


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser


def test_setup(browser):
    mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file("credentials.txt")

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

    # login_page.verify_title()

    # Add assertions to verify successful login
    logger.info("Completed test: test_valid_login")

    time.sleep(10)

    assert "Dashboard" in page.title()
    userPayload = NewHire(page)
    userPayload.setFirstName("CharlesCR")
    assert userPayload.getFirstName() == "CharlesCR"

    logger.info("Starting test: test_Page_Crashes")
    page.goto(BASE_URL + "/Sys/Employee/EmployeeCareerProfile.aspx")
    page.goto(BASE_URL + '/Sys/Employee/DirectDeposit.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeEducation.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeEducation.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeEmergencyContact.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeEquipments.aspx')
    page.goto(BASE_URL + '/Sys/Employee/I9/I9.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeLicenses.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeNotes.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeSkills.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeUserAccounts.aspx')
    page.goto(BASE_URL + '/Sys/Employee/TaxForms/TaxForms.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeeTaxInformation.aspx')
    page.goto(BASE_URL + '/Sys/Employee/EmployeePayStub.aspx')
    page.goto(BASE_URL + '/Sys/Employee/Demographics.aspx')
    page.goto(BASE_URL + '/Sys/Employer/Onboarding/EmployeeOnboardingStepInfo.aspx')
    page.goto(BASE_URL + '/Sys/Common/Benefits/EnrollmentWizard/BenefitEnrollmentWizard.aspx')
    page.goto(BASE_URL + '/Sys/Common/Benefits/LifeEvents/EmployeeLifeEvents.aspx')
    page.goto(BASE_URL + '/Sys/Common/Benefits/Reports/EnrollmentsSummaryReport.aspx')
    page.goto(BASE_URL + '/Sys/Employee/HR/EmployeePerformanceReviewDashboard.aspx')
    page.goto(BASE_URL + '/Sys/Employee/HR/PerformanceReviewJournal.aspx')
    page.goto(BASE_URL + '/Sys/Employee/FAQ/KnowledgeBase.aspx')
    page.goto(BASE_URL + '/Sys/Common/Kudos/ManageKudos.aspx')
    page.goto(BASE_URL + '/Sys/Employee/HR/PerformanceReviewGoals.aspx')
    page.goto(BASE_URL + '/Sys/Employee/HR/CompanyHolidays.aspx')
    page.goto(BASE_URL + '/Sys/Employee/Succession.aspx')
    page.goto(BASE_URL + '/Sys/Employee/HR/EmployeeWarnings.aspx')
    page.goto(BASE_URL + '/Sys/Employee/HR/EmployeeSuggestions.aspx')
    page.goto(BASE_URL + '/Sys/Employee/TimeoffManagement/EmployeeTimeoffRequest.aspx')
    page.goto(BASE_URL + '/Sys/Employee/TimeoffManagement/EmployeeTimeoffReport.aspx')
    page.goto(BASE_URL + '/Sys/Employee/FileCabinet/FileCabinet.aspx')
    page.goto(BASE_URL + '/Sys/Employee/Files/EmployeeForms/MyEmployeeForms.aspx')
    page.goto(BASE_URL + '/Sys/Employee/Payroll/Timesheet.aspx')
    page.goto(BASE_URL + '/Sys/Common/Tasks/Kanban.aspx')
    page.goto(BASE_URL + '/Sys/Common/Tasks/Task.aspx')
    page.goto(BASE_URL + '/Sys/Common/Tasks/TaskGroup.aspx')
    page.goto(BASE_URL + '/Sys/Common/Tasks/TaskList.aspx')
    page.goto(BASE_URL + '/Sys/Employee/ScheduleManagement/EmployeeSchedulePreference.aspx')
    page.goto(BASE_URL + '/Sys/Employee/ScheduleManagement/EmployeeSchedule.aspx')
    page.goto(BASE_URL + '/Sys/Employee/ScheduleManagement/EmployeeTradeShifts.aspx')
    page.goto(BASE_URL + '/Sys/Common/MessageCenter/Messages.aspx')
    page.goto(BASE_URL + '/Sys/UserProfile.aspx')
    page.goto(BASE_URL + '/Sys/Logoff.aspx')
    logger.info("Completed test: test_EE_Smoke_Test")
