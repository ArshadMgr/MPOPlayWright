from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser


def test_setup(browser):
    page = browser.new_page()
    page.goto('https://mypaperlessoffice.com/app/login.aspx')

    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("CharlesCR")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("Aspire321#")
    page.get_by_role("link", name=" Sign In").click()
    page.get_by_label("Employee").click()
    page.get_by_role("searchbox").fill("Employer")
    page.get_by_role("option", name="Employer").click()
    page.get_by_role("link", name="Go").click()
    assert page.title() == "Sign In"