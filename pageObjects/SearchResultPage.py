from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class SearchResultPageObjects(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __result_products = (By.XPATH, "//div[@class='product-thumb']//img")
    __no_product_search_criteria = (By.XPATH, "//input[@id='button-search']/following-sibling::p")

    def searched_product_displayed(self, product_name):
        # products = self.driver.find_elements(*self.__result_products)

        products = self.find_element(self.__result_products, multiple=True)

        specified_name = product_name.casefold()

        for product in products:
            title = product.get_attribute("title").casefold()
            if product.is_displayed() and (
                    specified_name in title or title.startswith(specified_name) or title.endswith(specified_name)):
                return True
        return False

    def no_product_search_criteria(self):

        # criteria_message = self.driver.find_element(*self.__no_product_search_criteria)

        criteria_message = self.find_element(self.__no_product_search_criteria)

        # "There is no product that matches the search criteria."
        if criteria_message.is_displayed():
            return True
        return False
