from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
import pytest

from MPOPlayWright.Payload.new_hire import NewHire
from MPOPlayWright.utils.config import BASE_URL
from MPOPlayWright.utils.config import USERNAME
from MPOPlayWright.utils.config import PASSWORD
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
    logger.info("Setting up the test environment(Demo)")
    page = browser.new_page()
    page.goto(BASE_URL + '/login.aspx')

    login_page = LoginPage(page)

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

    assert "Dashboard" in page.title()
    userPayload = NewHire(page)
    userPayload.setFirstName("CharlesCR")
    assert userPayload.getFirstName() == "CharlesCR"

    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/NewHire.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/NewHireReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/EditEmployees.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/TerminateEmployee.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/TerminationReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/CompanyManagement/CompanyLevelsHierarchy.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Onboarding/OnboardingReport.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/PerformanceReviewDashboard.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/PerformanceReviewJournal.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/PerformanceReviewReports.aspx")
    page.goto(BASE_URL + "/Sys/Manager/FAQ/KnowledgeBase.aspx")
    page.goto(BASE_URL + "/Sys/Common/Kudos/ManageKudos.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Kudos/KudosReport.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/PerformanceReviewGoals.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/CompanyHolidays.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/Succession.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/EmployeeWarnings.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/HR/EmployeeSuggestionReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/EnrollmentWizard/BenefitEnrollmentWizard.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Benefits/Reports/BeneficiariesReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Benefits/Reports/DependentsReport.aspx")
    page.goto(BASE_URL + "/EmployerManager/Benefits/Reports/BenefitEligibilityReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Reports/EnrollmentsSummaryReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffRequest.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffApprovalDenialReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffBalanceReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffCalendar.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Payroll/TimeSheet.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/AnniversaryReport.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/BirthdayReport.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/EducationReport.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/EmergencyContactReport.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/EmployeeNotesReport.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/EquipmentReport.aspx")
    page.goto(BASE_URL + "/Sys/Manager/HR/LicenseTrackingReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EmployeeSkillReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/HR/PreviousEmployersReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/TerminationTrend.aspx")
    page.goto(BASE_URL + "/Sys/Manager/FileCabinet/FileCabinet.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Files/EmployeeForms/EmployeeFormsReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ScheduleManagement/EmployeeSchedule.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ScheduleManagement/EmployeeRejectedShift.aspx")
    page.goto(BASE_URL + "/Sys/Common/Tasks/Kanban.aspx")
    page.goto(BASE_URL + "/Sys/Common/Tasks/Task.aspx")
    page.goto(BASE_URL + "/Sys/Common/Tasks/TaskGroup.aspx")
    page.goto(BASE_URL + "/Sys/Common/Tasks/TaskList.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/JobPostsSettings.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ApplicationFormSettings.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ManageInterviewsChecklists.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ApplicantsRecruitmentPipeline.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ApplicantsReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/Quizzes.aspx")
    page.goto(BASE_URL + "/Sys/Common/MessageCenter/Messages.aspx")
    page.goto(BASE_URL + "/Sys/UserProfile.aspx")
    page.goto(BASE_URL + "/Sys/logoff.aspx")

