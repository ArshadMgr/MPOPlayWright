from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from faker import Faker
import os
from pytest_check import check
from MPOPlayWright.Payload.login import Login
from MPOPlayWright.Payload.new_hire import NewHire
import pytest
from MPOPlayWright.Payload.soft_assertion_helper import SoftAssertContext
from MPOPlayWright.Payload import new_hire
from MPOPlayWright.pages import login_page, newhire_page
from MPOPlayWright.utils.config import BASE_URL
from MPOPlayWright.utils.config import USERNAME
from MPOPlayWright.pages.login_page import LoginPage
from MPOPlayWright.pages.newhire_page import NewHirePage
from MPOPlayWright.utils.logger import setup_logger
import time
import logging
import logging
import pytest
from cryptography.fernet import Fernet
from MPOPlayWright.Payload.security import generate_key, save_credentials_to_file, encrypt_message, load_credentials_from_file
from  MPOPlayWright.Payload.data_validation import validate_username, validate_email, validate_age
from MPOPlayWright.Payload.ai_validation_helper import validate_with_openai

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



def test_newhire_Setup(browser, fake_data,):
    with SoftAssertContext() as soft_assert:
        mpologin = Login()
    key, encrypted_password = mpologin.load_credentials_from_file("credentials.txt")

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(New Hire)")
    page = browser.new_page()
    login_page = LoginPage(page)
    newhire_page = NewHirePage(page)
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

    # Generate fake data
    first_name = fake_data.first_name_female()
    middle_name = fake_data.first_name_female()
    last_name = fake_data.last_name_female()
    user_name = fake_data.user_name()
    assert validate_username(user_name)
    #assert validate_with_openai("username", user_name), f"Invalid username: {user_name}"

    logger.info(f"Generated fake: "
                f": first name->: {first_name} "
                f": Middle Name->: {middle_name}"
                f": Last Name->: {last_name}"
                f": User Name->:{user_name}")

    logger.info("Starting test: test_Demographics Section")
    login_page.navigate(BASE_URL + "/Sys/EmployerManager/Employees/NewHireReport.aspx")


    try:
        assert newhire_page.verify_page_title("New Hire Report")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("screenshots", "AssertionError_NewHireReport.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed


    newhire_page.navigate(BASE_URL + '/Sys/EmployerManager/Employees/NewHire.aspx')
    try:
        assert newhire_page.verify_page_title("New Hire")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("screenshots", "AssertionError_NewHire.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    newhire_page.link_newhire_btn()
    newhire_page.first_name().fill(first_name)
    newhire_page.middle_name().fill(middle_name)
    newhire_page.last_name().fill(last_name)
    newhire_page.nick_name().fill(first_name)





    newhire_page.page_pause()

