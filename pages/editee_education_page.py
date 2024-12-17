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


class EditEEEducation(BasePage):

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

    def select_education(self):
        return self.page.get_by_role('link',name= 'Education ' )

    def add_education(self):
        return self.page.get_by_role('link',name= '+ Add Education' )

    def select_schooltype(self):
        return self.page.locator('#select2-Body_Body_ddlSchoolType-container')

    def type_education(self):
        return self.page.locator('input[type="search"]')

    def enter_education(self):
        return self.page.locator('input[type="search"]')

    def school_major(self):
        return self.page.get_by_label('School Major:')

    def school_name(self):
        return self.page.get_by_label('School Name:')

    def start_date(self):
        return self.page.get_by_label('Start Date:')

    def end_date(self):
        return self.page.get_by_label('Graduation Date:')

    def gpa(self):
        return self.page.locator('#Body_Body_tbGPA')

    def contact_name(self):
        return self.page.get_by_label('Contact Name:')

    def address(self):
        return self.page.get_by_label('Address 1:')

    def phone(self):
        return self.page.get_by_label('Phone:')

    def edit_education(self):
        return self.page.get_by_role('link',  name= '').nth(0)

    def press_save(self):
        return self.page.get_by_text('Save')

    def delete_education(self):
        return self.page.get_by_role('link',  name='').nth(0)

    def enter_yes(self):
        return self.page.get_by_text('Yes')


