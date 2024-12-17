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


class EditEECareerProfile(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

        # add Career Profile

    def ee_select(self):
        return self.page.get_by_role('link', name="Abraham, Joseph1 m")

    def select_careerprofile(self):
        return self.page.get_by_role('link', name='Career Profile ')


    def add_event(self):
        return self.page.get_by_role('link', name='+ Add Event')

    def add_summary(self):
        return self.page.get_by_label('Summary:')

    def add_details(self):
        return self.page.get_by_label('Details:')

    def save_select(self):
        return self.page.get_by_text('Save')

# edit sections starts from here

    def edit_event(self):
        return self.page.locator('#Body_Body_rptItems_btnEdit_0')

    def delete_event(self):
        return self.page.get_by_text('Delete')


