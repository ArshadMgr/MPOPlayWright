import os
import time

import pytest
from playwright.sync_api import sync_playwright

from Payload.ai_helper import generate_test_input
from Payload.ai_validation_helper import validate_with_openai

from utils.logger import setup_logger
import logging


logger = setup_logger()
# Setup logger
logger = logging.getLogger("TestLogger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def test_dynamic_input():

    username_prompt = "Generate a realistic username for testing login functionality."
    username = generate_test_input(username_prompt)

    password_prompt = "Generate a realistic password for testing login functionality."
    password = generate_test_input(password_prompt)


    logger.info(f"AI Model Response: "
                f": User Name->: {username} ")
    logger.info(f"AI Model Response: "
                f": Password->: {password} ")

    assert validate_with_openai("username", username), f"Invalid username: {username}"
    assert validate_with_openai("password", password), f"Invalid username: {password}"








