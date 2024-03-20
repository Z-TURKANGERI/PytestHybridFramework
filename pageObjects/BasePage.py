from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, multiple=False):
        """
        Locate and return element(s) based on the locator.

        Args:
            locator (tuple): A tuple containing the locator strategy and value.
            multiple (bool, optional): If False, find the first matching element. Defaults to True.

        Returns:
            WebElement or list of WebElements: The located element(s) or None if not found.
        """
        try:
            if multiple:
                elements = self.driver.find_elements(*locator)
                return elements if elements else None
            else:
                element = self.driver.find_element(*locator)
                return element if element else None
        except Exception as e:
            print(f"An error occurred while locating the element(s): {e}")
            return None

    def is_element_displayed(self, locator):
        element = self.find_element(locator)
        return element.is_displayed()

    def click_element(self, locator):
        if self.is_element_displayed(locator):
            element = self.find_element(locator)
            element.click()
        else:
            print("Element is not displayed, cannot click.")

    def enter_text_into_element(self, locator, text):
        self.click_element(locator)
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        return self.find_element(locator).text


"""
    def get_element(self, by_locator=None, locator_name=None, locator_value=None):
        element = None
        if by_locator is not None:
            element = self.driver.find_element(by_locator)
        elif by_locator is None:
            if locator_name.endswith("_id"):
                element = self.driver.find_element(By.ID, locator_value)
            elif locator_name.endswith("_name"):
                element = self.driver.find_element(By.NAME, locator_value)
            elif locator_name.endswith("_class_name"):
                element = self.driver.find_element(By.CLASS_NAME, locator_value)
            elif locator_name.endswith("_link_text"):
                element = self.driver.find_element(By.LINK_TEXT, locator_value)
            elif locator_name.endswith("_xpath"):
                element = self.driver.find_element(By.XPATH, locator_value)
            elif locator_name.endswith("_css"):
                element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def type_into_element(self, locator, text):
        element = self.get_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, by_locator=None, locator_name=None, locator_value=None):
        element = None
        if by_locator is not None:
            element = self.get_element(by_locator)
        elif by_locator is None:
            element = self.get_element(locator_name, locator_value)
        element.click()

    def check_display_status_of_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

    def retrieve_element_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text

    '''
    def wait_for_elements_to_be_displayed(self, by_locator=None, how=None, path=None, timeout=60):
        element = None
        if by_locator is not None:
            element = by_locator
        elif how == "id" or how == By.ID:
            element = By.ID, path
        elif how == "xpath" or how == By.XPATH:
            element = By.XPATH, path

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(element))
        except (StaleElementReferenceException, TimeoutException):
            print("wait for element to be displayed time out or element was stale in the DOM")

    '''
"""
