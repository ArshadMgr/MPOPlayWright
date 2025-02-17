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

class EmployeeWarning(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")


    #manage reason Sections
    def manage_reason(self):
        return self.page.get_by_role('link', name="Manage Reasons")

    def add_reason(self):
        return self.page.get_by_role('link', name="+ Add Reason")

    def reason(self):
        return self.page.get_by_label('Reason:')

    def reason_description(self):
        return self.page.get_by_label('Reason Description:')

    def save(self):
        return self.page.get_by_text('Save')

     #manage Category Sections
    def manage_category(self):
        return self.page.get_by_role('link', name='+ Manage Categories')

    def add_category(self):
        return self.page.get_by_role('link', name='+ Add Category')

    def category(self):
        return self.page.get_by_label('Category:')

    def category_description(self):
        return self.page.get_by_label('Category Description:')

    #Add Warning Sections
    def add_warning(self):
        return self.page.get_by_role('link', name='+ Add Warning')

    def add_employee(self):
        return self.page.locator("#select2-Body_ddlEmployee-container")

    def type_employee(self):
        return self.page.get_by_role('searchbox')

    def enter_employee(self):
        return self.page.get_by_role('searchbox')

    def add_categoryy(self):
        return self.page.locator("#select2-Body_ddlCategory-container")

    def type_categoryy(self):
        return self.page.get_by_role('searchbox')

    def enter_categoryy(self):
        return self.page.get_by_role('searchbox')

    def add_reasons(self):
        return self.page.get_by_label('Select')

    def type_reasons(self):
        return self.page.get_by_role('searchbox')

    def enter_reasons(self):
        return self.page.get_by_role('searchbox')

    def incident_date(self):
        return self.page.get_by_placeholder("Incident Date")

    def incident_description(self):
        return self.page.get_by_label('Incident Description:')

    def save_change(self):
        return self.page.get_by_role('link', name="Submit")

    # Delete Warning Sections
    def delete(self):
        return self.page.get_by_role('row', name='Amy Neal QAupdated').get_by_role('link').nth(1)

    def yes(self):
        return self.page.get_by_text("Yes")

    # Delete Category Sections
    def category_delete(self):
        return self.page.get_by_role('row', name='').get_by_role('link').nth(1)

    # Delete reason Sections
    def reason_delete(self):
        return self.page.get_by_role('row', name='Test Reason Testing the').get_by_role('link').nth(1)
