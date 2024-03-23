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

    def get_page_title(self, expected_title):
        return self.driver.title == expected_title

    # def get_page_title1(self, expected_title):
    #     count = 0
    #     page_title = self.driver.title
    #
    #     while (page_title != expected_title) and count<=10:
    #         count += 1
    #         page_title = self.driver.title



