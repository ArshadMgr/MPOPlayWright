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
    page.goto("https://mypaperlessoffice.com/app/login.aspx")
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


        login_page.clik_ee_role()
        login_page.enter_employer("Manager")
        login_page.press_enter()
        login_page.click_go_button()

        # login_page.verify_title()

        # Add assertions to verify successful login
        logger.info("Completed test: test_valid_login")

        time.sleep(10)

    def test_ee_smoke(self):

        logger.info("Starting test: test_Page_Crashes")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/Employees/NewHire.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/Employees/NewHireReport.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/Employees/EditEmployees.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/Employees/TerminateEmployee.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/Employees/TerminationReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Common/CompanyManagement/CompanyLevelsHierarchy.aspx")
        self.page.goto(BASE_URL + "/Sys/Employer/Onboarding/OnboardingReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/PerformanceReviewDashboard.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/PerformanceReviewJournal.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/PerformanceReviewReports.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/FAQ/KnowledgeBase.aspx")
        self.page.goto(BASE_URL + "/Sys/Common/Kudos/ManageKudos.aspx")
        self.page.goto(BASE_URL + "/Sys/Employer/Kudos/KudosReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/PerformanceReviewGoals.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/CompanyHolidays.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/Employees/Succession.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/EmployeeWarnings.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/HR/EmployeeSuggestionReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Common/Benefits/EnrollmentWizard/BenefitEnrollmentWizard.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/Benefits/Reports/BeneficiariesReport.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/Benefits/Reports/DependentsReport.aspx")
        self.page.goto(BASE_URL + "/EmployerManager/Benefits/Reports/BenefitEligibilityReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Common/Benefits/Reports/EnrollmentsSummaryReport.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffRequest.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffApprovalDenialReport.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffBalanceReport.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffCalendar.aspx")
        self.page.goto(BASE_URL + "/Sys/Employer/Payroll/TimeSheet.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/AnniversaryReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/BirthdayReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/EducationReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/EmergencyContactReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/EmployeeNotesReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/EquipmentReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/HR/LicenseTrackingReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Employer/HR/EmployeeSkillReport.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/HR/PreviousEmployersReport.aspx")
        self.page.goto(BASE_URL + "/Sys/Employer/HR/TerminationTrend.aspx")
        self.page.goto(BASE_URL + "/Sys/Manager/FileCabinet/FileCabinet.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/Files/EmployeeForms/EmployeeFormsReport.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/ScheduleManagement/EmployeeSchedule.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/ScheduleManagement/EmployeeRejectedShift.aspx")
        self.page.goto(BASE_URL + "/Sys/Common/Tasks/Kanban.aspx")
        self.page.goto(BASE_URL + "/Sys/Common/Tasks/Task.aspx")
        self.page.goto(BASE_URL + "/Sys/Common/Tasks/TaskGroup.aspx")
        self.page.goto(BASE_URL + "/Sys/Common/Tasks/TaskList.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/JobPostsSettings.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ApplicationFormSettings.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ManageInterviewsChecklists.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ApplicantsRecruitmentPipeline.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ApplicantsReport.aspx")
        self.page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/Quizzes.aspx")
        self.page.goto(BASE_URL + "/Sys/Common/MessageCenter/Messages.aspx")
        self.page.goto(BASE_URL + "/Sys/UserProfile.aspx")
        self.page.goto(BASE_URL + "/Sys/logoff.aspx")


