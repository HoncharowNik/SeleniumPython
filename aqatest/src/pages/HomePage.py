import pytest

from aqatest.src.helpers.config_helpers import get_base_url
from aqatest.src.SeleniumExtended import SeleniumExtended
from aqatest.src.pages.locators.HomePageLocators import HomePageLocatoes


class HomePage(HomePageLocatoes):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_homepage(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def clicl_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_RO_CART_BTN)

