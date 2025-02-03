from playwright.sync_api import sync_playwright
from faker import Faker
import os
from Payload.login import Login
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire

from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from pages.hr_360degreefeedback_page import Hr360DegreeFeedback
from utils.logger import setup_logger
import time
import logging
import pytest


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


def test_360degreefeedback_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file("E:/MPOPlayWright/tests/credentials.txt")

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)
    logger.info("Setting up the test environment(New Hire)")
    page = browser.new_page()
    login_page = LoginPage(page)
    hr_360degreefeedback = Hr360DegreeFeedback(page)
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


    hr_360degreefeedback.navigate(BASE_URL + '/Sys/Employer/HR/PerformanceReviewFeedback.aspx')
    try:
        assert  hr_360degreefeedback.verify_page_title("360 Degree Feedback")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    hr_360degreefeedback.add_360_degree_feedback().click()
    hr_360degreefeedback.session().click()
    hr_360degreefeedback.type_session().fill("arf")
    hr_360degreefeedback.enter_session().press("Enter")
    hr_360degreefeedback.employee().click()
    hr_360degreefeedback.type_employee().fill("ca")
    hr_360degreefeedback.enter_employee().press("Enter")
    hr_360degreefeedback.reviewer().click()
    hr_360degreefeedback.select_reviewer().click()
    hr_360degreefeedback.click_reviewer().click()
    hr_360degreefeedback.save().click()
    logger.info("Success: Added 360degreefeedback")
    time.sleep(5)
    hr_360degreefeedback.delete().click()
    hr_360degreefeedback.yes().click()
    logger.info("Success: Deleted 360degreefeedback")

