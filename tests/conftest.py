import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

import configparser
import subprocess

from utilities import ReadConfigurations


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="chrome"
    )
    parser.addoption(
        "--url", action="store", default="https://www.tutorialsninja.com/demo/"
    )


def get_browser_name(request):
    try:
        # Attempt to read configuration from 'basic info' section i.e. from config.ini file
        browser_config = ReadConfigurations.read_configuration("basic info", "browser")
    except configparser.NoSectionError:
        # If 'basic info' section not found, use command-line option
        browser_config = None

    if browser_config:
        return browser_config
    else:
        return request.config.getoption("--browserName")


def get_url(request):
    try:
        # Attempt to read configuration from 'basic info' section i.e. from config.ini file
        url_config = ReadConfigurations.read_configuration("basic info", "url")
    except (configparser.NoSectionError, configparser.NoOptionError):
        # If 'basic info' section or key not found, use default
        url_config = None

    if url_config:
        return url_config
    else:
        return request.config.getoption("--url")


@pytest.fixture(autouse=True)
def setup_and_teardown(request):
    global driver
    driver = None
    # Getting browser_name from get_browser_name method
    browser_name = get_browser_name(request)
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name")
    driver.maximize_window()
    # Getting url from get_url method
    url = get_url(request)
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()


def run_tests_and_generate_report():
    try:
        subprocess.run(["pytest", "--alluredir=./Reports"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running tests: {e}")


if __name__ == "__main__":
    run_tests_and_generate_report()
