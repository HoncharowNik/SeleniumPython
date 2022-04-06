
import pytest
from aqatest.src.pages.MyAccount import MyAccount
from aqatest.src.pages.MyAccountSignedIN import MyAccountSignedIn
from aqatest.src.helpers.generic_helpers import generate_random_email_and_password

@pytest.mark.usefixtures('init_driver')
class TestRegisterNewUser:

    @pytest.mark.tcid2
    def test_register_valid_new_user(self):

        rand_email = generate_random_email_and_password()
        my_account_i = MyAccountSignedIn(self.driver)
        my_account = MyAccount(self.driver)
        my_account.go_to_my_account()
        my_account.input_register_mail(rand_email['email'])
        my_account.input_register_password(rand_email['password'])
        my_account.click_on_register_button()
        my_account_i.verify_user_is_signed_in()