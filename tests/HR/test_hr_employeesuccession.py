from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from faker import Faker
import os
from Payload.login import Login
import pytest
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from pages import login_page, hr_employeesuccession_page
from utils.config import BASE_URL
from utils.config import USERNAME
from utils.config import excel_file_path_A
from utils.config import excel_file_path_H
from utils.config import CredentilasPath_A
from utils.config import CredentilasPath_H
from pages.login_page import LoginPage
from pages.hr_employeesuccession_page import EmployeeSuccession
from utils.logger import setup_logger
import time
import openpyxl

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
employee = get_test_data("EmployeeSuccession", "A2")
# Fetch test data from the Excel file
succession = get_test_data("EmployeeSuccession", "B2")
# Fetch test data from the Excel file
rediness = get_test_data("EmployeeSuccession", "C2")
# Fetch test data from the Excel file
note = get_test_data("EmployeeSuccession", "C2")

def test_succession_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_A)

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(New Hire)")
    page = browser.new_page()
    login_page = LoginPage(page)
    Employee_Succession = EmployeeSuccession(page)
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

    Employee_Succession.navigate(BASE_URL + '/Sys/EmployerManager/Employees/Succession.aspx')
    try:
        assert Employee_Succession.verify_page_title("Employee Succession")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    #adding succession
    Employee_Succession.add_succession().click()
    Employee_Succession.select_employee().click()
    Employee_Succession.employee().fill(employee)
    Employee_Succession.enter_employee().press("Enter")
    time.sleep(5)
    Employee_Succession.select_succession().click()
    Employee_Succession.succession().fill(succession)
    Employee_Succession.enter_succession().press("Enter")
    time.sleep(5)
    Employee_Succession.select_readiness().click()
    Employee_Succession.readiness().fill(rediness)
    Employee_Succession.enter_readiness().press("Enter")
    Employee_Succession.note().fill(note)
    Employee_Succession.save_button().click()
    logger.info("Success: Success Added employee Succession")
    #delete succession
    Employee_Succession.delete().click()
    Employee_Succession.yes().click()
    logger.info("Success: Deleted emplyee sucession")
    page.pause()