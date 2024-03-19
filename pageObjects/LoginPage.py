from selenium.webdriver.common.by import By

from pageObjects.MyAccountPage import MyAccountPageObjects


class LoginPageObjects:

    def __init__(self, driver):
        self.driver = driver

    __email_filed_loc = (By.ID, "input-email")
    __password_filed_loc = (By.ID, "input-password")
    __login_button_loc = (By.CSS_SELECTOR, "[type='submit']")

    __warning_message_of_email_password_loc = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

    def email_field(self):
        return self.driver.find_element(*self.__email_filed_loc)

    def password_field(self):
        return self.driver.find_element(*self.__password_filed_loc)

    def login_button(self):
        self.driver.find_element(*self.__login_button_loc).click()
        myAccount = MyAccountPageObjects(self.driver)
        return myAccount

    def no_match_warning_message_of_email_password(self, warning_message):
        message = self.driver.find_element(*self.__warning_message_of_email_password_loc).text
        if message.casefold().__contains__(warning_message.casefold()):
            return True
        return False




