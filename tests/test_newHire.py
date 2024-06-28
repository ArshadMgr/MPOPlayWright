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
from MPOPlayWright.pages.newhire_page import NewHirePage
from MPOPlayWright.utils.logger import setup_logger
import time
import logging
import pytest
from cryptography.fernet import Fernet
from MPOPlayWright.Payload.security import generate_key, save_credentials_to_file, encrypt_message, load_credentials_from_file



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


def decrypt_message(encrypted_message: str, key: bytes) -> str:
    """Decrypt a message."""
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    return decrypted_message.decode()


def load_credentials_from_file(filename: str) -> tuple:
    """Load the encryption key and encrypted credentials from a file."""
    with open(filename, 'r') as file:
        key_line = file.readline().strip()
        encrypted_base_url_line = file.readline().strip()
        encrypted_username_line = file.readline().strip()
        encrypted_password_line = file.readline().strip()

    # Extract key and encrypted values
    key = key_line.split("Key: ")[1].encode()
    encrypted_base_url = encrypted_base_url_line.split("BaseURL: ")[1]
    encrypted_username = encrypted_username_line.split("Username: ")[1]
    encrypted_password = encrypted_password_line.split("Password: ")[1]

    return key, encrypted_base_url, encrypted_username, encrypted_password


def test_encryption_decryption_with_file():
    # Load key and encrypted data from file
    key, encrypted_base_url, encrypted_username, encrypted_password = load_credentials_from_file("credentials.txt")

    # Decrypt data
    decrypted_base_url = decrypt_message(encrypted_base_url, key)
    decrypted_username = decrypt_message(encrypted_username, key)
    decrypted_password = decrypt_message(encrypted_password, key)


    # Assertions
    assert BASE_URL == decrypted_base_url
    assert USERNAME == decrypted_username
    assert PASSWORD == decrypted_password
    logger.info(f"Assertions: "
                f": Decripted BaseURL->: {decrypted_base_url} ")
    logger.info(f"Assertions: "
                f": Decripted UserName->: {decrypted_username} ")




def test_newhire_Setup(browser, fake_data):
    logger.info("Setting up the test environment(New Hire)")
    page = browser.new_page()
    login_page = LoginPage(page)
    newhire_page = NewHirePage(page)
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

    # Generate fake data
    first_name = fake_data.first_name_female()
    middle_name = fake_data.first_name_female()
    last_name = fake_data.last_name_female()
    user_name = fake_data.user_name()

    logger.info(f"Generated fake: "
                f": first name->: {first_name} "
                f": Middle Name->: {middle_name}"
                f": Last Name->: {last_name}"
                f": User Name->:{user_name}")

    logger.info("Starting test: test_Demographics Section")
    login_page.navigate(BASE_URL + "/Sys/EmployerManager/Employees/NewHireReport.aspx")
    assert newhire_page.verify_page_title("New Hire Report")
    newhire_page.navigate(BASE_URL + '/Sys/EmployerManager/Employees/NewHire.aspx')
    newhire_page.link_newhire_btn()
    newhire_page.first_name().fill(first_name)
    newhire_page.middle_name().fill(middle_name)
    newhire_page.last_name().fill(last_name)
    newhire_page.nick_name().fill(first_name)







    newhire_page.page_pause()

