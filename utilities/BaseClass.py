from datetime import datetime

import pytest
from faker import Faker


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseClass:
    fake = Faker()

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "zubertest" + time_stamp + "@gmail.com"

    def fake_data(self, first_name=None, last_name=None, email=None, phone_number=None):
        if first_name is not None:
            """Fixture to generate a fake first name."""
            return self.fake.first_name()
        elif last_name is not None:
            """Fixture to generate a fake last name."""
            return self.fake.last_name()
        elif email is not None:
            """Fixture to generate a fake email."""
            return self.fake.email()
        elif phone_number is not None:
            """Fixture to generate a fake phone number."""
            return self.fake.phone_number()


    def type_into_element14(self, locator_method, text):
        element = locator_method
        element.click()
        element.clear()
        element.send_keys(text)

    def type_into_element(self, locator_method, text):
        locator_method.send_keys(text)

        # element = locator_method
        # element.click()
        # element.clear()
        # element.send_keys(text)

    def click_on_element(self, locator_method):
        element = locator_method
        element.click()

    def check_display_status_of_element(self, locator_method):
        element = locator_method
        return element.is_displayed()

    def retrieve_element_text(self, locator_method):
        element = locator_method
        return element.text
