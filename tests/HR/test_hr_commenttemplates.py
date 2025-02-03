from playwright.sync_api import sync_playwright
from faker import Faker
import os
from Payload.login import Login
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from pages.hr_commenttemplates_page import HrCommentTemplates
from utils.logger import setup_logger
import time
import logging
import pytest
import openpyxl

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
comment_name = get_test_data("CommentTemplates", "A2")
Comments = get_test_data("CommentTemplates", "B2")


def test_commenttemplates_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file("E:/MPOPlayWright/tests/credentials.txt")


    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(Commenttemplate)")
    page = browser.new_page()
    login_page = LoginPage(page)
    hr_commenttemplates = HrCommentTemplates(page)
    login_page.navigate(BASE_URL + '/login.aspx')

    login_page.enter_username(USERNAME)
    login_page.enter_password(decrypted_password)
    login_page.click_login()

    login_page.clik_ee_role()
    login_page.enter_employer("Employer")
    login_page.press_enter()
    login_page.click_go_button()



    # Add assertions to verify successful login
    logger.info("Completed test: test_valid_login")

    time.sleep(10)

    assert "Dashboard" in page.title()
    userPayload = new_hire.NewHire(page)
    userPayload.setFirstName("CharlesCR")
    assert userPayload.getFirstName() == "CharlesCR"


    hr_commenttemplates.navigate(BASE_URL + '/Sys/Employer/HR/PerformanceReviewCommentTemplates.aspx')
    try:
        assert  hr_commenttemplates.verify_page_title("Comment Templates")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

     #Add Comment Template
    hr_commenttemplates.add_template().click()
    hr_commenttemplates.comment_name().fill(comment_name)
    hr_commenttemplates.Comments().fill(Comments)
    hr_commenttemplates.status().click()
    hr_commenttemplates.save().click()
    logger.info("Success: Added Comment Template")
    #delete Commet Template
    hr_commenttemplates.delete().click()
    hr_commenttemplates.yes().click()
    logger.info("Success: Deleted comment Template")
    page.pause()
