import time

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True to run headless
        yield browser
        browser.close()


def test_rahulshettyacademy(browser):
    context = browser.new_context()
    page = context.new_page()

    # Navigate to website
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator('//input[@id="username"]').fill("rahulshettyacademy");
    time.sleep(2)
    page.locator('//input[@id="password"]').fill("learning");
    time.sleep(2)
    page.locator('//input[@id="signInBtn"]').click();

    #context.close()
    page.pause()