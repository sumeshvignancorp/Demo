import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_swap_search():
    # driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://tracking.ontrack-telematics.co.uk/")
    driver.find_element("name", "email").send_keys("sumeshhiremath13@gmail.com")
    driver.find_element("name", "password").send_keys("Ajnaview@13")
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()  # Login Button
    driver.find_element("xpath", "(//button[@role='tab'])[2]").click()
    time.sleep(3)
    driver.find_element("xpath", "(//button[@role='tab'])[1]").click()
    time.sleep(3)
    driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("Test")
    time.sleep(2)
    driver.get_screenshot_as_file("../Results&Status/10Search device.png")
    driver.find_element("xpath", "//button[@aria-label='Close']").click()
    driver.get_screenshot_as_file("../Results&Status/11close device list.png")
    time.sleep(3)
    driver.quit()
