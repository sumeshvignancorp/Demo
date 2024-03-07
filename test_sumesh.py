import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    # Initialize the Chrome browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(browser):
    # Navigate to the webpage
    browser.get("https://pg.ajnaview.net/")
    time.sleep(2)
    browser.find_element("name", "email").send_keys(generate_email_with_time_stamp())
    # print(generate_email_with_time_stamp())
    print(generate_email_with_time_stamp())
    browser.find_element("name", "password").send_keys("Sum")


@pytest.mark.parametrize("i", range(2))
def test_device(browser, login, i):
    time.sleep(2)
    browser.find_element("xpath", "//a[text()='Reset Password']").click()
    time.sleep(3)
    browser.find_element("xpath", "(// button[@ type='button'])[2]").click()
    time.sleep(1)

    # assert test_device(browser, login, i) == 1


def generate_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%H_%M_%S")  # "%Y_%m_%d_%H_%M_%S"
    return "Test" + time_stamp + "@gmail.com"
