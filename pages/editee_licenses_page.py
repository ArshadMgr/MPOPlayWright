import pytest
from playwright.sync_api import Page
from .base_page import BasePage
from faker import Faker
from MPOPlayWright.utils.logger import setup_logger
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

class EditEElicenses(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def ee_select(self):
        return self.page.get_by_role('link', name="Abraham, Joseph1 m")

    #Manage License Types

    def select_licenses_type(self):
        return self.page.get_by_role('link', name=" Manage License Types")

    def add_licenses_type(self):
        return self.page.get_by_role('link', name="+ Add License Type")

    def licenses_type(self):
        return self.page.get_by_label("License Type:")

    def licenses_description(self):
        return self.page.get_by_label("License Description:")

    def save(self):
        return self.page.get_by_text("Save")

    # Add Licenses
    def select_licenses(self):
        return self.page.get_by_role('link', name="License Tracking ")

    def add_licenses(self):
        return self.page.get_by_role('link', name="+ Add License")

    def enter_title(self):
        return self.page.get_by_label("Title:")

    def select_type(self):
        return self.page.get_by_title("Select")

    def fill_type(self):
        return self.page.locator('input[type="search"]')

    def enter_type(self):
        return self.page.locator('input[type="search"]')

    def issued_by(self):
        return self.page.get_by_label("Issued By:")

    def licenses_number(self):
        return self.page.get_by_label("License Number:")

    def issued_date(self):
        return self.page.get_by_label('Issued Date:')

    def notes(self):
        return self.page.get_by_label('Notes:')

    def press_save(self):
        return self.page.locator("//a[@id='Body_Body_btnSave']")

    def edit_licenses(self):
        return self.page.get_by_role('link', name="").nth(0)

    def delete_licenses(self):
        return self.page.get_by_role('link', name="").nth(0)

    def delete_yes(self):
        return self.page.get_by_text('Yes')

    # Request Licenses

    def request_license(self):
        return self.page.get_by_role('link', name="+ Request License")

    def title(self):
        return self.page.locator('#Body_Body_tbRequestTitle')

    def license_type(self):
        return self.page.get_by_title('Select')

    def add_type(self):
        return self.page.locator('input[type="search"]')

    def enter_lictype(self):
        return self.page.locator('input[type="search"]')

    def save_req(self):
        return self.page.locator('#Body_Body_btnRequestLicenseSave')

    def edit_request_license(self):
        return self.page.get_by_role('link', name="")

    def delete_request_license(self):
        return self.page.get_by_role('link', name="").nth(0)

    def delete_licensetype(self):
        return self.page.get_by_role('link', name="").nth(0)

