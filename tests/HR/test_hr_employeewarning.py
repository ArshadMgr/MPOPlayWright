from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from faker import Faker
import os
from Payload.login import Login
import pytest
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from pages import login_page, hr_employeewarning_page
from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from pages.hr_employeewarning_page import EmployeeWarning
from utils.logger import setup_logger
import time
import openpyxl
from utils.config import excel_file_path_A
from utils.config import excel_file_path_H
from utils.config import CredentilasPath_A
from utils.config import CredentilasPath_H

import logging
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

# Path to the Excel file
excel_file_path = excel_file_path_A

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
reason = get_test_data("EmployeeWarning", "A3")
# Fetch test data from the Excel file
description = get_test_data("EmployeeWarning", "B3")
# Fetch test data from the Excel file
category = get_test_data("EmployeeWarning", "A6")
# Fetch test data from the Excel file
category_description = get_test_data("EmployeeWarning", "B6")
# Fetch test data from the Excel file
incident_date = get_test_data("EmployeeWarning", "A9")
# Fetch test data from the Excel file
incident_description = get_test_data("EmployeeWarning", "B9")

def test_succession_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_A)

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(Employee Warning)")
    page = browser.new_page()
    login_page = LoginPage(page)
    Employee_Warning = EmployeeWarning(page)
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

    Employee_Warning.navigate(BASE_URL + '/Sys/Employer/HR/EmployeeWarnings.aspx')
    try:
        assert Employee_Warning.verify_page_title("Employee Warnings")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    #Mange Reason section
    Employee_Warning.manage_reason().click()
    Employee_Warning.add_reason().click()
    Employee_Warning.reason().fill(reason)
    Employee_Warning.reason_description().fill(description)
    Employee_Warning.save().click()
    page.goto('https://mypaperlessoffice.com/app/Sys/Employer/HR/EmployeeWarnings.aspx')

    # Mange category section
    Employee_Warning.manage_category().click()
    Employee_Warning.add_category().click()
    Employee_Warning.category().fill(category)
    Employee_Warning.category_description().fill(category_description)
    Employee_Warning.save().click()
    page.goto('https://mypaperlessoffice.com/app/Sys/Employer/HR/EmployeeWarnings.aspx')

    # Add Warning section
    Employee_Warning.add_warning().click()
    Employee_Warning.add_employee().click()
    Employee_Warning.type_employee().fill("amy")
    Employee_Warning.enter_employee().press("Enter")
    time.sleep(3)
    Employee_Warning.add_categoryy().click()
    Employee_Warning.type_categoryy().fill("Test")
    Employee_Warning.enter_categoryy().press("Enter")
    Employee_Warning.add_reasons().click()
    Employee_Warning.type_reasons().fill("Test")
    Employee_Warning.enter_reasons().press("Enter")
    Employee_Warning.incident_date().fill(incident_date)
    Employee_Warning.incident_description().fill(incident_description)
    Employee_Warning.save_change().click()
    time.sleep(4)

    # Delete Warning section
    Employee_Warning.delete().click()
    Employee_Warning.yes().click()

    # Mange category section
    Employee_Warning.manage_category().click()
    Employee_Warning.category_delete().click()
    Employee_Warning.yes().click()
    page.goto('https://mypaperlessoffice.com/app/Sys/Employer/HR/EmployeeWarnings.aspx')

    # Delete Reason section
    Employee_Warning.manage_reason().click()
    Employee_Warning.category_delete().click()
    Employee_Warning.yes().click()
    page.goto('https://mypaperlessoffice.com/app/Sys/Employer/HR/EmployeeWarnings.aspx')