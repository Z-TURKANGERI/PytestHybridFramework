import pytest

from pageObjects.HomePage import HomePageObjects
from utilities import ExcelUtils
from utilities.BaseTest import BaseClass


class TestLogin(BaseClass):

    @pytest.mark.parametrize("email,password",
                             ExcelUtils.get_data_from_excel("excelFiles/TutorialsNinja.xlsx", "LoginTest"))
    def test_logging_with_valid_credential(self, email, password):
        homePage = HomePageObjects(self.driver)
        loginPage = homePage.click_on_account_drop_down_and_click_on_logic()
        loginPage.email_field().send_keys(email)
        loginPage.password_field().send_keys(password)
        myAccount = loginPage.login_button()
        assert myAccount.my_account_info().is_displayed()

    def test_logging_with_invalid_credential(self):
        homePage = HomePageObjects(self.driver)
        loginPage = homePage.click_on_account_drop_down_and_click_on_logic()
        loginPage.email_field().send_keys(self.generate_email_with_time_stamp())
        loginPage.password_field().send_keys("01061997")
        loginPage.login_button()
        assert loginPage.no_match_warning_message_of_email_password(
            "Warning: No match for E-Mail Address and/or Password.")

    def test_logging_with_valid_username_invalid_password(self):
        homePage = HomePageObjects(self.driver)
        loginPage = homePage.click_on_account_drop_down_and_click_on_logic()
        loginPage.email_field().send_keys("zubertest0@gmail.com")
        loginPage.password_field().send_keys("12345")
        loginPage.login_button()
        assert loginPage.no_match_warning_message_of_email_password(
            "Warning: No match for E-Mail Address and/or Password.")

    def test_logging_without_credential(self):
        homePage = HomePageObjects(self.driver)
        loginPage = homePage.click_on_account_drop_down_and_click_on_logic()
        loginPage.login_button()
        assert loginPage.no_match_warning_message_of_email_password(
            "Warning: No match for E-Mail Address and/or Password.")
