from playwright.sync_api import Page
from .base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page: Page):
        self.page = page

        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"

        self.fill_er_role = page.get_by_role("searchbox")

    def enter_username(self, username):
        self.fill(self.page.get_by_label("Username:"), username)

    def enter_password(self, password):
        self.fill(self.page.get_by_label("Password:"), password)

    def click_login(self):
        self.click(self.page.get_by_role("link", name=" Sign In"))

    def click_role(self):
        self.click_Role.click()

    def search_role(self, role: str):
        self.search_role.fill(role)

    def click_role(self):
        self.click_Role.click()

    def click_go_button(self):
        self.click(self.page.get_by_role("link", name="Go"))

    def clik_ee_role(self):
        self.click(self.page.get_by_role("textbox", name="Employee"))

    def enter_employer(self, role: str):
        self.fill_er_role.fill(role)

    def press_enter(self):
        self.page.keyboard.press('Enter')
