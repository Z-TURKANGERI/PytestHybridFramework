from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.NewAccountCreatedPage import NewAccountCreatedPageObjects


class RegisterPageObjects(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

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

    """     Error messages locator      """
    __register_firstName_error_message = (
        By.XPATH, "//div[contains(text(),'First Name must be between 1 and 32 characters!')]")
    __register_lastName_error_message = (
        By.XPATH, "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]")
    __register_email_error_message = (By.XPATH, "//div[contains(text(),'E-Mail Address does not appear to be valid!')]")
    __register_telephone_error_message = (
        By.XPATH, "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]")
    __register_password_error_message = (
        By.XPATH, "//div[contains(text(),'Password must be between 4 and 20 characters!')]")
    __register_privacy_policy_error_message = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    __register_confirm_password_error_message = (By.CSS_SELECTOR, ".text-danger")

    def register_first_name(self, *, send_keys):
        # return self.driver.find_element(*self.__register_firstName_loc)
        # return self.find_element(self.__register_firstName_loc)
        return self.enter_text_into_element(self.__register_firstName_loc, send_keys)

    def register_last_name(self, *, send_keys):
        # return self.driver.find_element(*self.__register_lastName_loc)
        # return self.find_element(self.__register_lastName_loc)
        return self.enter_text_into_element(self.__register_lastName_loc, send_keys)

    def register_email(self, *, send_keys):
        # return self.driver.find_element(*self.__register_email_loc)
        # return self.find_element(self.__register_email_loc)
        return self.enter_text_into_element(self.__register_email_loc, send_keys)

    def register_telephone(self, *, send_keys):
        # return self.driver.find_element(*self.__register_telephone_loc)
        # return self.find_element(self.__register_telephone_loc)
        return self.enter_text_into_element(self.__register_telephone_loc, send_keys)

    def register_password(self, *, send_keys):
        # return self.driver.find_element(*self.__register_password_loc)
        # return self.find_element(self.__register_password_loc)
        return self.enter_text_into_element(self.__register_password_loc, send_keys)

    def register_confirm_password(self, *, send_keys):
        # return self.driver.find_element(*self.__register_confirm_password_loc)
        # return self.find_element(self.__register_confirm_password_loc)
        return self.enter_text_into_element(self.__register_confirm_password_loc, send_keys)

    def register_click_on_privacy_policy(self):
        # return self.driver.find_element(*self.__register_privacy_policy_loc)
        # return self.find_element(self.__register_privacy_policy_loc)
        self.click_element(self.__register_privacy_policy_loc)

    def register_continue_button_loc(self):
        # self.driver.find_element(*self.__register_continue_button_loc).click()
        self.click_element(self.__register_continue_button_loc)
        newAccountPage = NewAccountCreatedPageObjects(self.driver)
        return newAccountPage

    def newsletter_click_YES(self):
        # return self.driver.find_element(*self.__register_newsletter_yes_loc)
        # return self.find_element(self.__register_newsletter_yes_loc)
        return self.click_element(self.__register_newsletter_yes_loc)

    def newsletter_click_NO(self):
        # return self.driver.find_element(*self.__register_newsletter_no_loc)
        # return self.find_element(self.__register_newsletter_no_loc)
        return self.click_element(self.__register_newsletter_no_loc)

    def first_name_error_message(self):
        return self.get_element_text(self.__register_firstName_error_message)
        # return self.find_element(self.__register_firstName_error_message)

    def last_name_error_message(self):
        return self.get_element_text(self.__register_lastName_error_message)
        # return self.find_element(self.__register_lastName_error_message)

    def email_error_message(self):
        return self.get_element_text(self.__register_email_error_message)
        # return self.find_element(self.__register_email_error_message)

    def telephone_error_message(self):
        return self.get_element_text(self.__register_telephone_error_message)
        # return self.find_element(self.__register_telephone_error_message)

    def password_error_message(self):
        return self.get_element_text(self.__register_password_error_message)
        # return self.find_element(self.__register_password_error_message)

    def privacy_policy_error_message(self):
        return self.get_element_text(self.__register_privacy_policy_error_message)
        # return self.find_element(self.__register_privacy_policy_error_message)

    def confirm_password_error_message(self):
        return self.get_element_text(self.__register_confirm_password_error_message)
        # return self.find_element(self.__register_confirm_password_error_message)
