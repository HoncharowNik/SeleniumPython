
from aqatest.src.SeleniumExtended import SeleniumExtended
from aqatest.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from aqatest.src.helpers.generic_helpers import generate_random_email_and_password

class CheckoutPage(CheckoutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_billing_first_name(self, first_name = None):
        first_name = first_name if first_name else 'RandomFname'

        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)

    def input_billing_last_name(self, last_name = None):
        last_name = last_name if last_name else 'RandomLname'

        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)

    def input_billing_address(self, address = None):
        address = address if address else 'Random st'

        self.sl.wait_and_input_text(self.BILLING_ADDRESS_1_FIELD, address)

    def input_billing_city(self, city = None):
        city = city if city else 'Random'

        self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city)

    def input_billing_zip(self, zip = None):
        zip = zip if zip else '12345'

        self.sl.wait_and_input_text(self.BILLING_ZIP_FIELD, zip)

    def input_billing_phone(self, phone = None):
        phone = phone if phone else '5550000055'

        self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, phone)

    def input_billing_email(self, email = None):
        if not email:
            ramdom_email = generate_random_email_and_password()
            email = ramdom_email['email']

        self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)

    def click_place_order_btn(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)

    def fill_in_billing_info(self, first_name = None, last_name = None, address = None, city = None, zip = None, phone = None, email = None):
        self.input_billing_first_name(first_name=first_name)
        self.input_billing_last_name(last_name=last_name)
        self.input_billing_address(address=address)
        self.input_billing_city(city=city)
        self.input_billing_zip(zip=zip)
        self.input_billing_phone(phone=phone)
        self.input_billing_email(email=email)
        self.click_place_order_btn()

