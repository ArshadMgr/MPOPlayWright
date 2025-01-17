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

class Hr360DegreeFeedback(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def add_360_degree_feedback(self):
        return self.page.get_by_role('link', name="+ Add 360 Degree Feedback")

    def session(self):
        return self.page.get_by_title('Select')

    def type_session(self):
        return self.page.locator('input[type="search"]')

    def enter_session(self):
        return self.page.locator('input[type="search"]')

    def employee(self):
        return self.page.get_by_title('Select')

    def type_employee(self):
        return self.page.locator('input[type="search"]')

    def enter_employee(self):
        return self.page.locator('input[type="search"]')

    def reviewer(self):
        return self.page.get_by_title('None')

    def select_reviewer(self):
        return self.page.get_by_label('Alicia Freeland (454444)')

    def click_reviewer(self):
        return self.page.get_by_title('Alicia Freeland (454444)')

    def save(self):
        return self.page.get_by_text('Save')

#delet
    def delete(self):
        return self.page.get_by_role('row', name='ARF T California QA Alicia').get_by_role('link').nth(1)

    def yes(self):
        return self.page.locator('button').filter(has_text='Yes')
