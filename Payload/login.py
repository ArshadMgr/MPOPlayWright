from playwright.sync_api import sync_playwright

from MPOPlayWright.pages.login_page import LoginPage
from MPOPlayWright.utils.config import USERNAME, BASE_URL
from MPOPlayWright.utils.logger import setup_logger
import logging
import pytest
from cryptography.fernet import Fernet
logger = setup_logger()
# Setup logger
logger = logging.getLogger("TestLogger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class Login:

    @pytest.fixture(scope="session")
    def browser(self):
        with sync_playwright() as p:
         browser = p.chromium.launch(headless=False)
         yield browser


    def decrypt_message(self, encrypted_message: str, key: bytes) -> str:
        """Decrypt a message."""
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message.encode())
        return decrypted_message.decode()


    def load_credentials_from_file(self, filename: str) -> tuple:
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

            return key, encrypted_password

    #testing new function

    def erlogin_setup(self, browser):

        key, encrypted_password = self.load_credentials_from_file("credentials.txt")

        decrypted_password = self.decrypt_message(encrypted_password, key)



        logger.info("Setting up the test environment(Demo)")
        page = browser.new_page()
        login_page = LoginPage(page)
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

