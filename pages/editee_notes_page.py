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

class EditEENotes(BasePage):

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

    def select_notes(self):
        return self.page.get_by_role('link', name="Notes ")

    def add_notes(self):
        return self.page.get_by_role('link', name="+ Add Notes")

    def add_title(self):
        return self.page.get_by_label('Title:')

    def add_category(self):
        return self.page.get_by_title('Select')

    def type_category(self):
        return self.page.locator('input[type="search"]')

    def enter_category(self):
        return self.page.locator('input[type="search"]')

    def note(self):
        return self.page.get_by_label('Notes:')

    def save(self):
        return self.page.get_by_text('Save')

    def manage_cateogry(self):
        return self.page.get_by_role('link', name="+ Manage Categories")

    def add_cateogry(self):
        return self.page.get_by_role('link', name="+ Add Category")

    def code(self):
        return self.page.get_by_label('Code:')

    def description(self):
        return self.page.get_by_label('Description:')

    def edit_note(self):
        return self.page.get_by_role('link', name="").nth(0)

    def delete_note(self):
        return self.page.get_by_role('link', name="").nth(0)

    def yes(self):
        return self.page.get_by_text("Yes")

    def delete_category(self):
        return self.page.locator("//tbody/tr[1]/td[4]/a[2]/span[1]").nth(0)

