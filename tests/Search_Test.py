from pageObjects.HomePage import HomePageObjects
from utilities.BaseTest import BaseClass


class TestSearch(BaseClass):
    def test_search_for_a_valid_product(self):
        homePage = HomePageObjects(self.driver)
        homePage.search_box_field().send_keys("mac")
        searchResult = homePage.search_button()

        assert searchResult.searched_product_displayed("mac"), "product is not present"

    def test_search_for_a_invalid_product(self):
        homePage = HomePageObjects(self.driver)
        homePage.search_box_field().send_keys("Honda")
        searchResult = homePage.search_button()
        assert searchResult.no_product_search_criteria()

    def test_search_for_a_without_product(self):
        homePage = HomePageObjects(self.driver)
        searchResult = homePage.search_button()
        assert searchResult.no_product_search_criteria()
