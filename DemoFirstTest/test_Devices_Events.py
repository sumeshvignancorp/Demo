import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_login_valid_credentials():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    driver.find_element("name", "email").send_keys("sumesh@vignancorp.com")
    driver.find_element("name", "password").send_keys("Sumesh@123")
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()  # Login Button
    driver.find_element("xpath", "(//button[@role='tab'])[2]").click()
    time.sleep(3)
    driver.find_element("xpath", "(//button[@role='tab'])[1]").click()
    time.sleep(3)
    driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("test")
    time.sleep(5)
    driver.find_element("xpath", "(//button[@type='button'])[6]").click();
    time.sleep(8)
    driver.quit()
