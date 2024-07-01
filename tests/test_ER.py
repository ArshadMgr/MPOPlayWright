from cryptography.fernet import Fernet
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
import pytest

from MPOPlayWright.Payload.login import Login
from MPOPlayWright.Payload.security import generate_key, save_credentials_to_file, encrypt_message, load_credentials_from_file
from MPOPlayWright.Payload.new_hire import NewHire
from MPOPlayWright.utils.config import BASE_URL
from MPOPlayWright.utils.config import USERNAME
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
    login_page.enter_employer("Employer")
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
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/NewHireReport.aspx")
    assert "New Hire Report" in page.title()
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/EditEmployees.aspx")
    assert "Edit Employees" in page.title()
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/TerminateEmployee.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/TerminationReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/UserManagement/ManagerAssignment.aspx")
    page.goto(BASE_URL + "/Sys/Common/CompanyManagement/CompanyLevelsHierarchy.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Employees/JobTitles.aspx")
    page.goto(BASE_URL + "/Sys/Employer/WelcomeEmail/WelcomeEmailReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Onboarding/OnboardingReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Onboarding/OnboardingTemplateSettings.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Onboarding/OnboardingDashboardSettings.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Onboarding/OnboardingReminderAlertSettings.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Orientation/EmployeeOrientationReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Announcements/Announcements.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewSetupWizard.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewDashboard.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewJournal.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewChecklists.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewSessions.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewCriteriaLibrary.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewCommentTemplates.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewWorkflows.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewReports.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewFeedback.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewReminderAlertSettings.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewGoalReminderAlertSettings.aspx")
    page.goto(BASE_URL + "/Sys/Employer/FAQ/KnowledgeBase.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Kudos/KudosSettings.aspx")
    page.goto(BASE_URL + "/Sys/Common/Kudos/ManageKudos.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Kudos/KudosReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/PerformanceReviewGoals.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/Succession.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EmployeeWarnings.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/CompanyHolidays.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/HR/EmployeeSuggestionReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/EnrollmentWizard/BenefitEnrollmentWizard.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Setup/BenefitPlans.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/LifeEvents/LifeEventsReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Reports/BenefitEdiReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Templates/BenefitDurationTemplates.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Templates/BenefitCoverages.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Templates/BenefitComparisonSummaryTemplates.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Templates/FlexCredits.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Templates/BenefitForms.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Benefits/Reports/BeneficiariesReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Benefits/Reports/DependentsReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Reports/BenefitEnrollmentReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Setup/BenefitCloneReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Reports/BenefitEdiReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Reports/BenefitsActivitiesReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Reports/EnrollmentsSummaryReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Reports/InsuranceApplicationsReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Reports/Benefit401KPlanEnrollmentReport.aspx")
    page.goto(BASE_URL + "/Sys/Common/Benefits/Reports/BenefitsConsolidatedBillingReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffRequest.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffApprovalDenialReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffBalanceReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffCalendar.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/TimeoffManagement/TimeoffMiscellaneousSettings.aspx")
    page.goto(BASE_URL + "/Sys/Employer/TimeOffAccruals/TimeOffAccrualsProfiles.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Payroll/CalendarRules.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Payroll/HolidayRules.aspx")
    page.goto(BASE_URL + "/Sys/Common/Payroll/TimeSheetSettings.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Payroll/ImportTimePunches.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Payroll/TimeCardType.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Payroll/PayrollBatches.aspx")
    page.goto(BASE_URL + "/Sys/Employer/CustomReport/CustomReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Reports/DeductionApprovalReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/TaskManagement/ScheduledReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/AnniversaryReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/BirthdayReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EducationReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EmergencyContactReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EmployeeNotesReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EquipmentReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/LicenseTrackingReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EmployeeCountReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EmployeeTurnoverReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EmployeeUserAccountsReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EmployeeEEOReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/I9/Ei9ExpirationReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/EmployeeSkillReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Employees/OrganizationChart.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Reports/WorkForceAge.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Reports/Vet4212.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Reports/PayHistory.aspx")
    page.goto(BASE_URL + "/Sys/Employer/Reports/PayRates.aspx")
    page.goto(BASE_URL + "/Sys/Employer/HR/TerminationTrend.aspx")
    page.goto(BASE_URL + "/Sys/Common/Reports/SyncChangeReport.aspx")
    page.goto(BASE_URL + "/Sys/Employer/FileCabinet/FileCabinet.aspx")
    page.goto(BASE_URL + "/Sys/Common/Files/EmployeeForms/EmployeeForms.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/Files/EmployeeForms/EmployeeFormsReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ScheduleManagement/EmployeeSchedule.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ScheduleManagement/ScheduleDisplaySettings.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ScheduleManagement/EmployeeRejectedShift.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/JobPostsSettings.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ApplicationFormSettings.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ManageInterviewsChecklists.aspx")
    page.goto(BASE_URL + "/Sys/Employer/ApplicantTrackingSystem/JobPostingStageSettings.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ApplicantsRecruitmentPipeline.aspx")
    page.goto(BASE_URL + "/Sys/Employer/ApplicantTrackingSystem/ExternalJobBoardSettings.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/ApplicantsReport.aspx")
    page.goto(BASE_URL + "/Sys/EmployerManager/ApplicantTrackingSystem/Quizzes.aspx")
    page.goto(BASE_URL + "/Sys/Common/Tasks/Kanban.aspx")
    page.goto(BASE_URL + "/Sys/Common/Tasks/Task.aspx'")
    page.goto(BASE_URL + "/Sys/Common/Tasks/TaskGroup.aspx")
    page.goto(BASE_URL + "/Sys/Common/Tasks/TaskList.aspx")
    page.goto(BASE_URL + "/Sys/Common/MessageCenter/Messages.aspx")
    page.goto(BASE_URL + "/Sys/UserProfile.aspx")
