import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

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


@pytest.fixture(autouse=True)
def setup_and_teardown(request):
    global driver
    driver = None
    browser_name = ReadConfigurations.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name")
    driver.maximize_window()
    url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
