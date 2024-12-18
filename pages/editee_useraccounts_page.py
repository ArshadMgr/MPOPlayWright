import pytest
from playwright.sync_api import Page
from .base_page import BasePage
from faker import Faker
from utils.logger import setup_logger
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

class EditEEUserAccount(BasePage):

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

    def select_useraccount(self):
        return self.page.get_by_role('link', name="User Accounts ")

    def select_manage_user(self):
        return self.page.get_by_role('link', name=" Manage User Account Types")

    def add_accounttype(self):
        return self.page.get_by_role('link', name="+ Add Account Type")

    def account_type(self):
        return self.page.get_by_label("Account Type:")

    def description(self):
        return self.page.get_by_label("Account Description:")

    def save(self):
        return self.page.get_by_text("Save")

    def add_account(self):
        return self.page.get_by_role('link', name="+ Add User Account")

    def add_account_type(self):
        return self.page.get_by_title("Select")

    def type_account_type(self):
        return self.page.locator('input[type="search"]')

    def enter_account_type(self):
        return self.page.locator('input[type="search"]')

    def username(self):
        return self.page.get_by_label("Username:")

    def URL(self):
        return self.page.get_by_label("Account URL:")

    def notes(self):
        return self.page.get_by_label("Notes:")

    def edit_account(self):
        return self.page.get_by_role('link', name="").nth(0)

    def delete_account(self):
        return self.page.get_by_role('link', name="").nth(0)

    def yes(self):
        return self.page.get_by_text("Yes")