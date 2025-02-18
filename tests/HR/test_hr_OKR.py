from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from faker import Faker
import os
from Payload.login import Login
import pytest
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from pages import login_page, hr_OKR_page
from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from pages.hr_OKR_page import OKR
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
title = get_test_data("OKR", "A3")
# Fetch test data from the Excel file
description = get_test_data("OKR", "B3")
# Fetch test data from the Excel file
objective_title = get_test_data("OKR", "A6")
# Fetch test data from the Excel file
objective_description = get_test_data("OKR", "B6")
# Fetch test data from the Excel file
start_date = get_test_data("OKR", "A8")
# Fetch test data from the Excel file
due_date = get_test_data("OKR", "B8")

def test_succession_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_A)

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(OKR)")
    page = browser.new_page()
    login_page = LoginPage(page)
    OKR_page = OKR(page)
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

    OKR_page.navigate(BASE_URL + '/Sys/Employer/HR/PerformanceReviewGoals.aspx')
    try:
        assert OKR_page.verify_page_title("Objective & Key Results")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    #Add OKR Category
    OKR_page.okr_category().click()
    OKR_page.add_okr().click()
    OKR_page.add_title().fill(title)
    OKR_page.add_description().fill(description)
    OKR_page.save().click()
    time.sleep(3)
    page.goto('https://mypaperlessoffice.com/app/Sys/Employer/HR/PerformanceReviewGoals.aspx')

    #Add OKR (Company)
    OKR_page.add_okrcompany().click()
    OKR_page.objective_title().fill(objective_title)
    OKR_page.objective_description().fill(objective_title)
    OKR_page.type_category().click()
    OKR_page.select_category().fill("Test OKR")
    OKR_page.enter_category().press("Enter")
    OKR_page.start_date().fill(start_date)
    OKR_page.due_date().fill(due_date)
    #object type
    OKR_page.viewing_rights().click()
    OKR_page.save_okr().click()
    time.sleep(3)

    #delete okr (company)
    OKR_page.company_okr().click()
    OKR_page.delete_company().click()
    OKR_page.yes().click()

    #Add OKR (Department)
    OKR_page.add_okrcompany().click()
    OKR_page.objective_title().fill(objective_title)
    OKR_page.objective_description().fill(objective_title)
    OKR_page.type_category().click()
    OKR_page.select_category().fill("Test OKR")
    OKR_page.enter_category().press("Enter")
    OKR_page.start_date().fill(start_date)
    OKR_page.due_date().fill(due_date)
    OKR_page.select_department().click()
    OKR_page.type_department().fill("Dep")
    OKR_page.enter_department().press("Enter")
    OKR_page.viewing_rights().click()
    OKR_page.save_okr().click()
    time.sleep(3)

    #delete okr (department)
    OKR_page.delete_department().click()
    OKR_page.yes().click()

    #Add OKR (Personal)
    OKR_page.add_okrcompany().click()
    OKR_page.objective_title().fill(objective_title)
    OKR_page.objective_description().fill(objective_title)
    OKR_page.type_category().click()
    OKR_page.select_category().fill("Test OKR")
    OKR_page.enter_category().press("Enter")
    OKR_page.start_date().fill(start_date)
    OKR_page.due_date().fill(due_date)
    OKR_page.select_personal().click()
    OKR_page.type_personal().fill("Per")
    OKR_page.enter_personal().press("Enter")
    OKR_page.type_assignee().click()
    OKR_page.select_assignee().fill("amy")
    OKR_page.enter_assignee().press("Enter")
    OKR_page.viewing_rights().click()
    OKR_page.save_okr().click()
    time.sleep(3)

    #delete okr (department)
    OKR_page.delete_personal().click()
    OKR_page.yes().click()

    # delete OKR Category
    OKR_page.okr_category().click()
    OKR_page.delete_category().click()
    OKR_page.yes().click()
    time.sleep(3)
    page.goto('https://mypaperlessoffice.com/app/Sys/Employer/HR/PerformanceReviewGoals.aspx')