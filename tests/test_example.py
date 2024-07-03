import time

import pytest
from MPOPlayWright.Payload.ai_helper import generate_test_input
from MPOPlayWright.utils.logger import setup_logger
import logging


logger = setup_logger()
# Setup logger
logger = logging.getLogger("TestLogger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def test_dynamic_input(page):
    retry_count = 3
    for i in range(retry_count):
        try:
            page.goto("https://mypaperlessoffice.com/app/login.aspx")
            break
        except Exception as e:
            print(f"Attempt {i + 1} failed: {e}")
            time.sleep(2)  # wait before retrying
    else:
        raise Exception("Failed to navigate to the URL after multiple attempts")


    username_prompt = "Generate a realistic username for testing login functionality."
    username = generate_test_input(username_prompt)

    password_prompt = "Generate a realistic password for testing login functionality."
    password = generate_test_input(password_prompt)

    page.get_by_label("Username:").fill(username)
    page.get_by_label("Password:").fill(password)

    logger.info(f"AI Model Response: "
                f": User Name->: {username} ")
    logger.info(f"AI Model Response: "
                f": Password->: {password} ")

    page.get_by_role("link", name=" Sign In").click()

    page.pause()
