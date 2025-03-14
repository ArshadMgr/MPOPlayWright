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

class ApplicantQuizzes(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def add_quiz(self):
        return self.page.get_by_role('link', name="+ Add New Quiz")

    def quiz_name(self):
        return self.page.get_by_label('Quiz Name:')

    def score(self):
        return self.page.get_by_label('Minimum Passing Score:')

    def description(self):
        return self.page.get_by_label('Description:')

    def save(self):
        return self.page.get_by_text('Save')

    def question(self):
        return self.page.get_by_label('Question:')

    def question_score(self):
        return self.page.get_by_label('Score:')

    def save_question(self):
        return self.page.get_by_role('link', name='Save Question')

    def back(self):
        return self.page.get_by_role('link', name=' Back' )

    def delete(self):
        return self.page.get_by_role('row', name='Testing Quiz 1 3/14/2025').get_by_role('link').nth(3)

    def yes(self):
        return self.page.get_by_text('Yes')