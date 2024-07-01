from cryptography.fernet import Fernet
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from faker import Faker
from MPOPlayWright.Payload.new_hire import NewHire

import pytest
from MPOPlayWright.Payload import new_hire
from MPOPlayWright.utils.config import BASE_URL
from MPOPlayWright.utils.config import USERNAME
from MPOPlayWright.Payload.security import generate_key, save_credentials_to_file, encrypt_message, load_credentials_from_file
from MPOPlayWright.pages.login_page import LoginPage
from MPOPlayWright.utils.logger import setup_logger
from MPOPlayWright.Payload.login import Login
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


def test_setup(browser):

    mpologin = Login()
    mpologin.erlogin_setup(browser)



