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

class ApplicantStatusSettings(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def add_stage(self):
        return self.page.get_by_role('link', name="+ Add New Stage")

    def select_job_title(self):
        return self.page.locator("#select2-Body_ddlJobPostings-container")

    def enter_job_title(self):
        return self.page.locator("input[type='search']")

    def enter_stage(self):
        return self.page.get_by_label('Manage Applicant Stage').get_by_title('Select')

    def enter_stage_title(self):
        return self.page.locator('input[type="search"]')

    def save(self):
        return self.page.get_by_label('Manage Applicant Stage').get_by_text('Save')

    def delete(self):
        return self.page.get_by_role("row", name="SQA ABC Test Company ABC Test").get_by_role("link")

    def yes(self):
        return self.page.get_by_text("Yes")