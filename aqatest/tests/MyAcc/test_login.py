
import pytest
from aqatest.src.pages.MyAccount import MyAccount
from aqatest.src.helpers.generic_helpers import generate_random_email_and_password

@pytest.mark.usefixtures('init_driver')
class TestLoginNegative:

    @pytest.mark.tcid1
    def test_login_none(self):

        rand_email = generate_random_email_and_password()

        my_account = MyAccount(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_name(rand_email['email'])
        my_account.input_login_password(rand_email['password'])
        my_account.click_on()
        expected_err = "Unknown email address. Check again or try your username."
        my_account.wait_until_error_is_displayed(expected_err)




