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


class EditEEEEmergencyContact(BasePage):

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

    def select_emergencycontacts(self):
        return self.page.get_by_role('link',name= 'Emergency Contacts ')

    def add_emergencycontacts(self):
        return self.page.get_by_role('link',name= '+ Add Emergency Contact')

    def contactname(self):
        return self.page.get_by_label('Contact Name:')

    def select_relation(self):
        return self.page.locator('#select2-Body_Body_ddlRelationship-container')

    def type_relation(self):
        return self.page.locator('input[type="search"]')

    def enter_relation(self):
        return self.page.locator('input[type="search"]')

    def selectcountry(self):
        return self.page.locator('#select2-Body_Body_ddlCountryID-container')

    def type_country(self):
        return self.page.locator('input[type="search"]')

    def enter_country(self):
        return self.page.locator('input[type="search"]')

    def address1(self):
        return self.page.get_by_label('Address 1:')

    def homephone(self):
        return self.page.get_by_label('Home Phone:')

    def workphone(self):
        return self.page.get_by_label('Work Phone:')

    def cellphone(self):
        return self.page.get_by_label('Cell Phone:')

    def email(self):
        return self.page.get_by_label('Email Address:')

    #Edit

    def edit_emergency(self):
        return self.page.get_by_role('link', name='').nth(0)

    def press_save(self):
        return self.page.get_by_text('Save')

    def delete_emergency(self):
        return self.page.get_by_role('link', name='').nth(0)

    def enter_yes(self):
        return self.page.get_by_text('Yes')