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

class EditEEEEquipment(BasePage):

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

    def select_equipment(self):
        return self.page.get_by_role('link', name='Equipment ')

    def add_equipment(self):
        return self.page.get_by_role('link', name='+ Add Equipment')

    def equipment_issued(self):
        return self.page.get_by_label('Equipment Issued:')

    def serial_number(self):
        return self.page.get_by_label('Serial Number:')

    def date_issued(self):
        return self.page.get_by_label('Date Issued:')

    def issued_by(self):
        return self.page.get_by_label('Issued By:')

    def return_to(self):
        return self.page.get_by_label('Returned To:')

    def notess(self):
        return self.page.get_by_label('Notes:')

    def edit_equipment(self):
        return self.page.get_by_role('link', name='').nth(0)

    def press_save(self):
        return self.page.get_by_text('Save')

    def delete_equipment(self):
        return self.page.get_by_role('link', name='').nth(0)

    def enter_yes(self):
        return self.page.get_by_text('Yes')