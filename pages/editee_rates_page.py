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

class EditEERates(BasePage):

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

#Rates
    #Add

    def select_rates(self):
        return self.page.get_by_role('link', name= 'Rates ')

    def add_rates(self):
        return self.page.get_by_role('link', name=  '+ Add Rate')

    def select_pay(self):
        return self.page.get_by_text('Pay Schedule: Select Bi-')

    def type_pay(self):
        return self.page.locator('input[type="search"]')

    def enter_pay(self):
        return self.page.locator('input[type="search"]')

    def select_paytype(self):
        return self.page.get_by_text('Pay Type: Select Commission')

    def type_paytype(self):
        return self.page.locator('input[type="search"]')

    def enter_paytype(self):
        return self.page.locator('input[type="search"]')

    def select_exempt(self):
        return self.page.get_by_text('Exempt: Select Yes No Select')

    def type_exempt(self):
        return self.page.locator('input[type="search"]')

    def enter_exempt(self):
        return self.page.locator('input[type="search"]')

    def hours(self):
        return self.page.get_by_label('Default Hours (Pay Period):')

    def annual(self):
        return self.page.get_by_label('Annual Salary:')

    def effective_datee(self):
        return self.page.locator('#select2-Body_Body_tabContainer_ucDefaultRates_ucDefaultRateModal_ucDefaultRate_ddlEffectiveDate-container')

    def type_effective_datee(self):
        return self.page.locator('input[type="search"]')

    def enter_effective_datee(self):
        return self.page.locator('input[type="search"]')

    def edit_rates(self):
        return self.page.get_by_role('link', name= '').nth(0)

    def press_save(self):
        return self.page.get_by_text('Save')

    def delete_rates(self):
        return self.page.get_by_role('link', name= '').nth(0)

    def enter_yes(self):
        return self.page.locator("//button[normalize-space()='Yes']")