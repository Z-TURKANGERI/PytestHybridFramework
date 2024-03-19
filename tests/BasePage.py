from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

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

    def check_display_status_of_element(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.is_displayed()

    def retrieve_element_text(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
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