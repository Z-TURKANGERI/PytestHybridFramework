
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

