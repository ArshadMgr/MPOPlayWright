import pytest
import openpyxl
from playwright.sync_api import sync_playwright

# Path to the Excel file
excel_file_path = "C:/Users/Arshad Mehmood/OneDrive - Riphah International University/Desktop/ArshadMgr/RIO_Test_Automation/Payload/testData/SignUp.xlsx"

# Pytest fixture to initialize and provide the browser and page
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

# Function to read test data from the Excel file
def get_test_data(sheet_name, cell_reference):
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook[sheet_name]
    data = sheet[cell_reference].value
    workbook.close()
    return data

# Fetch test data from the Excel file
first_name = get_test_data("SignupInfo", "A2")
last_name = get_test_data("SignupInfo", "B2")
email=get_test_data("SignupInfo", "C2")




# Test case for signup functionality
def test_signup(browser):
    # Navigate to the signup page
    browser.goto("https://utest.com/signup/personal")

    # Perform actions on the page
    browser.fill("input[id='firstName']", first_name)
    browser.fill("input[id='lastName']", last_name)
    browser.fill("input[id='email']", email)



    browser.pause()


