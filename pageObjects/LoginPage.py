from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.MyAccountPage import MyAccountPageObjects


class LoginPageObjects(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __email_filed_loc = (By.ID, "input-email")
    __password_filed_loc = (By.ID, "input-password")
    __login_button_loc = (By.CSS_SELECTOR, "[type='submit']")

    __warning_message_of_email_password_loc = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

    def email_field(self, *, send_keys):
        # return self.driver.find_element(*self.__email_filed_loc)

        # return self.find_element(self.__email_filed_loc)
        return self.enter_text_into_element(self.__email_filed_loc, send_keys)

    def password_field(self, *, send_keys):

        # return self.driver.find_element(*self.__password_filed_loc)
        # return self.find_element(self.__password_filed_loc)
        return self.enter_text_into_element(self.__password_filed_loc, send_keys)

    def login_button(self):
        # self.driver.find_element(*self.__login_button_loc).click()

        self.click_element(self.__login_button_loc)

        myAccount = MyAccountPageObjects(self.driver)
        return myAccount

    def no_match_warning_message_of_email_password(self, warning_message):
        # message = self.driver.find_element(*self.__warning_message_of_email_password_loc).text

        message = self.get_element_text(self.__warning_message_of_email_password_loc)


        if message.casefold().__contains__(warning_message.casefold()):
            return True
        return False
