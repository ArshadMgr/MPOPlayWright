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

class EditEEPerviousEmployers(BasePage):

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

    def edit_previous_employer(self):
        return self.page.get_by_role('link', name='Previous Employers ')

    def add_previous_employer(self):
        return self.page.get_by_role('link', name='+ Add Previous Employer')

    def business_type(self):
        return self.page.get_by_label('Business Type:')

    def employer(self):
        return self.page.get_by_label('Employer:')

    def start_datee(self):
        return self.page.get_by_label('Start Date:')

    def salary(self):
        return self.page.get_by_label('Salary:')

    def select_salary_per(self):
        return self.page.locator('div:nth-child(6) > .col-md-5')

    def type_salryper(self):
        return self.page.locator('input[type="search"]')

    def enter_salryper(self):
        return self.page.locator('input[type="search"]')

    def job_titlee(self):
        return self.page.get_by_label('Job Title:')

    def term_reason(self):
        return self.page.get_by_label('Term Reason:')

    def phonee(self):
       return self.page.get_by_label('Phone:')

    def supervisor(self):
        return self.page.get_by_label('Supervisor:')

    def duties(self):
        return self.page.get_by_label('Duties:')

    def notes(self):
        return self.page.get_by_label('Notes:')

    def edit_perviousemploye(self):
        return self.page.locator("// tbody / tr[1] / td[15] / a[1] / span[1]").nth(0)

    def press_save(self):
        return self.page.get_by_text('Save')

    def delete_perviousemploye(self):
        return self.page.locator("(//span[@class='glyphicon glyphicon-remove'])[1]").nth(0)

    def enter_yes(self):
        return self.page.locator("//button[normalize-space()='Yes']")

