from aqatest.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators
from aqatest.src.SeleniumExtended import SeleniumExtended

class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LEDT_NAV_LOGOUT_BTN)
