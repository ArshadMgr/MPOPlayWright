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


class EditBeneficiaries(BasePage):

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

    def select_beneficiaries(self):
        return self.page.get_by_role('link', name="Beneficiaries ")

    def add_beneficiaries(self):
        return self.page.get_by_role('link', name="+ Add Beneficiary")

    def addfirst_name(self):
        return self.page.get_by_placeholder("First Name")

    def addlast_name(self):
        return self.page.get_by_placeholder("Last Name")

    def gender_select(self):
        return self.page.get_by_text('Gender: Select Female Male')

    def gender_type(self):
         return self.page.locator('input[type="search"]')

    def gender_enter(self):
        return self.page.locator('input[type="search"]')

    def relation_select(self):
        return self.page.get_by_text('Relationship: Select Aunt')

    def relation_type(self):
        return self.page.locator('input[type="search"]')

    def relation_enter(self):
        return self.page.locator('input[type="search"]')

    def ssn_enter(self):
        return self.page.get_by_label('SSN:')

    def date_enter(self):
        return self.page.get_by_placeholder('MM/DD/YYYY')

    def address_enter(self):
        return self.page.get_by_placeholder('Address')

    def city_name(self):
        return self.page.get_by_placeholder('City')

    def press_save(self):
        return self.page.get_by_text('Save')

     # edit sections starts from here

    def edit_button(self):
        return self.page.locator('#Body_Body_gvEmployeeBeneficiaries_btnEdit_0')

    def delete_beneficiaries(self):
        return self.page.locator('#Body_Body_gvEmployeeBeneficiaries_btnDelete_0')

    def enter_yes(self):
        return self.page.get_by_text('Yes')
