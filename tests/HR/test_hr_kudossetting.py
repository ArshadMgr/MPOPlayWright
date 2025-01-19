from playwright.sync_api import sync_playwright
from faker import Faker
import os
from Payload.login import Login
import pytest
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from pages.hr_kudossetting_page import HrKudosSetting
from utils.logger import setup_logger
import time
import logging
import pytest
from  Payload.data_validation import validate_username, validate_email, validate_age

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



def test_Kudos_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file("C:/Users/pc planet/Desktop/MPOPlayWright/tests/credentials.txt")

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(New Hire)")
    page = browser.new_page()
    login_page = LoginPage(page)
    hr_kudossetting = HrKudosSetting(page)
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

    hr_kudossetting.navigate(BASE_URL + '/Sys/Employer/Kudos/KudosSettings.aspx')
    try:
        assert hr_kudossetting.verify_page_title("Kudos Settings")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    #adding kudos settings
    hr_kudossetting.kudos_category().click()
    time.sleep(5)
    hr_kudossetting.category_name().fill("Kudos testing")
    hr_kudossetting.select_icon().click()
    hr_kudossetting.type_icon().fill("500")
    hr_kudossetting.enter_icon().press("Enter")
    hr_kudossetting.save().click()
    time.sleep(10)
    logger.info("Success: Added Kudos Settings")
    #delete Kudos settings
    hr_kudossetting.delete_category().click()
    time.sleep(5)
    hr_kudossetting.yes().click()
