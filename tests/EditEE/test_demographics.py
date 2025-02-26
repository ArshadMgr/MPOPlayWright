from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from faker import Faker
import os

from Payload.login import Login
from Payload.new_hire import NewHire
import pytest
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from pages import login_page, newhire_page
from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from pages.newhire_page import NewHirePage
from utils.logger import setup_logger
import time
import logging
from utils.config import CredentilasPath_A
from utils.config import CredentilasPath_H
import logging
import pytest
from cryptography.fernet import Fernet
from Payload.security import generate_key, save_credentials_to_file, encrypt_message, load_credentials_from_file
from  Payload.data_validation import validate_username, validate_email, validate_age
from Payload.ai_validation_helper import validate_with_openai

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
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_H)

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
    date_of_birth = fake_data.date_of_birth()
    ssn = fake_data.ssn()
    personal_email = fake_data.email()
    work_email = fake_data.company_email()
    gender = fake_data.passport_gender()
    # employee_id = fake_data.()
    country_name = fake_data.country()
    phone_number = fake_data.phone_number()
    address = fake_data.address()
    city = fake_data.city()
    zip_code = fake_data.zipcode()
    assert validate_username(user_name)
    #assert validate_with_openai("username", user_name), f"Invalid username: {user_name}"

    logger.info(f"Generated fake: "
                f": first name->: {first_name} "
                f": Middle Name->: {middle_name}"
                f": Last Name->: {last_name}"
                f": User Name->:{user_name}"
                f": date of birth->:{date_of_birth}"
                f": ssn->:{ssn}"
                f": gender->:{gender}"
                f": personal email->:{personal_email}"
                f": work email->:{work_email}"
                # f": employee id->:{employee_id}"
                f": country name->:{country_name}"
                f": phone number->:{phone_number}"
                f": address->:{address}"
                f": city->:{city}"
                f": zip code->:{zip_code}")


    newhire_page.navigate(BASE_URL + '/Sys/EmployerManager/Employees/EditEmployees.aspx')
    try:
        assert newhire_page.verify_page_title("Edit Employees")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError_NewHire.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    newhire_page.ee_select().click()
    newhire_page.select_demogrpahics().click()

    newhire_page.date_of_birth().fill('9/9/1999')
    newhire_page.ssn().type(ssn)
    newhire_page.gender_field().click()
    newhire_page.select_gender().fill(gender)
    newhire_page.enter_gender().press('Enter')
    newhire_page.ethnicity_field().click()
    newhire_page.select_ethnicity().fill('asian')
    newhire_page.enter_ethnicity().press('Enter')
    newhire_page.marital_status().click()
    newhire_page.select_marital_status().fill('married')
    newhire_page.enter_marital_status().press('Enter')
    newhire_page.veteran_field().click()
    newhire_page.select_veteran_field().fill('yes')
    newhire_page.enter_veteran_field().press('Enter')
    newhire_page.employee_id().fill("1433")
    # newhire_page.employee_payroll_id().type(employee_id)

    # Contact Information

    newhire_page.select_email().click()
    newhire_page.select_email_status().fill('email')
    newhire_page.enter_email_status().press('Enter')
    newhire_page.work_email().fill(work_email)
    newhire_page.personal_email().fill(personal_email)
    newhire_page.home_phone().fill(phone_number)
    newhire_page.work_phone().fill(phone_number)
    newhire_page.cell_phone().fill(phone_number)
    newhire_page.select_country().click()
    newhire_page.enter_country_name().fill(country_name)
    newhire_page.press_enter().press('Enter')

    newhire_page.address_street().fill(address)
    newhire_page.address_2().fill(address)
    newhire_page.city().fill(city)
    # state drop down will be select with the city.
    # newhire_page.state().click()
    # newhire_page.select_state().fill('alaska')
    # newhire_page.select_state().press('Enter')
    newhire_page.zip_code().fill(zip_code)
    # newhire_page.mailing_address().click()
    # Status/ information
    newhire_page.user_group().click()
    newhire_page.select_user_group().fill('system')
    newhire_page.enter_user_group().press('Enter')
    newhire_page.employee_status().click()
    newhire_page.select_employee_status().fill('active')
    newhire_page.enter_employee_status().press('Enter')
    newhire_page.employee_type().click()
    newhire_page.select_employee_type().fill('full')
    newhire_page.enter_employee_type().press('Enter')
    newhire_page.hiring_date().fill('7/25/2024')

    newhire_page.save().click()





    newhire_page.page_pause()

