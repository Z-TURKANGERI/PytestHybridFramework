from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPageObjects
from pageObjects.RegisterPage import RegisterPageObjects
from pageObjects.SearchResultPage import SearchResultPageObjects


class HomePageObjects:

    def __init__(self, driver):
        self.driver = driver

    __account_drop_down_loc = (By.CSS_SELECTOR, "[title='My Account']")
    __register_to_account_loc = (By.LINK_TEXT, "Register")
    __login_to_account_loc = (By.LINK_TEXT, "Login")
    __search_box_filed_loc = (By.NAME, "search")
    __search_button_loc = (By.XPATH, "//div[@id='search']//button")

    def account_drop_down(self):
        return self.driver.find_element(*self.__account_drop_down_loc).click()

    def click_on_account_drop_down_and_click_on_logic(self):
        self.driver.find_element(*self.__account_drop_down_loc).click()
        self.driver.find_element(*self.__login_to_account_loc).click()
        loginPage = LoginPageObjects(self.driver)
        return loginPage

    def click_on_account_drop_down_and_click_on_register(self):
        self.driver.find_element(*self.__account_drop_down_loc).click()
        self.driver.find_element(*self.__register_to_account_loc).click()
        registerPage = RegisterPageObjects(self.driver)
        return registerPage

    def search_box_field(self):
        return self.driver.find_element(*self.__search_box_filed_loc)

    def search_button(self):
        self.driver.find_element(*self.__search_button_loc).click()
        searchResult = SearchResultPageObjects(self.driver)
        return searchResult
