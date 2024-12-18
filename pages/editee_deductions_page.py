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


class EditEEDeductions(BasePage):

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

    def select_deductions(self):
        return self.page.get_by_role('link', name="Deductions ")

    def add_deductions(self):
        return self.page.get_by_role('link', name='+ Add Deduction')

    def select_code(self):
        return self.page.locator("#select2-Body_Body_ddlDeductionCode-container")

    def code_type(self):
        return self.page.locator('input[type="search"]')

    def code_enter(self):
        return self.page.locator('input[type="search"]')

    def deduction_amount(self):
        return self.page.get_by_label('Deduction Amount:')

    def effective_date(self):
        return self.page.locator("//input[@id='Body_Body_dtEffectiveDate']")

    def select_status(self):
        return self.page.locator('#select2-Body_Body_ddlDeductionStatus-container')

    def type_status(self):
        return self.page.locator('input[type="search"]')

    def enter_status(self):
        return self.page.locator('input[type="search"]')

    def press_save(self):
        return self.page.get_by_text('Save')
        # Edit

    def edit_deductions(self):
        return self.page.get_by_role('link', name='')
