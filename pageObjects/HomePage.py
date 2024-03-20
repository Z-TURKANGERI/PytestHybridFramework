from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.LoginPage import LoginPageObjects
from pageObjects.RegisterPage import RegisterPageObjects
from pageObjects.SearchResultPage import SearchResultPageObjects


class HomePageObjects(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __account_drop_down_loc = (By.CSS_SELECTOR, "[title='My Account']")
    __register_to_account_loc = (By.LINK_TEXT, "Register")
    __login_to_account_loc = (By.LINK_TEXT, "Login")
    __search_box_filed_loc = (By.NAME, "search")
    __search_button_loc = (By.XPATH, "//div[@id='search']//button")

    def account_drop_down(self):
        # return self.driver.find_element(*self.__account_drop_down_loc).click()

        return self.click_element(*self.__account_drop_down_loc)



    def click_on_account_drop_down_and_click_on_logic(self):
        # self.driver.find_element(*self.__account_drop_down_loc).click()
        # self.driver.find_element(*self.__login_to_account_loc).click()

        self.click_element(self.__account_drop_down_loc)
        self.click_element(self.__login_to_account_loc)

        loginPage = LoginPageObjects(self.driver)
        return loginPage

    def click_on_account_drop_down_and_click_on_register(self):
        # self.driver.find_element(*self.__account_drop_down_loc).click()
        # self.driver.find_element(*self.__register_to_account_loc).click()

        self.click_element(self.__account_drop_down_loc)
        self.click_element(self.__register_to_account_loc)

        registerPage = RegisterPageObjects(self.driver)
        return registerPage

    def search_box_field(self):
        # return self.driver.find_element(*self.__search_box_filed_loc)
        return self.find_element(self.__search_box_filed_loc)


    def search_button(self):
        # self.driver.find_element(*self.__search_button_loc).click()

        self.click_element(self.__search_button_loc)

        searchResult = SearchResultPageObjects(self.driver)
        return searchResult
