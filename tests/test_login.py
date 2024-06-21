import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL
from utils.config import USERNAME
from utils.config import PASSWORD
from pages.login_page import LoginPage
from utils.logger import setup_logger
import time

logger = setup_logger()


@pytest.fixture(scope="class")
def test_setup(request):
    logger.info("Setting up the test environment")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(BASE_URL + "/login.aspx")
    request.cls.page = page
    request.cls.browser = browser
    yield
    logger.info("Tearing down the test environment")
    browser.close()
    playwright.stop()


@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_valid_login(self):
        logger.info("Starting test: test_valid_login")
        login_page = LoginPage(self.page)
        login_page.enter_username(USERNAME)
        login_page.enter_password(PASSWORD)
        login_page.click_login()

        login_page.click_go_button()

        # login_page.verify_title()

        # Add assertions to verify successful login
        logger.info("Completed test: test_valid_login")

    def test_ee_smoke(self):
        logger.info("Starting test: test_Page_Crashes")
        self.page.goto(BASE_URL + "/Sys/Employee/EmployeeCareerProfile.aspx")
        self.page.goto(BASE_URL + '/Sys/Employee/DirectDeposit.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/EmployeeEducation.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/EmployeeEducation.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/EmployeeEmergencyContact.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/EmployeeEquipments.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/I9/I9.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/EmployeeLicenses.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/EmployeeNotes.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/EmployeeSkills.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/EmployeeUserAccounts.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/TaxForms/TaxForms.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/EmployeeTaxInformation.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/EmployeePayStub.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/Demographics.aspx')
        self.page.goto(BASE_URL + '/Sys/Employer/Onboarding/EmployeeOnboardingStepInfo.aspx')
        self.page.goto(BASE_URL + '/Sys/Common/Benefits/EnrollmentWizard/BenefitEnrollmentWizard.aspx')
        self.page.goto(BASE_URL + '/Sys/Common/Benefits/LifeEvents/EmployeeLifeEvents.aspx')
        self.page.goto(BASE_URL + '/Sys/Common/Benefits/Reports/EnrollmentsSummaryReport.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/HR/EmployeePerformanceReviewDashboard.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/HR/PerformanceReviewJournal.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/FAQ/KnowledgeBase.aspx')
        self.page.goto(BASE_URL + '/Sys/Common/Kudos/ManageKudos.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/HR/PerformanceReviewGoals.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/HR/CompanyHolidays.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/Succession.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/HR/EmployeeWarnings.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/HR/EmployeeSuggestions.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/TimeoffManagement/EmployeeTimeoffRequest.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/TimeoffManagement/EmployeeTimeoffReport.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/FileCabinet/FileCabinet.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/Files/EmployeeForms/MyEmployeeForms.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/Payroll/Timesheet.aspx')
        self.page.goto(BASE_URL + '/Sys/Common/Tasks/Kanban.aspx')
        self.page.goto(BASE_URL + '/Sys/Common/Tasks/Task.aspx')
        self.page.goto(BASE_URL + '/Sys/Common/Tasks/TaskGroup.aspx')
        self.page.goto(BASE_URL + '/Sys/Common/Tasks/TaskList.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/ScheduleManagement/EmployeeSchedulePreference.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/ScheduleManagement/EmployeeSchedule.aspx')
        self.page.goto(BASE_URL + '/Sys/Employee/ScheduleManagement/EmployeeTradeShifts.aspx')
        self.page.goto(BASE_URL + '/Sys/Common/MessageCenter/Messages.aspx')
        self.page.goto(BASE_URL + '/Sys/UserProfile.aspx')
        self.page.goto(BASE_URL + '/Sys/Logoff.aspx')
        logger.info("Completed test: test_EE_Smoke_Test")
