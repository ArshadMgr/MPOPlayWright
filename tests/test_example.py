import pytest
from MPOPlayWright.Payload.ai_helper import generate_test_input
def test_dynamic_input(page):
    page.goto("https://mypaperlessoffice.com/app/login.aspx")

    username_prompt = "Generate a realistic username for testing login functionality."
    username = generate_test_input(username_prompt)

    password_prompt = "Generate a realistic password for testing login functionality."
    password = generate_test_input(password_prompt)

    page.fill("input[name='username']", username)
    page.fill("input[name='password']", password)

    page.click("button[type='submit']")


    page.page_pause()
