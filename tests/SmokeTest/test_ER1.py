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
    login_page.enter_employer("Employer")
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
        ("/Sys/EmployerManager/Employees/NewHireReport.aspx", "New Hire Report"),
        ("/Sys/EmployerManager/Employees/EditEmployees.aspx", "Edit Employees"),
        ("/Sys/EmployerManager/Employees/TerminateEmployee.aspx", "Employee Termination"),

        ("/Sys/Employer/HR/EmployeeWarnings.aspx", "Employee Warnings"),
        ("/Sys/EmployerManager/TimeoffManagement/TimeoffRequest.aspx", "Time Off Request"),
        ("/Sys/Employer/FileCabinet/FileCabinet.aspx", "File Cabinet"),
        ("/Sys/Employer/Reports/PayHistory.aspx", "Pay History"),
        ("/Sys/Common/Reports/SyncChangeReport.aspx", "Sync Change Report"),

        ("/Sys/EmployerManager/Employees/TerminationReport.aspx", "Termination Report"),
        ("/Sys/Common/UserManagement/ManagerAssignment.aspx", "Manager Assignment"),
        ("/Sys/Common/CompanyManagement/CompanyLevelsHierarchy.aspx", "Company Levels Hierarchy"),
        ("/Sys/Employer/Employees/JobTitles.aspx", "Job Titles"),
        ("/Sys/Employer/WelcomeEmail/WelcomeEmailReport.aspx", "Welcome Email Report"),
        ("/Sys/Employer/Onboarding/OnboardingReport.aspx", "Onboarding Report"),
        ("/Sys/Employer/Onboarding/OnboardingTemplateSettings.aspx", "Onboarding Settings"),
        ("/Sys/Employer/Onboarding/OnboardingDashboardSettings.aspx", "Onboarding Dashboard Settings"),
        ("/Sys/Employer/Onboarding/OnboardingReminderAlertSettings.aspx", "Onboarding Reminder Alert Settings"),
        ("/Sys/EmployerManager/Orientation/EmployeeOrientationReport.aspx", "Orientation"),
        ("/Sys/Common/Announcements/Announcements.aspx","Announcements"),
        ("/Sys/Employer/HR/PerformanceReviewSetupWizard.aspx","Performance Review Setup Wizard"),

        ("/Sys/Employer/HR/PerformanceReviewJournal.aspx","Performance Journal"),
        ("/Sys/Employer/HR/PerformanceReviewChecklists.aspx","Review Forms"),
        ("/Sys/Employer/HR/PerformanceReviewSessions.aspx","Review Sessions"),
        ("/Sys/Employer/HR/PerformanceReviewCriteriaLibrary.aspx","Criteria Library"),
        ("/Sys/Employer/HR/PerformanceReviewCommentTemplates.aspx","Comment Templates"),
        ("/Sys/Employer/HR/PerformanceReviewWorkflows.aspx","Review Workflows"),
        ("/Sys/Employer/HR/PerformanceReviewReports.aspx","Employee Performance Reports"),
        ("/Sys/Employer/HR/PerformanceReviewFeedback.aspx","360 Degree Feedback"),
        ("/Sys/Employer/HR/PerformanceReviewReminderAlertSettings.aspx","Performance Review Reminder Alert Settings"),

        ("/Sys/Employer/FAQ/KnowledgeBase.aspx","Knowledge Base"),
        ("/Sys/Employer/Kudos/KudosSettings.aspx","Kudos Settings"),
        ("/Sys/Common/Kudos/ManageKudos.aspx","Kudos"),
        ("/Sys/Employer/Kudos/KudosReport.aspx","Kudos Report"),
        ("/Sys/Employer/HR/PerformanceReviewGoals.aspx","Objective & Key Results"),
        ("/Sys/EmployerManager/Employees/Succession.aspx","Succession"),
        ("/Sys/Employer/HR/EmployeeWarnings.aspx","Employee Warnings"),

        ("/Sys/EmployerManager/HR/EmployeeSuggestionReport.aspx","Employee Suggestions Report"),
        ("/Sys/Common/Benefits/EnrollmentWizard/BenefitEnrollmentWizard.aspx","Benefit Enrollment Wizard"),
        ("/Sys/Common/Benefits/Setup/BenefitPlans.aspx","Benefit Plans"),
        ("/Sys/Common/Benefits/LifeEvents/LifeEventsReport.aspx","Life Events"),
        ("/Sys/Common/Benefits/Reports/BenefitEdiReport.aspx","Benefit EDI Report"),
        ("/Sys/Common/Benefits/Templates/BenefitDurationTemplates.aspx","Benefit Duration Templates"),
        ("/Sys/Common/Benefits/Templates/BenefitCoverages.aspx","Benefit Coverages"),
        ("/Sys/Common/Benefits/Templates/BenefitComparisonSummaryTemplates.aspx","Benefit Comparison Summary Templates"),
        ("/Sys/Common/Benefits/Templates/FlexCredits.aspx","Flex Credits"),
        ("/Sys/Common/Benefits/Templates/BenefitForms.aspx","Benefit Forms"),
        ("/Sys/EmployerManager/Benefits/Reports/BeneficiariesReport.aspx","Beneficiaries Report"),
        ("/Sys/EmployerManager/Benefits/Reports/DependentsReport.aspx","Dependents Report"),
        ("/Sys/Common/Benefits/Reports/BenefitEnrollmentReport.aspx","Benefit Approval Report"),
        ("/Sys/Common/Benefits/Setup/BenefitCloneReport.aspx","Benefit Clone Report"),
        ("/Sys/Common/Benefits/Reports/BenefitEdiReport.aspx","Benefit EDI Report"),
        ("/Sys/Common/Benefits/Reports/BenefitsActivitiesReport.aspx","Benefit Activities Report"),
        ("/Sys/Common/Benefits/Reports/EnrollmentsSummaryReport.aspx","Enrollment Summary Report"),
        ("/Sys/Common/Benefits/Reports/InsuranceApplicationsReport.aspx","Insurance Applications Report"),
        ("/Sys/Common/Benefits/Reports/Benefit401KPlanEnrollmentReport.aspx","401(k) Enrollment Report"),
        ("/Sys/Common/Benefits/Reports/BenefitsConsolidatedBillingReport.aspx","Benefits Consolidated Billing Report"),
        ("/Sys/EmployerManager/TimeoffManagement/TimeoffRequest.aspx","Time Off Request"),
        ("/Sys/EmployerManager/TimeoffManagement/TimeoffApprovalDenialReport.aspx","Time Off Approval/Denial Report"),
        ("/Sys/EmployerManager/TimeoffManagement/TimeoffBalanceReport.aspx","Time Off Balance Report"),

        ("/Sys/EmployerManager/TimeoffManagement/TimeoffMiscellaneousSettings.aspx","Time Off Settings: Lock Dates"),
        ("/Sys/Employer/TimeOffAccruals/TimeOffAccrualsProfiles.aspx","Accrual Profiles"),
        ("/Sys/Employer/Payroll/CalendarRules.aspx","Calendar Rules"),
        ("/Sys/Employer/Payroll/HolidayRules.aspx","Holiday Rules"),
        ("/Sys/Common/Payroll/TimeSheetSettings.aspx","Time Sheet Settings"),
        ("/Sys/EmployerManager/Payroll/ImportTimePunches.aspx","Import Time"),
        ("/Sys/EmployerManager/Payroll/TimeCardType.aspx","Time Card Type"),
        ("/Sys/EmployerManager/Payroll/PayrollBatches.aspx","Payroll Batches"),
        ("/Sys/Employer/CustomReport/CustomReport.aspx","Custom Report"),
        ("/Sys/Employer/Reports/DeductionApprovalReport.aspx","Deduction Approval Report"),
        ("/Sys/Employer/TaskManagement/ScheduledReport.aspx","Scheduled Report"),
        ("/Sys/Employer/HR/AnniversaryReport.aspx","Anniversary Report"),
        ("/Sys/Employer/HR/BirthdayReport.aspx","Birthday Report"),
        ("/Sys/Employer/HR/EducationReport.aspx","Education Report"),
        ("/Sys/Employer/HR/EmergencyContactReport.aspx","Emergency Contact Report"),
        ("/Sys/Employer/HR/EmployeeNotesReport.aspx","Employee Notes Report"),
        ("/Sys/Employer/HR/EquipmentReport.aspx","Equipment Report"),
        ("/Sys/Employer/HR/LicenseTrackingReport.aspx","License Tracking Report"),
        ("/Sys/Employer/HR/EmployeeCountReport.aspx","Employee Count Report"),
        ("/Sys/Employer/HR/EmployeeTurnoverReport.aspx","Employee Turnover & Retention Report"),
        ("/Sys/Employer/HR/EmployeeUserAccountsReport.aspx","Employee User Account Report"),
        ("/Sys/Employer/HR/EmployeeEEOReport.aspx","Employee EEO Report"),
        ("/Sys/EmployerManager/I9/Ei9ExpirationReport.aspx","I9 Expiration Report"),
        ("/Sys/Employer/HR/EmployeeSkillReport.aspx","Employee Skill Report"),
        ("/Sys/Employer/Employees/OrganizationChart.aspx","Organization Chart"),
        ("/Sys/Employer/Reports/WorkForceAge.aspx","Workforce Age Report"),
        ("/Sys/Employer/Reports/Vet4212.aspx","VETS Report"),
        ("/Sys/Employer/Reports/PayHistory.aspx","Pay History"),
        ("/Sys/Employer/Reports/PayRates.aspx","Pay Rates"),
        ("/Sys/Employer/HR/TerminationTrend.aspx","Termination Trend"),
        ("/Sys/Common/Reports/SyncChangeReport.aspx","Sync Change Report"),
        ("/Sys/Employer/FileCabinet/FileCabinet.aspx","File Cabinet"),
        ("/Sys/Common/Files/EmployeeForms/EmployeeForms.aspx","Employee Forms"),
        ("/Sys/EmployerManager/Files/EmployeeForms/EmployeeFormsReport.aspx","Employee Forms Report"),
        ("/Sys/EmployerManager/ScheduleManagement/EmployeeSchedule.aspx","Schedule"),
        ("/Sys/EmployerManager/ScheduleManagement/ScheduleDisplaySettings.aspx","Schedule Display Settings"),
        ("/Sys/EmployerManager/ScheduleManagement/EmployeeRejectedShift.aspx","Rejected Shifts"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/JobPostsSettings.aspx","Manage Jobs"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/ApplicationFormSettings.aspx","Application Form Settings"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/ManageInterviewsChecklists.aspx","Interview Checklists"),
        ("/Sys/Employer/ApplicantTrackingSystem/JobPostingStageSettings.aspx","Applicant Status Settings"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/ApplicantsRecruitmentPipeline.aspx","Recruiting Pipeline"),
        ("/Sys/Employer/ApplicantTrackingSystem/ExternalJobBoardSettings.aspx","External Job Board Settings"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/ApplicantsReport.aspx", "Applicant Report"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/Quizzes.aspx","Quizzes"),
        ("/Sys/Common/Tasks/Kanban.aspx","Task Board"),
        ("/Sys/Common/Tasks/Task.aspx","Task"),
        ("/Sys/Common/Tasks/TaskGroup.aspx","Task Group"),
        ("/Sys/Common/Tasks/TaskList.aspx","Task List"),
        ("/Sys/Common/MessageCenter/Messages.aspx","Messages"),

        ("/Sys/Employer/HR/PerformanceReviewGoalReminderAlertSetting.aspx", "Performance Review Goal Reminder Alert Setting"),
        ("/Sys/Employer/HR/PerformanceReviewDashboard.aspx", "Performance Review Dashboard"),
        ("/Sys/EmployerManager/TimeoffManagement/TimeoffCalendar.aspx", "Time Off Calendar"),
        ("/Sys/Employer/HR/CompanyHolidays.aspx", "Company Holidays"),
        ("/Sys/UserProfile.aspx","User Profile"),
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
