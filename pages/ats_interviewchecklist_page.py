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

class InterviewChecklist(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    # Interview CheckLists
    def interview_tab(self):
        return self.page.get_by_role('tab', name= 'Interview Checklists' )

    def add_interviewlist(self):
        return self.page.get_by_role('link', name= '+ Add Checklist')

    def checklist_name(self):
        return self.page.get_by_label("Checklist Name:")

    def associate_job(self):
        return self.page.get_by_label('Manage Checklist').get_by_title('Select')

    def enter_associate_job(self):
        return self.page.locator('input[type="search"]')

    def interviewer_instructions(self):
        return self.page.get_by_text('Interviewer Instructions:')

    def active(self):
        return self.page.locator('.col-md-6 > .AspireCheckBox > label')

    def save(self):
        return self.page.get_by_text('Save')

    # add Question
    def add_question(self):
        return self.page.get_by_role('link', name= '+ Add New Question' )

    def question(self):
        return self.page.get_by_label('Question:')

    def active1(self):
        return self.page.locator('#Body_dvisActive label').nth(1)

    def save_sort(self):
        return self.page.get_by_role('link', name=' Save Sort Order')

    def cancel(self):
        return self.page.get_by_role('link', name= 'Cancel')

    def schedule_interview(self):
        return self.page.get_by_role('link', name= '+ Schedule Interview' )

    def interview_list(self):
        return self.page.locator('#select2-Body_tabContainer_candidateInterviewTab_ddlInterviewChecklistID-container')

    def select_interview_list(self):
        return self.page.locator('input[type="search"]')

    def applicant(self):
        return self.page.locator('#select2-Body_tabContainer_candidateInterviewTab_ddlApplicantID-container')

    def select_applicant(self):
        return self.page.locator('input[type="search"]')

    def interview_date(self):
        return self.page.get_by_label("Interview Date/Time:")

    def location(self):
        return self.page.locator("#select2-Body_tabContainer_candidateInterviewTab_ddlCLocationID-container")

    def location_select(self):
        return self.page.locator('input[type="search"]')

    def interviewer_list(self):
        return self.page.get_by_text('None')

    def select_interviewer(self):
        return self.page.locator('a').filter(has_text="Employer - Michael Hoffman (")

    def close_list(self):
        return self.page.get_by_text('Interviewer List:')

    def schedule_done(self):
        return self.page.locator('#Body_tabContainer_candidateInterviewTab_btnSave')

    # Delete Section
    def search_date(self):
        return self.page.get_by_label("From Date:")

    def search(self):
        return self.page.get_by_role('link', name= ' Search' )

    def delete(self):
        return self.page.get_by_role('link', name= '')

    def yes(self):
        return self.page.get_by_text('Yes')

    def delete_list(self):
        return self.page.get_by_role('row',  name= 'Testing list HR Manager 1 0 0' ).get_by_role('link').nth(3)
