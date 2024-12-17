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

class EditEESkills(BasePage):

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

    def select_skills(self):
        return self.page.get_by_role('link', name="Skills ")

    def select_manage_skill(self):
        return self.page.get_by_role('link', name=" Manage Skill")

    def select_group_skill(self):
        return self.page.get_by_role('tab', name="Skill Groups")

    def add_group_skill(self):
        return self.page.get_by_role('link', name="+ Add Group")

    def type_skill_group(self):
        return self.page.locator("//input[@id='Body_tabContainer_skillGroupsTab_tbSkillGroup']")

    def press_save(self):
        return self.page.locator("//a[@id='Body_tabContainer_skillGroupsTab_btnSaveSkillGroup']")

    def select_company_skill(self):
        return self.page.get_by_role('tab', name="Company Skills")

    def add_company_skill(self):
        return self.page.get_by_role('link', name="+ Add Skill")

    def add_skill_group(self):
        return self.page.get_by_label("Select")

    def type_group_skill(self):
        return self.page.locator('input[type="search"]')

    def enter_group_skill(self):
        return self.page.locator('input[type="search"]')

    def add_skill_name(self):
        return self.page.get_by_label("Skill Name:")

    def presss_save(self):
        return self.page.locator("//a[@id='Body_tabContainer_companySkillsTab_btnSaveSkillGroup']")

    def add_skill(self):
        return self.page.get_by_role('link', name="+ Add Skill")

    def skill_group(self):
        return self.page.locator("#select2-Body_Body_ddlSkillGroup-container")

    def type_skill_gorup(self):
        return self.page.locator('input[type="search"]')

    def enter_skill_group(self):
        return self.page.locator('input[type="search"]')

    def skill_name(self):
        return self.page.locator("#select2-Body_Body_ddlSkillName-container")

    def type_skill_name(self):
        return self.page.locator('input[type="search"]')

    def enter_skill_name(self):
        return self.page.locator('input[type="search"]')

    def proficiency(self):
        return self.page.locator("#select2-Body_Body_ddlProficiency-container")

    def type_proficiency(self):
        return self.page.locator('input[type="search"]')

    def enter_proficiency(self):
        return self.page.locator('input[type="search"]')

    def add_note(self):
        return self.page.get_by_label("Notes:")

    def save(self):
        return self.page.get_by_text("Save")

    def edit_skill(self):
        return self.page.get_by_role('link', name="").nth(0)

    def delete_skill(self):
        return self.page.get_by_role('link', name="").nth(0)

    def yes(self):
        return self.page.get_by_text("Yes")