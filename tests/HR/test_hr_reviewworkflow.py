from playwright.sync_api import sync_playwright
from faker import Faker
import os
from Payload.login import Login
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from pages.hr_reviewworkflow_page import HrReviewWorkflow
from utils.logger import setup_logger
import time
import logging
import openpyxl
import pytest
from  Payload.data_validation import validate_username, validate_email, validate_age

# Path to the Excel file
excel_file_path = "E:/MPOPlayWright/Payload/test_Data/TestData.xlsx"

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
workflow_name = get_test_data("ReviewWorkflow", "A2")
description = get_test_data("ReviewWorkflow", "B2")

def test_reviewworkflow_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file("E:/MPOPlayWright/tests/credentials.txt")

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(New Hire)")
    page = browser.new_page()
    login_page = LoginPage(page)
    hr_reviewworkflow = HrReviewWorkflow(page)
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


    hr_reviewworkflow.navigate(BASE_URL + '/Sys/Employer/HR/PerformanceReviewWorkflows.aspx')
    try:
        assert  hr_reviewworkflow.verify_page_title("Review Workflows")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    #add review workflow
    hr_reviewworkflow.add_workflow().click()
    hr_reviewworkflow.workflow_name().fill(workflow_name)
    hr_reviewworkflow.add_step().click()
    hr_reviewworkflow.user_type().click()
    hr_reviewworkflow.type_user_type().fill("employer")
    hr_reviewworkflow.enter_user_type().press("Enter")
    hr_reviewworkflow.description().fill(description)
    hr_reviewworkflow.save_step().click()
    hr_reviewworkflow.save().click()
    logger.info("Success: Added review workflow")
    #delete review workflow
    hr_reviewworkflow.delete().click()
    hr_reviewworkflow.yes().click()
    logger.info("Success: Deleted review workflow")
