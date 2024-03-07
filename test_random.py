import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.mark.parametrize("i", range(5))
def test_random():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://pg.ajnaview.net/')
    time.sleep(5)
    driver.find_element("name", "email").send_keys(generate_email_with_time_stamp())
    print(generate_email_with_time_stamp())
    driver.find_element("name", "password").send_keys("Ajnaview@13")
    # assert test_random() == 5
    time.sleep(2)
    # driver.get_screenshot_as_file("generate_email_with_time_stamp().png")
    # driver.find_element("xpath", "(//button[@type='button'])[2]").click()  # Login Button
    print("Title :", driver.title)
    # time.sleep(10)
    # driver.close()


def generate_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%H_%M_%S")  # "%Y_%m_%d_%H_%M_%S"
    return "Test" + time_stamp + "@gmail.com"
