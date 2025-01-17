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

class HrPerformanceJournal(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def add_note(self):
        return self.page.get_by_role('link', name="+ Add Note")

    def employee(self):
        return self.page.locator('#select2-Body_ddlEmployee-container')

    def add_employee(self):
        return self.page.locator('input[type="search"]')

    def enter_employee(self):
        return self.page.locator('input[type="search"]')

    def note_type(self):
        return self.page.get_by_title('Select')

    def note(self):
        return self.page.locator('input[type="search"]')

    def enter_note(self):
        return self.page.locator('input[type="search"]')

    def title(self):
        return self.page.get_by_label('Title:')

    def save(self):
        return self.page.get_by_text('Save')

#delete
    def delete(self):
        return self.page.get_by_role('row', name='Neal Amy 3265656 Testing').get_by_role('link').nth(1)

    def yes(self):
        return self.page.get_by_text('Yes')