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

    def test_verify_register_error_message_for_all_mandatory_fields(self):
        homePage = HomePageObjects(self.driver)
        registerPage = homePage.click_on_account_drop_down_and_click_on_register()
        registerPage.register_continue_button_loc()

        assert registerPage.first_name_error_message() == "First Name must be between 1 and 32 characters!"
        assert registerPage.last_name_error_message() == "Last Name must be between 1 and 32 characters!"
        assert registerPage.email_error_message() == "E-Mail Address does not appear to be valid!"
        assert registerPage.telephone_error_message() == "Telephone must be between 3 and 32 characters!"
        assert registerPage.password_error_message() == "Password must be between 4 and 20 characters!"
        assert registerPage.privacy_policy_error_message() == "Warning: You must agree to the Privacy Policy!"

    def test_verify_register_by_providing_different_password_and_confirm_password(self):
        homePage = HomePageObjects(self.driver)
        registerPage = homePage.click_on_account_drop_down_and_click_on_register()
        registerPage.register_first_name(send_keys=self.fake_data(first_name=True))
        registerPage.register_last_name(send_keys=self.fake_data(last_name=True))
        registerPage.register_email(send_keys=self.generate_email_with_time_stamp())
        registerPage.register_telephone(send_keys=self.fake_data(phone_number=True))
        registerPage.register_password(send_keys="01061997")
        registerPage.register_confirm_password(send_keys="12345")
        registerPage.register_click_on_privacy_policy()
        registerPage.register_continue_button_loc()

        assert self.get_page_title("Register Account")
        assert registerPage.confirm_password_error_message() == "Password confirmation does not match password!"

    def test_verify_register_by_providing_existing_account_details(self):
        # homePage = HomePageObjects(self.driver)
        # registerPage = homePage.click_on_account_drop_down_and_click_on_register()
        # registerPage.register_first_name(send_keys=self.fake_data(first_name=True))
        # registerPage.register_last_name(send_keys=self.fake_data(last_name=True))
        # registerPage.register_email(send_keys=self.generate_email_with_time_stamp())
        # registerPage.register_telephone(send_keys=self.fake_data(phone_number=True))
        # registerPage.register_password(send_keys="12345")
        # registerPage.register_confirm_password(send_keys="12345")
        # registerPage.register_click_on_privacy_policy()
        # newAccountPage = registerPage.register_continue_button_loc()
        # assert newAccountPage.new_account_created_message().is_displayed()
        pass