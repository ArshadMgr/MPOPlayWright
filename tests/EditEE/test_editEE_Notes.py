from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from faker import Faker
import os
from pytest_check import check
from Payload.login import Login
import pytest
from Payload.soft_assertion_helper import SoftAssertContext
from Payload import new_hire
from pages import login_page, editee_notes_page
from utils.config import BASE_URL
from utils.config import USERNAME
from pages.login_page import LoginPage
from pages.editee_notes_page import EditEENotes
from utils.logger import setup_logger
import time
import logging
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
    key, encrypted_password = mpologin.load_credentials_from_file("credentials.txt")

    decrypted_password = mpologin.decrypt_message(encrypted_password, key)


    logger.info("Setting up the test environment(New Hire)")
    page = browser.new_page()
    login_page = LoginPage(page)
    editee_Notes = EditEENotes(page)
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
    digit = fake_data.random_digit()
    note = fake_data.paragraph()
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
                f": digit->:{digit}"
                f": zip code->:{zip_code}"
                f": note->:{note}")

    editee_Notes.navigate(BASE_URL + '/Sys/EmployerManager/Employees/EditEmployees.aspx')
    try:
        assert editee_Notes.verify_page_title("Edit Employees")
    except AssertionError:
        # Capture a screenshot on assertion failure
        page.screenshot(path=os.path.join("../screenshots", "AssertionError_NewHire.jpg"))
        raise  # Re-raise the AssertionError to mark the test as failed

    editee_Notes.ee_select().click()
    editee_Notes.select_notes().click()

    #manage category
    editee_Notes.manage_cateogry().click()
    editee_Notes.add_cateogry().click()
    editee_Notes.code().fill("Meeting 3")
    editee_Notes.description().fill("For Testing")
    editee_Notes.save().click()
    page.goto("https://mypaperlessoffice.com/app/Sys/EmployerManager/Employees/EmployeeNotes")

    #Add Notes
    editee_Notes.add_notes().click()
    editee_Notes.add_title().fill("Test Notes")
    editee_Notes.add_category().click()
    editee_Notes.type_category().fill("Meeting 3")
    editee_Notes.enter_category().press("Enter")
    editee_Notes.note().fill(note)
    editee_Notes.save().click()

#Edit
    editee_Notes.edit_note().click()
    editee_Notes.add_title().fill("Test")
    editee_Notes.save().click()

    #Delete
    editee_Notes.delete_note().click()
    editee_Notes.yes().click()

    #Delete Category
    editee_Notes.manage_cateogry().click()
    editee_Notes.delete_category().click()
    editee_Notes.yes().click()
    page.goto("https://mypaperlessoffice.com/app/Sys/EmployerManager/Employees/EmployeeNotes")

    editee_Notes.page_pause()


