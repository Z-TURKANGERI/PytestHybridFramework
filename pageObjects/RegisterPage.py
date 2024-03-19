from selenium.webdriver.common.by import By

from pageObjects.NewAccountCreatedPage import NewAccountCreatedPageObjects


class RegisterPageObjects:

    def __init__(self, driver):
        self.driver = driver

    __register_firstName_loc = (By.ID, "input-firstname")
    __register_lastName_loc = (By.ID, "input-lastname")
    __register_email_loc = (By.ID, "input-email")
    __register_telephone_loc = (By.ID, "input-telephone")
    __register_password_loc = (By.ID, "input-password")
    __register_confirm_password_loc = (By.ID, "input-confirm")
    __register_privacy_policy_loc = (By.CSS_SELECTOR, "input[name=agree]")
    __register_continue_button_loc = (By.CSS_SELECTOR, "input[type=submit]")
    __register_newsletter_yes_loc = (By.XPATH, "//label[text()='Yes']/input")
    __register_newsletter_no_loc = (By.XPATH, "//label[text()='No']/input")

    def register_first_name(self):
        return self.driver.find_element(*self.__register_firstName_loc)

    def register_last_name(self):
        return self.driver.find_element(*self.__register_lastName_loc)

    def register_email(self):
        return self.driver.find_element(*self.__register_email_loc)

    def register_telephone(self):
        return self.driver.find_element(*self.__register_telephone_loc)

    def register_password(self):
        return self.driver.find_element(*self.__register_password_loc)

    def register_confirm_password(self):
        return self.driver.find_element(*self.__register_confirm_password_loc)

    def register_privacy_policy(self):
        return self.driver.find_element(*self.__register_privacy_policy_loc)

    def register_continue_button_loc(self):
        self.driver.find_element(*self.__register_continue_button_loc).click()
        newAccountPage = NewAccountCreatedPageObjects(self.driver)
        return newAccountPage

    def newsletter_YES(self):
        return self.driver.find_element(*self.__register_newsletter_yes_loc)

    def newsletter_NO(self):
        return self.driver.find_element(*self.__register_newsletter_no_loc)

