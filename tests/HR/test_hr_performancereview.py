from playwright.sync_api import sync_playwright
from faker import Faker
import os
from Payload.login import Login
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from utils.config import BASE_URL
from utils.config import USERNAME
from utils.config import excel_file_path_A
from utils.config import excel_file_path_H
from utils.config import CredentilasPath_A
from utils.config import CredentilasPath_H
from pages.login_page import LoginPage
from pages.hr_performancereview_page import HrPerformanceReview
from utils.logger import setup_logger
import time
import logging
import pytest
import openpyxl

# Path to the Excel file
excel_file_path = excel_file_path_A

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
Name = get_test_data("PerformanceReview", "A2")
Description = get_test_data("PerformanceReview", "B2")
Instruction = get_test_data("PerformanceReview", "C2")

def test_newhire_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_A)

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(Performance Review)")
    page = browser.new_page()
    login_page = LoginPage(page)
    hr_performancereview = HrPerformanceReview(page)
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


    hr_performancereview.navigate(BASE_URL + '/Sys/Employer/HR/PerformanceReviewChecklists.aspx')
    try:
        assert  hr_performancereview.verify_page_title("Review Forms")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    #Add performance review checklist
    hr_performancereview.add_review_form().click()
    hr_performancereview.name().fill(Name)
    hr_performancereview.description().fill(Description)
    hr_performancereview.instructions().fill(Instruction)
    hr_performancereview.status().click()
    hr_performancereview.save().click()
    time.sleep(5)
    logger.info("Success: Added performance review checklist")
    #edit Performance review chhecklist
    hr_performancereview.edit().click()
    hr_performancereview.name().fill("Name")
    hr_performancereview.description().fill("Testing the description")
    hr_performancereview.instructions().fill("Testing the instructions ")
    hr_performancereview.save().click()
    logger.info("Success: Updated performance review checklist")

    #delete performance review checklist
    hr_performancereview.delete().click()
    hr_performancereview.yes().click()
    logger.info("Success: Deleted performance view checklist")