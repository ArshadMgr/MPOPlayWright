from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from faker import Faker
from MPOPlayWright.Payload.new_hire import NewHire

import pytest
from MPOPlayWright.Payload import new_hire
from MPOPlayWright.utils.config import BASE_URL
from MPOPlayWright.utils.config import USERNAME
from MPOPlayWright.utils.config import PASSWORD
from MPOPlayWright.pages.login_page import LoginPage
from MPOPlayWright.utils.logger import setup_logger
import time
import logging


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


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser


def test_setup(browser, fake_data):
    logger.info("Setting up the test environment(Demo)")
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL + '/login.aspx')

    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
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

    logger.info("Starting test: test_Page_Crashes")
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/NewHireReport.aspx")
    assert "New Hire Report" in page.title()
    page.goto(BASE_URL + "/Sys/EmployerManager/Employees/EditEmployees.aspx")
    assert "Edit Employees" in page.title()

    # Generate fake data using the fake_data fixture
    fake_name = fake_data.name()
    fake_email = fake_data.email()

    logger.info(f"Generated fake name: {fake_name} and fake email: {fake_email}")
    # You can use the fake_name and fake_email in your tests here

    page.close()
