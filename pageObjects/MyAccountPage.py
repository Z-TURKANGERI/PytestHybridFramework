from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class MyAccountPageObjects(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __my_account_info_loc = (By.XPATH, "//h2[text()='My Account']")

    def my_account_info(self):
        # return self.driver.find_element(*self.__my_account_info_loc)

        return self.find_element(self.__my_account_info_loc)
