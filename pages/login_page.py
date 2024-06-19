from playwright.sync_api import Page
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Username:")
        self.password_input = page.get_by_label("Password:")
        self.login_button = page.get_by_role("link", name=" Sign In")
        # self.click_Role =
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")

    def enter_username(self, username: str):
        self.username_input.fill(username)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def click_role(self):
        self.click_Role.click()

    def search_role(self, role: str):
        self.search_role.fill(role)

    def click_role(self):
        self.click_Role.click()

    def click_go_button(self):
        self.go_btn.click()

    def clik_ee_role(self):
        self.click_ee_role.click()

    def enter_employer(self, role: str):
        self.fill_er_role.fill(role)

    def press_enter(self):
        self.search_role.press("Enter")

