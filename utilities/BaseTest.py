from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseClass:

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "zubertest" + time_stamp + "@gmail.com"

    def type_into_element(self, locator_method, text):
        element = locator_method
        element.click()
        element.clear()
        element.send_keys(text)

    def click_on_element(self, locator_method):
        element = locator_method
        element.click()

    def check_display_status_of_element(self, locator_method):
        element = locator_method
        return element.is_displayed()

    def retrieve_element_text(self, locator_method):
        element = locator_method
        return element.text
