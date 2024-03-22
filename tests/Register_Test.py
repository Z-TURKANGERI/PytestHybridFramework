import pytest

from pageObjects.HomePage import HomePageObjects
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):

    @pytest.mark.smoke
    def test_verify_register_by_providing_mandatory_fields(self):
        homePage = HomePageObjects(self.driver)
        registerPage = homePage.click_on_account_drop_down_and_click_on_register()
        registerPage.register_first_name(send_keys=self.fake_data(first_name=True))
        registerPage.register_last_name(send_keys=self.fake_data(last_name=True))
        registerPage.register_email(send_keys=self.generate_email_with_time_stamp())
        registerPage.register_telephone(send_keys=self.fake_data(phone_number=True))
        registerPage.register_password(send_keys="12345")
        registerPage.register_confirm_password(send_keys="12345")
        registerPage.register_click_on_privacy_policy()
        newAccountPage = registerPage.register_continue_button_loc()
        assert newAccountPage.new_account_created_message().is_displayed()

    def test_verify_register_by_providing_all_fields(self):
        homePage = HomePageObjects(self.driver)
        registerPage = homePage.click_on_account_drop_down_and_click_on_register()
        registerPage.register_first_name(send_keys=self.fake_data(first_name=True))
        registerPage.register_last_name(send_keys=self.fake_data(last_name=True))
        registerPage.register_email(send_keys=self.generate_email_with_time_stamp())
        registerPage.register_telephone(send_keys=self.fake_data(phone_number=True))
        registerPage.register_password(send_keys="12345")
        registerPage.register_confirm_password(send_keys="12345")
        registerPage.newsletter_click_YES()
        registerPage.register_click_on_privacy_policy()
        newAccountPage = registerPage.register_continue_button_loc()
        assert newAccountPage.new_account_created_message().is_displayed()
