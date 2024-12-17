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

class EditEEtimeoff(BasePage):

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

    def select_timeoff(self):
        return self.page.get_by_role('link', name="Time Off ")

    def add_timeoff(self):
        return self.page.get_by_role('link', name="+ Add Time Off Policy")

    def add_timeoff_code(self):
        return self.page.get_by_label('', exact=True)

    def type_timeoff_code(self):
        return self.page.locator('input[type="search"]')

    def enter_timeoff_code(self):
        return self.page.locator('input[type="search"]')

    def available_hours(self):
        return self.page.get_by_label('Available Hours:')

    def used_hours(self):
        return self.page.get_by_label('Used Hours:')

    def start_date(self):
        return self.page.get_by_label('Start Date:')

    def end_date(self):
        return self.page.get_by_label('End Date:')

    def save(self):
        return self.page.get_by_text('Save')

    def edit_timeoff(self):
        return self.page.get_by_role('link', name="").nth(0)

    def delete_timeoff(self):
        return self.page.get_by_role('link', name="").nth(0)

    def yes(self):
        return self.page.get_by_text('Yes')
