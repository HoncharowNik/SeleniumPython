from selenium import webdriver
from aqatest.src.SeleniumExtended import SeleniumExtended
from aqatest.src.pages.locators.MyAccountLocator import MyAccountLocator
from aqatest.src.helpers.config_helpers import get_base_url


class MyAccount(MyAccountLocator):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def input_login_name(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_on(self):
        self.sl.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)

    def input_register_mail(self, mail):
        self.sl.wait_and_input_text(self.REGISTER_MAIL, mail)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_on_register_button(self):
        self.sl.wait_and_click(self.REGISTER_BTN)

