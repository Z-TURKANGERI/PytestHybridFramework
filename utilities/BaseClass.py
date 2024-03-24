from datetime import datetime

import pytest
from faker import Faker

from testData.TestData import TestData


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseClass:
    fake = Faker()
    testData = TestData()

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "zubertest" + time_stamp + "@gmail.com"

    def fake_data(self, first_name=None, last_name=None, email=None, phone_number=None, random_password=None):
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
        elif random_password is not None:
            """Fixture to generate a fake password."""
            # Customize this line as per your requirements for generating a fake password
            return self.fake.password()

    def get_page_title(self, expected_title):
        return self.driver.title == expected_title

    def has_validation_message(self, web_element):
        # Get the validation message attribute from the web element
        validation_message = web_element.get_attribute("validationMessage")

        # If a validation message exists, return True; otherwise, return False
        return validation_message is not None

    def has_validation_message_using_javascript(self, web_element):
        # Execute JavaScript to get the validation message attribute from the web element
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", web_element)

        # If a validation message exists and it's not empty, return True; otherwise, return False
        return validation_message and validation_message.strip() != ""

    def get_text_of_filed(self, locator):
        return locator.text

    # def get_page_title1(self, expected_title):
    #     count = 0
    #     page_title = self.driver.title
    #
    #     while (page_title != expected_title) and count<=10:
    #         count += 1
    #         page_title = self.driver.title
