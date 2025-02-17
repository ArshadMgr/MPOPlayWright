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

class OKR(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")


    #Add OKR Category

    def okr_category(self):
        return self.page.get_by_role('link', name="OKR Categories")

    def add_okr(self):
        return self.page.get_by_role('link', name="+ Add OKR Category")

    def add_title(self):
        return self.page.get_by_label("Title:")

    def add_description(self):
        return self.page.get_by_label("Description:")

    def save(self):
        return self.page.get_by_text("Save")

    # Add OKR (Company)
    def add_okrcompany(self):
        return self.page.get_by_role('link', name='+ Add Objective')

    def objective_title(self):
        return self.page.get_by_label('Objective Title:')

    def objective_description(self):
        return self.page.locator('.note-editable')

    def type_category(self):
        return self.page.locator('#select2-Body_ddlCategory-container')

    def select_category(self):
        return self.page.get_by_role('searchbox')

    def enter_category(self):
        return self.page.get_by_role('searchbox')

    def start_date(self):
        return self.page.get_by_label('Start Date:')

    def due_date(self):
        return self.page.get_by_label('Due Date:')

    def viewing_rights(self):
        return self.page.get_by_text('Public', exact=True)

    def save_okr(self):
        return self.page.get_by_role('link', name=' Save')

    #delete OKR (Company)

    def company_okr(self):
        return self.page.get_by_role('tab', name='Company Objectives')

    def delete_company(self):
        return self.page.get_by_role('row', name='Testing Objective Ttitle 0').get_by_role('link').nth(2)

    def yes(self):
        return self.page.get_by_text("Yes")

    #add Okr (Department)
    def select_department(self):
        return self.page.get_by_role('textbox', name='Company')

    def type_department(self):
        return self.page.get_by_role('searchbox')

    def enter_department(self):
        return self.page.get_by_role('searchbox')

    #delete OKR (department)
    def delete_department(self):
        return self.page.get_by_role("link", name='').nth(0)

    # add Okr (personal)
    def select_personal(self):
        return self.page.get_by_role('textbox', name='Company')
    def type_personal(self):
        return self.page.get_by_role('searchbox')

    def enter_personal(self):
        return self.page.get_by_role('searchbox')

    def type_assignee(self):
        return self.page.locator('#select2-Body_ddlEmployee-container')

    def select_assignee(self):
        return self.page.get_by_role('searchbox')

    def enter_assignee(self):
        return self.page.get_by_role('searchbox')

    # delete OKR (personal)
    def delete_personal(self):
        return self.page.get_by_role('row', name='Amy Neal Testing Objective').get_by_role('link').nth(2)

    # delete OKR Category
    def delete_category(self):
        return self.page.get_by_role("link", name='').nth(3)