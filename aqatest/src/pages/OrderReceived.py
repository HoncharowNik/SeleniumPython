import pdb

from aqatest.src.pages.locators.OrderReceivedLocators import OrderReceivedLocators
from aqatest.src.SeleniumExtended import SeleniumExtended

class OrderReceived(OrderReceivedLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_order_receive_page_loaded(self):
        self.sl.wait_until_element_contains_text(self.PAGE_MAIN_HEADER, 'Order received')

    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NUMBER)

