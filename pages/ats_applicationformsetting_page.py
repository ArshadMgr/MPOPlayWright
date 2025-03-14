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

class ApplicationFormSetting(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def add_form(self):
        return self.page.get_by_role('link', name="+ Add Form")

    def form_name(self):
        return self.page.get_by_label('Manage Application Form').get_by_label('Form Name:')

    def save(self):
        return self.page.get_by_label('Manage Application Form').get_by_text('Save')

    def add_new_field(self):
        return self.page.get_by_role('link', name='+ Add New Field')

    def field_name(self):
        return self.page.get_by_label("Field Name:")

    def save_field(self):
        return self.page.get_by_text('Save', exact= True)

    def save_order(self):
        return self.page.get_by_role('link', name=' Save Sort Order')

    def cancel(self):
        return self.page.get_by_role('link', name= 'Cancel')

    def active(self):
        return self.page.get_by_role('link', name='Inactive').nth(0)

    def delete(self):
        return self.page.get_by_role('row', name='Testing the field 0 3/12/2025').get_by_role('link').nth(4)

    def yes(self):
        return self.page.get_by_text('Yes')
