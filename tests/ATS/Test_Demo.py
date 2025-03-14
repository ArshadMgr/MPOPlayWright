import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True to run headless
        yield browser
        browser.close()


def test_visit_google(browser):
    context = browser.new_context()
    page = context.new_page()

    # Navigate to Google
    page.goto("https://www.google.com")

    if "Google" not in page.title():
        page.screenshot(path="google_homepage.png")
        assert False, "Title does not contain 'Google'"

    context.close()
