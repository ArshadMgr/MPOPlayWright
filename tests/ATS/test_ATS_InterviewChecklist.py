from playwright.sync_api import sync_playwright
from faker import Faker
import os
from Payload.login import Login
import pytest
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from utils.config import BASE_URL
from utils.config import USERNAME
from utils.config import excel_file_path_A
from utils.config import excel_file_path_H
from utils.config import CredentilasPath_A
from utils.config import CredentilasPath_H
from pages.login_page import LoginPage
from pages.ats_interviewchecklist_page import InterviewChecklist
from utils.logger import setup_logger
import time
import logging
import openpyxl
import pytest
from  Payload.data_validation import validate_username, validate_email, validate_age

# Path to the Excel file
excel_file_path = excel_file_path_H

logger = setup_logger()
# Setup logger
logger = logging.getLogger("TestLogger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


@pytest.fixture
def fake_data():
    return Faker()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser

# Function to read test data from the Excel file
def get_test_data(sheet_name, cell_reference):
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook[sheet_name]
    data = sheet[cell_reference].value
    workbook.close()
    return data

# Fetch test data from the Excel file
checklist_name = get_test_data("InterviewLists", "A2")
interviewer_instructions = get_test_data("InterviewLists", "B2")
question = get_test_data("InterviewLists", "C2")

def test_announcements_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_H)

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(Add Job Category)")
    page = browser.new_page()
    login_page = LoginPage(page)
    ATSIC = InterviewChecklist(page)
    login_page.navigate(BASE_URL + '/login.aspx')

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
    userPayload = new_hire.NewHire(page)
    userPayload.setFirstName("CharlesCR")
    assert userPayload.getFirstName() == "CharlesCR"

    ATSIC.navigate(BASE_URL + '/Sys/EmployerManager/ApplicantTrackingSystem/ManageInterviewsChecklists.aspx')
    try:
        assert ATSIC.verify_page_title("Interview Checklists")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed


    # Interview CheckLists
    ATSIC.interview_tab().click()
    ATSIC.add_interviewlist().click()
    ATSIC.checklist_name().fill(checklist_name)
    ATSIC.associate_job().click()
    ATSIC.enter_associate_job().fill("Hr Manager")
    ATSIC.enter_associate_job().press("Enter")
    ATSIC.interviewer_instructions().fill(interviewer_instructions)
    ATSIC.active().click()
    ATSIC.save().click()
    time.sleep(2)
    #add Question
    ATSIC.add_question().click()
    ATSIC.question().fill(question)
    ATSIC.active1().click()
    ATSIC.save().click()
    time.sleep(2)
    ATSIC.save_sort().click()
    time.sleep(2)
    ATSIC.cancel().click()
    time.sleep(2)

    # Interview
    ATSIC.schedule_interview().click()
    ATSIC.interview_list().click()
    ATSIC.select_interview_list().fill("Testing list")
    ATSIC.select_interview_list().press("Enter")
    time.sleep(2)
    ATSIC.applicant().click()
    ATSIC.select_applicant().fill("John")
    ATSIC.select_applicant().press("Enter")
    time.sleep(2)
    ATSIC.interview_date().click()
    ATSIC.interview_date().fill("8/21/2025 12:57 am")
    ATSIC.interview_date().press("Enter")
    time.sleep(2)
    ATSIC.interviewer_list().click()
    ATSIC.select_interviewer().click()
    ATSIC.close_list().click()
    time.sleep(2)
    ATSIC.location().click()
    ATSIC.location_select().fill("ALA")
    ATSIC.location_select().press("Enter")
    time.sleep(2)
    ATSIC.interviewer_list().click()
    ATSIC.select_interviewer().click()
    ATSIC.close_list().click()
    time.sleep(2)
    ATSIC.schedule_done().click()

    #Delete Section
    time.sleep(2)
    ATSIC.search_date().fill("8/21/2025")
    ATSIC.search().click()
    time.sleep(2)
    ATSIC.delete().click()
    ATSIC.yes().click()
    time.sleep(2)

    page.goto("https://mypaperlessoffice.com/app/Sys/EmployerManager/ApplicantTrackingSystem/ManageInterviewsChecklists.aspx")
    ATSIC.interview_tab().click()
    time.sleep(2)
    ATSIC.delete_list().click()
    ATSIC.yes().click()
    time.sleep(2)
