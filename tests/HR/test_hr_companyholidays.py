from playwright.sync_api import sync_playwright
from faker import Faker
import os
from Payload.login import Login
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from pages.hr_companyholidays_page import HrCompanyHolidays
from utils.logger import setup_logger
import logging
import pytest
import time


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

def test_companyholiday_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file("C:/Users/pc planet/Desktop/MPOPlayWright/tests/credentials.txt")

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(New Hire)")
    page = browser.new_page()
    login_page = LoginPage(page)
    hr_companyholidays = HrCompanyHolidays(page)
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


    hr_companyholidays.navigate(BASE_URL + '/Sys/Employer/HR/CompanyHolidays.aspx')
    try:
        assert hr_companyholidays.verify_page_title("Company Holidays")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    #add company holiday
    hr_companyholidays.add_holiday().click()
    hr_companyholidays.holiday_name().fill("National Holiday")
    hr_companyholidays.date().fill("1/22/2025")
    hr_companyholidays.paid().click()
    hr_companyholidays.position().click()
    hr_companyholidays.save().click()
    logger.info("Success: Company holiday added")
    #edit company holiday
    hr_companyholidays.edit_holiday().click()
    hr_companyholidays.holiday_name().fill("Holiday")
    hr_companyholidays.date().fill("10/20/2025")
    hr_companyholidays.save().click()
    logger.info("Success: Company holiday updated")
    #Delete compnay holiday
    hr_companyholidays.delete_holiday().click()
    hr_companyholidays.yes().click()
    logger.info("Success: Company holiday updated")