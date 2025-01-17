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

class HrViewAnnouncemnets(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def add_new(self):
        return self.page.get_by_role('link', name="+ Add New Announcement")

    def summary(self):
        return self.page.get_by_label('Summary:')

    def release_date(self):
        return self.page.get_by_label('Release Date:')

    def release_time(self):
        return self.page.get_by_label('Release Time:')

    def description(self):
        return self.page.locator('#Body_updatePanelMain div').filter(
            has_text='Description:'
        ).get_by_role('textbox')

    def save_button(self):
        return self.page.get_by_role('link', name="Save")

    #edit
    #def edit(self):
     #   return self.page.locator('role=row[name="Summary for testing 4/6/2025"]').locator('role=link').nth(1)

    #delete
    def delet(self):
        return self.page.locator('#Body_gvAnnouncements_btnDelete_0')

    def yes_button(self):
        return self.page.get_by_text("Yes")