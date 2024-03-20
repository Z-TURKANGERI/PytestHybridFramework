from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class NewAccountCreatedPageObjects(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __account_confirm = (By.XPATH, "//p[contains(text(),'Congratulations! Your new account has been success')]")

    def new_account_created_message(self):
        # return self.driver.find_element(*self.__account_confirm)

        return self.find_element(self.__account_confirm)


