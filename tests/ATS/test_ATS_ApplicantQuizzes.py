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
from pages.ats_applicantquizzes_page import ApplicantQuizzes
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
quiz_name = get_test_data("Quiz", "A3")
score = get_test_data("Quiz", "B3")
description = get_test_data("Quiz", "C3")
question = get_test_data("Quiz", "D3")
question_score = get_test_data("Quiz", "E3")

def test_announcements_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_H)

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(Add Job Category)")
    page = browser.new_page()
    login_page = LoginPage(page)
    ATSAQ = ApplicantQuizzes(page)
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

    ATSAQ.navigate(BASE_URL + '/Sys/EmployerManager/ApplicantTrackingSystem/Quizzes.aspx')
    try:
        assert ATSAQ.verify_page_title("Applicant Quizzes")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    # Add Quiz
    ATSAQ.add_quiz().click()
    ATSAQ.quiz_name().fill(quiz_name)
    ATSAQ.score().fill(score)
    ATSAQ.description().fill(description)
    ATSAQ.save().click()
    time.sleep(2)
    ATSAQ.question().fill(question)
    ATSAQ.question_score().fill(question_score)
    ATSAQ.save_question().click()
    ATSAQ.back().click()
    time.sleep(2)

    #Delete Quiz
    ATSAQ.delete().click()
    ATSAQ.yes().click()