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


class EditEEDirectdeposit(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def ee_select(self):
        return self.page.get_by_role('link', name="Abraham, Joseph a")

    def select_directdeposit(self):
        return self.page.get_by_role('link',name= 'Direct Deposit ')

    def add_directdeposit(self):
        return self.page.get_by_role('link',name= '+ Add Direct Deposit')

    def select_account(self):
        return self.page.locator('#select2-Body_Body_ddlAccountType-container')

    def account_typ(self):
        return self.page.locator('input[type="search"]')

    def account_ente(self):
        return self.page.locator('input[type="search"]')

    def priority_enter(self):
        return self.page.get_by_label('Priority:')

    def bank_name(self):
        return self.page.get_by_label('Bank Name:')

    def branch_city(self):
        return self.page.get_by_label('Branch City:')

    def account_name(self):
        return self.page.get_by_label('Account Name:')

    def account_aba_number(self):
        return self.page.get_by_label('ABA Routing Number:')

    def account_number(self):
        return self.page.get_by_label('Account Number:')

    def select_amount_type(self):
        return self.page.locator('#select2-Body_Body_ddlAmountType-container')

    def type_amount_type(self):
        return self.page.locator('input[type="search"]')

    def enter_amount_type(self):
        return self.page.locator('input[type="search"]')

    def enter_amount(self):
        return self.page.get_by_label('Amount:')

    #Edit
    def edit_directdeospit(self):
        return self.page.locator('#Body_Body_gvDDeposit_btnEdit_0')

    def press_save(self):
        return self.page.get_by_text('Save')