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

class HrReviewWorkflow(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def add_workflow(self):
        return self.page.get_by_role('link', name="+ Add Workflow")

    def workflow_name(self):
        return self.page.get_by_label('Workflow Name:')

    def add_step(self):
        return self.page.get_by_role('link', name="+ Add Step")

    def user_type(self):
        return self.page.get_by_title('Select')

    def type_user_type(self):
        return self.page.locator('input[type="search"]')

    def enter_user_type(self):
        return self.page.locator('input[type="search"]')

    def description(self):
        return self.page.get_by_label('Description:')

    def save_step(self):
        return self.page.get_by_label('Add Workflow Step').get_by_text('Save')

    def save(self):
        return self.page.get_by_role('link', name="Save")

    # delete
    def delete(self):
        return self.page.get_by_role('row', name='test name No   CharlesCR (').get_by_role('link').nth(1)

    def yes(self):
        return self.page.locator('button').filter(has_text='Yes')





