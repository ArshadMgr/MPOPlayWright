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
import logging
import pytest
from cryptography.fernet import Fernet
from Payload.security import generate_key, save_credentials_to_file, encrypt_message, load_credentials_from_file
from  Payload.data_validation import validate_username, validate_email, validate_age
from Payload.ai_validation_helper import validate_with_openai
from utils.config import CredentilasPath_A
from utils.config import CredentilasPath_H
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
    key, encrypted_password = mpologin.load_credentials_from_file(CredentilasPath_A)

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

    # code by Haseeb
    newhire_page.user_name().fill(user_name)
    newhire_page.date_of_birth().fill('9/9/1998')
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
    newhire_page.employee_id().fill("143")
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
    # togel button seasonal skip
    newhire_page.hiring_date().fill('7/25/2024')
    newhire_page.job_title().click()
    newhire_page.select_job_title().fill('SQA')
    newhire_page.enter_job_title().press('Enter')
    newhire_page.tier_title().click()
    newhire_page.select_tier_title().fill('2')
    newhire_page.enter_tier_title().press('Enter')
    # work's comp not found
    # newhire_page.eeo_title().click()
    # newhire_page.select_eeo_title().fill('craft')
    # newhire_page.enter_eeo_title().press('Enter')
    newhire_page.department_title().click()
    newhire_page.select_department_title().fill('dev')
    newhire_page.enter_department_title().press('Enter')
    newhire_page.location_title().click()
    newhire_page.select_location_title().fill('wl')
    newhire_page.enter_location_title().press('Enter')
    # desigantion not found
    # sub desigantion not found
    # country not found
    # level not found
    newhire_page.primary_location_title().click()
    newhire_page.select_primary_location_title().fill('ny')
    newhire_page.enter_primary_location_title().press('Enter')
    newhire_page.time_enter_title().click()
    newhire_page.select_time_enter_title().fill('manual')
    newhire_page.enter_time_enter_title().press('Enter')
    # newhire_page.enable_punching().click() locator not found
    # newhire_page.bypass_onboarding().click() locator not found
    # newhire_page.independent_contractor().click() locator not found

    # pay rate information
    newhire_page.pay_schedule().click()
    newhire_page.select_pay_schedule().fill('month')
    newhire_page.enter_pay_schedule().press('Enter')
    newhire_page.pay_type().click()
    newhire_page.select_pay_type().fill('salary')
    newhire_page.enter_pay_type().press('Enter')
    newhire_page.annual_salary().fill('5000')
    newhire_page.default_hour().fill('50')

    # Federal Tax Information
    newhire_page.filling_status().click()
    newhire_page.select_filling_status().fill('unknown')
    newhire_page.enter_filling_status().press('Enter')
    # mutiple job toggle button
    newhire_page.w4_submitted().fill('7/1/2023')
    newhire_page.claim_dependents_amount().fill('150')
    newhire_page.deduction().fill('100')
    newhire_page.other_income().fill('200')
    newhire_page.extra_withholding().fill('0')

    newhire_page.add_new_hire_button().click()



    newhire_page.page_pause()

