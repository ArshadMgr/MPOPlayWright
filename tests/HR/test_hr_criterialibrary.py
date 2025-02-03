from playwright.sync_api import sync_playwright
from faker import Faker
import os
from Payload.login import Login
import pytest
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from pages import login_page, hr_criterialibrary_page
from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from pages.hr_criterialibrary_page import HrCriteriaLibrary
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
Header = get_test_data("CriteriaLibrary", "A2")
Weight = get_test_data("CriteriaLibrary", "B2")
Description = get_test_data("CriteriaLibrary", "C2")


def test_criterialibrary_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file("E:/MPOPlayWright/tests/credentials.txt")

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(Criteria Library)")
    page = browser.new_page()
    login_page = LoginPage(page)
    hr_criterialibrary = HrCriteriaLibrary(page)
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

    hr_criterialibrary.navigate(BASE_URL + '/Sys/Employer/HR/PerformanceReviewCriteriaLibrary.aspx')
    try:
        assert hr_criterialibrary.verify_page_title("Criteria Library")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError_NewHire.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    #adding criteria library
    hr_criterialibrary.add_criteria().click()
    hr_criterialibrary.header().fill(Header)
    hr_criterialibrary.weight().fill(Weight)
    hr_criterialibrary.description().fill(Description)
    hr_criterialibrary.status().click()
    hr_criterialibrary.save().click()
    time.sleep(5)
    logger.info("Success: Criteria Library added")
    #deleting criteria library
    hr_criterialibrary.delete().click()
    hr_criterialibrary.yes().click()
    logger.info("Success: Criteria Library deleted")