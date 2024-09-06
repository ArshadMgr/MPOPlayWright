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


class EditEEDependents(BasePage):

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

    def select_dependents(self):
        return self.page.get_by_role('link',name= 'Dependents ')

    def add_dependents(self):
        return self.page.get_by_role('link',name= '+ Add Dependent')

    def first_enter(self):
        return self.page.get_by_placeholder('First Name')

    def last_enter(self):
        return self.page.get_by_placeholder('Last Name')

    def gender_status(self):
        return self.page.get_by_text('Gender: Select Female Male')

    def gender_typ(self):
        return self.page.locator('input[type="search"]')

    def gender_ente(self):
        return self.page.locator('input[type="search"]')

    def relation_status(self):
        return self.page.get_by_text('Relationship: Select Child (')

    def relation_typ(self):
        return self.page.locator('input[type="search"]')

    def relation_ente(self):
        return self.page.locator('input[type="search"]')

    def ssn_ente(self):
        return self.page.get_by_label('SSN:')

    def dob_ente(self):
        return self.page.get_by_placeholder('MM/DD/YYYY')

    #Edit

    def edit_dependents(self):
        return self.page.locator('#Body_Body_gvDependents_btnEdit_5')

    def press_save(self):
        return self.page.get_by_text('Save')