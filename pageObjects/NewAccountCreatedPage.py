from selenium.webdriver.common.by import By


class NewAccountCreatedPageObjects:

    def __init__(self, driver):
        self.driver = driver

    __account_confirm = (By.XPATH, "//p[contains(text(),'Congratulations! Your new account has been success')]")

    def new_account_created_message(self):
        return self.driver.find_element(*self.__account_confirm)
