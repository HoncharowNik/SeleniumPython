
import pytest
from aqatest.src.pages.HomePage import HomePage
from aqatest.src.pages.Header import Header
from aqatest.src.pages.CartPage import CartPage
from aqatest.src.pages.OrderReceived import OrderReceived
from aqatest.src.configs.generic_condigs import GenericConfigs
from aqatest.src.pages.CheckoutPage import CheckoutPage
from aqatest.src.helpers.database_helpers import get_order_from_db_by_order_no


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid3
    def test_end_to_end_checkout_guest_user(self):
        pass

        home_p = HomePage(self.driver)
        cart_p = CartPage(self.driver)
        header = Header(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceived(self.driver)


        home_p.go_to_homepage()
        home_p.clicl_first_add_to_cart_button()
        header.wait_until_cart_item_count(1)
        header.click_on_cart_on_right_header()
        product_names = cart_p.get_all_product_names_in_cart()
        assert len(product_names) == 1, f'Expected 1 item in cart but found{len(product_names)}'
        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)
        cart_p.click_on_proceed_to_checkout()
        checkout_p.fill_in_billing_info()
        order_received_p.verify_order_receive_page_loaded()


        # Quary to database.

        # order_no = order_received_p.get_order_number()
        # dbs_order = get_order_from_db_by_order_no(order_no)
        # assert dbs_order, f'After creating order with FE, not found in DB. Order no: {order_no}'


