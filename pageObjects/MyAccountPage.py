from selenium.webdriver.common.by import By


class MyAccountPageObjects:

    def __init__(self, driver):
        self.driver = driver

    __my_account_info_loc = (By.XPATH, "//h2[text()='My Account']")

    def my_account_info(self):
        return self.driver.find_element(*self.__my_account_info_loc)
