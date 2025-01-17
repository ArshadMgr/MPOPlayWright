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

class HrPerformanceReview(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def add_review_form(self):
        return self.page.get_by_role('link', name="+ Add Review Form")

    def name(self):
        return self.page.get_by_label('Name:')

    def description(self):
        return self.page.get_by_label('Description:')

    def instructions(self):
        return self.page.locator('.note-editable')

    def status(self):
        return self.page.get_by_label('Add Review Form').get_by_text('Active', exact=True)

    def save(self):
        return self.page.get_by_text('Save')

    #edit
    def edit(self):
        return self.page.locator('#Body_gvChecklist_ctl00_0')

    #delete
    def delete(self):
        return self.page.locator('#Body_gvChecklist_ctl02_0')

    def yes(self):
        return self.page.locator('button').filter(has_text='Yes')
