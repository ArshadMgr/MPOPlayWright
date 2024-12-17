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


class NewHirePage(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.search_role = page.get_by_role("searchbox")
        self.click_role = page.get_by_role("option", name="Employer")
        self.go_btn = page.get_by_role("link", name="Go")
        self.page_title = page.title() == "Sign In"
        self.click_ee_role = page.get_by_role("textbox", name="Employee")
        self.fill_er_role = page.get_by_role("searchbox")


    def first_name(self):
        return self.page.get_by_label('First Name: *')

    def middle_name(self):
        return self.page.get_by_label('Middle Initial:')

    def link_newhire_btn(self):
        return self.page.get_by_role("link", name="+ Add New Hire")

    def last_name(self):
        return self.page.get_by_label('Last Name: *')

    def nick_name(self):
        return self.page.get_by_label('Nickname:')

     # code by haseeb
    def user_name(self):
        return self.page.get_by_label('Username: *')

    def date_of_birth(self):
        return self.page.get_by_label('Date of Birth: *')

    def ssn(self):
         return self.page.get_by_label('SSN: *')

    def gender_field(self):
         return self.page.get_by_text('Gender: Select Female Male')

    def select_gender(self):
        return self.page.get_by_role('searchbox')

    def enter_gender(self):
        return self.page.get_by_role('searchbox')

    def ethnicity_field(self):
         return self.page.get_by_text('Ethnicity: Select American')

    def select_ethnicity(self):
        return self.page.get_by_role('searchbox')

    def enter_ethnicity(self):
        return self.page.get_by_role('searchbox')

    def marital_status(self):
        return self.page.get_by_text('Marital Status: Select')

    def select_marital_status(self):
        return self.page.get_by_role('searchbox')

    def enter_marital_status(self):
        return self.page.get_by_role('searchbox')

    def veteran_field(self):
        return self.page.get_by_text('Veteran: Select Yes No')

    def select_veteran_field(self):
        return self.page.get_by_role('searchbox')

    def enter_veteran_field(self):
        return self.page.get_by_role('searchbox')

    def employee_id(self):
        return self.page.get_by_label('Employee ID: *')

    def employee_payroll_id(self):
        return self.page.get_by_label('Employee Payroll ID:')

        # Contact Information
    def select_email(self):
        return self.page.get_by_text('Primary Email: Select Email')

    def select_email_status(self):
        return self.page.get_by_role('searchbox')

    def enter_email_status(self):
        return self.page.get_by_role('searchbox')

    def work_email(self):
        return self.page.get_by_label('Work Email:')

    def personal_email(self):
        return self.page.get_by_label('Personal Email:')

    def home_phone(self):
        return self.page.get_by_label('Home Phone:')

    def work_phone(self):
        return self.page.get_by_label('Work Phone:')

    def cell_phone(self):
        return self.page.get_by_label('Cell Phone:')

    def select_country(self):
        return self.page.get_by_label('United States')

    def enter_country_name(self):
        return self.page.get_by_role('searchbox')

    def press_enter(self):
        return self.page.get_by_role('searchbox')

        # skip address sectiom
    def address_street(self):
        return self.page.get_by_role('textbox', name='Street Address:')

    def address_2(self):
        return self.page.get_by_role('textbox', name='Address 2:')

    def city(self):
        return self.page.get_by_role('textbox', name='City:')

    def state(self):
        return self.page.get_by_text('State Select Alabama Alaska')

    def select_state(self):
        return self.page.get_by_role('searchbox')

    def enter_state(self):
        return self.page.get_by_role('searchbox')

    def zip_code(self):
        return self.page.get_by_role('textbox', name='Zip Code:')

    def mailing_address(self):
        return self.page.locator('/html[1]/body[1]/form[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div[9]/div[1]/div[1]/div[1]/div[1]/div[1]/label[2]')

        # Status/information information

    def user_group(self):
        return self.page.get_by_text('User Group: * Select Nasir')

    def select_user_group(self):
        return self.page.get_by_role('searchbox')

    def enter_user_group(self):
        return self.page.get_by_role('searchbox')

    def employee_status(self):
        return self.page.get_by_text('Employee Status: * Select')

    def select_employee_status(self):
        return self.page.get_by_role('searchbox')

    def enter_employee_status(self):
         return self.page.get_by_role('searchbox')

    def employee_type(self):
        return self.page.get_by_text('Employment Type: * Select')

    def select_employee_type(self):
        return self.page.get_by_role('searchbox')

    def enter_employee_type(self):
        return self.page.get_by_role('searchbox')

        # togel button seasonal skip
    def hiring_date(self):
        return self.page.get_by_label('Date of Hire: *')

    def job_title(self):
        return self.page.get_by_text('Job Title: * Select Dog')

    def select_job_title(self):
        return self.page.get_by_role('searchbox')

    def enter_job_title(self):
        return self.page.get_by_role('searchbox')

    def tier_title(self):
        return self.page.get_by_text('Tier: Select 1 (1) 2 (2) 3 (3')

    def select_tier_title(self):
        return self.page.get_by_role('searchbox')

    def enter_tier_title(self):
        return self.page.get_by_role('searchbox')

    def eeo_title(self):
        return self.page.get_by_text('EEO Class: Select')

    def select_eeo_title(self):
        return self.page.get_by_role('searchbox')

    def enter_eeo_title(self):
        return self.page.get_by_role('searchbox')

    def department_title(self):
        return self.page.get_by_text('Department: * Select (CS)')

    def select_department_title(self):
        return self.page.get_by_role('searchbox')

    def enter_department_title(self):
        return self.page.get_by_role('searchbox')

    def location_title(self):
        return self.page.get_by_text('Location: Select (WL)')

    def select_location_title(self):
        return self.page.get_by_role('searchbox')

    def enter_location_title(self):
        return self.page.get_by_role('searchbox')

        # desigantion not found
        # sub desigantion not found
        # country not found
        # level not found

    def primary_location_title(self):
        return self.page.get_by_text('Primary Work Location: Select')

    def select_primary_location_title(self):
        return self.page.get_by_role('searchbox')

    def enter_primary_location_title(self):
        return self.page.get_by_role('searchbox')

    def time_enter_title(self):
        return self.page.get_by_text('Time Entry Type: Manual Time')

    def select_time_enter_title(self):
        return self.page.get_by_role('searchbox')

    def enter_time_enter_title(self):
        return self.page.get_by_role('searchbox')

    def enable_punching(self):
         return self.page.get_by_text('Enable Punching: EnableDisable')

    def bypass_onboarding(self):
        return self.page.get_by_text('Bypass Onboarding: YesNo')

    def independent_contractor(self):
         return self.page.get_by_text('/ Independent Contractor: YesNo')

        # pay rate information

    def pay_schedule(self):
        return self.page.get_by_text('Pay Schedule: Select Bi-')

    def select_pay_schedule(self):
        return self.page.get_by_role('searchbox')

    def enter_pay_schedule(self):
        return self.page.get_by_role('searchbox')

    def pay_type(self):
        return self.page.get_by_text('Pay Type: * Select Commission')

    def select_pay_type(self):
        return self.page.get_by_role('searchbox')

    def enter_pay_type(self):
        return self.page.get_by_role('searchbox')

    def annual_salary(self):
        return self.page.get_by_label('Annual Salary: *')

    def default_hour(self):
        return self.page.get_by_label('Default Hours (Pay Period): *')

        # FederalTaxInformation

    def filling_status(self):
        return self.page.get_by_text('Filing Status: Exempt Head of')

    def select_filling_status(self):
        return self.page.get_by_role('searchbox')

    def enter_filling_status(self):
        return self.page.get_by_role('searchbox')

        # mutiple job toggle button

    def w4_submitted(self):
        return self.page.get_by_label('W-4 Submitted On:')

    def claim_dependents_amount(self):
        return self.page.get_by_label('Claim Dependents Amount:')

    def deduction(self):
         return self.page.get_by_label('Deductions:')

    def other_income(self):
        return self.page.get_by_label('Other Income:')

    def extra_withholding(self):
        return self.page.get_by_label('Extra Withholding:')

    def add_new_hire_button(self):
        return self.page.get_by_role('link', name='+ Add New Hire')

    def ee_select(self):
        return self.page.get_by_role('link', name="Adnan, Stephen m")

    def select_demogrpahics(self):
        return self.page.locator("#Body_Body_hlDemographics")

    def save(self):
        return self.page.get_by_role('link', name=' Save')
