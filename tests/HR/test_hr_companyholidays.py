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
from pages.hr_companyholidays_page import HrCompanyHolidays
from utils.logger import setup_logger
import logging
import pytest
import time
import openpyxl

logger = setup_logger()
# Setup logger
logger = logging.getLogger("TestLogger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Path to the Excel file
excel_file_path = excel_file_path_H

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
company_holiday = get_test_data("CompanyHoliday", "A2")
holiday_date=get_test_data("CompanyHoliday", "B2")
company_holiday2 = get_test_data("CompanyHoliday", "C2")
holiday_date2 = get_test_data("CompanyHoliday", "D2")


def test_companyholiday_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_H)

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
    hr_companyholidays.holiday_name().fill(company_holiday)
    hr_companyholidays.date().fill(holiday_date)
    hr_companyholidays.paid().click()
    hr_companyholidays.position().click()
    hr_companyholidays.save().click()
    logger.info("Success: Company holiday added")
    #edit company holiday
    hr_companyholidays.edit_holiday().click()
    hr_companyholidays.holiday_name().fill(company_holiday2)
    hr_companyholidays.date().fill(holiday_date2)
    hr_companyholidays.save().click()
    logger.info("Success: Company holiday updated")
    #Delete compnay holiday
    hr_companyholidays.delete_holiday().click()
    hr_companyholidays.yes().click()
    logger.info("Success: Company holiday updated")

    page.pause()