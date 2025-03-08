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
    login_page.enter_employer("Manager")
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
        ("/Sys/EmployerManager/Employees/NewHire.aspx", "New Hire"),
        ("/Sys/EmployerManager/Employees/NewHireReport.aspx", "New Hire Report"),
        ("/Sys/EmployerManager/Employees/EditEmployees.aspx", "Edit Employees"),
        ("/Sys/EmployerManager/Employees/TerminateEmployee.aspx", "Employee Termination"),
        ("/Sys/EmployerManager/Employees/TerminationReport.aspx", "Termination Report"),
        ("/Sys/Common/CompanyManagement/CompanyLevelsHierarchy.aspx", "Company Levels Hierarchy"),
        ("/Sys/Employer/Onboarding/OnboardingReport.aspx", "Onboarding Report"),
        ("/Sys/Manager/HR/PerformanceReviewDashboard.aspx", "Performance Review Dashboard"),
        ("/Sys/Manager/HR/PerformanceReviewJournal.aspx","Performance Journal"),
        ("/Sys/Manager/HR/PerformanceReviewReports.aspx", "Employee Performance Reports"),
        ("/Sys/Manager/FAQ/KnowledgeBase.aspx","Knowledge Base"),
        ("/Sys/Common/Kudos/ManageKudos.aspx","Kudos"),
        ("/Sys/Employer/Kudos/KudosReport.aspx","Kudos Report"),
        ("/Sys/Manager/HR/PerformanceReviewGoals.aspx", "Objectives & Key Results"),
        ("/Sys/Manager/HR/CompanyHolidays.aspx","Company Holidays"),
        ("/Sys/EmployerManager/Employees/Succession.aspx","Succession"),
        ("/Sys/Manager/HR/EmployeeWarnings.aspx", "Employee Warnings"),
        ("/Sys/EmployerManager/HR/EmployeeSuggestionReport.aspx", "Employee Suggestions Report"),
        ("/Sys/Common/Benefits/EnrollmentWizard/BenefitEnrollmentWizard.aspx", "Benefit Enrollment Wizard"),
        ("/Sys/EmployerManager/Benefits/Reports/BeneficiariesReport.aspx", "Beneficiaries Report"),
        ("/Sys/EmployerManager/Benefits/Reports/DependentsReport.aspx", "Dependents Report"),

        ("/Sys/Common/Benefits/Reports/EnrollmentsSummaryReport.aspx", "Enrollment Summary Report"),
        ("/Sys/EmployerManager/TimeoffManagement/TimeoffRequest.aspx", "Time Off Request"),
        ("/Sys/EmployerManager/TimeoffManagement/TimeoffApprovalDenialReport.aspx", "Time Off Approval/Denial Report"),
        ("/Sys/EmployerManager/TimeoffManagement/TimeoffBalanceReport.aspx","Time Off Balance Report"),
        ("/Sys/EmployerManager/TimeoffManagement/TimeoffCalendar.aspx", "Time Off Calendar"),

        ("/Sys/Manager/HR/AnniversaryReport.aspx", "Anniversary Report"),
        ("/Sys/Manager/HR/BirthdayReport.aspx", "Employee Birthday Report"),
        ("/Sys/Manager/HR/EducationReport.aspx", "Education Report"),
        ("/Sys/Manager/HR/EmergencyContactReport.aspx", "Emergency Contact Report"),
        ("/Sys/Manager/HR/EmployeeNotesReport.aspx", "Employee Notes Report"),
        ("/Sys/Manager/HR/EquipmentReport.aspx", "Equipment Report"),
        ("/Sys/Manager/HR/LicenseTrackingReport.aspx", "License Tracking Report"),

        ("/Sys/EmployerManager/HR/PreviousEmployersReport.aspx", "Previous Employers Report"),
        ("/Sys/Employer/HR/TerminationTrend.aspx", "Termination Trend"),
        ("/Sys/Manager/FileCabinet/FileCabinet.aspx", "File Cabinet"),
        ("/Sys/EmployerManager/Files/EmployeeForms/EmployeeFormsReport.aspx", "Employee Forms Report"),
        ("/Sys/EmployerManager/ScheduleManagement/EmployeeSchedule.aspx", "Schedule"),
        ("/Sys/EmployerManager/ScheduleManagement/EmployeeRejectedShift.aspx", "Rejected Shifts"),
        ("/Sys/Common/Tasks/Kanban.aspx", "Task Board"),
        ("/Sys/Common/Tasks/Task.aspx","Task"),
        ("/Sys/Common/Tasks/TaskGroup.aspx","Task Group"),
        ("/Sys/Common/Tasks/TaskList.aspx","Task List"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/JobPostsSettings.aspx","Manage Jobs"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/ApplicationFormSettings.aspx","Application Form Settings"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/ManageInterviewsChecklists.aspx","Interview Checklists"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/ApplicantsRecruitmentPipeline.aspx","Recruiting Pipeline"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/ApplicantsReport.aspx","Applicant Report"),
        ("/Sys/EmployerManager/ApplicantTrackingSystem/Quizzes.aspx", "Quizzes"),
        ("/Sys/Common/MessageCenter/Messages.aspx", "Messages"),
        ("/Sys/UserProfile.aspx", "User Profile"),
        ("/EmployerManager/Benefits/Reports/BenefitEligibilityReport.aspx", "Benefit Eligibility Report"),
        ("/Sys/Employer/Payroll/TimeSheet.aspx", "Time Sheet"),
        ("/Sys/logoff.aspx", "Login"),
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
