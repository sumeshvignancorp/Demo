import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_Add_Maintenance():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    driver.find_element("name", "email").send_keys("demo123@gmail.com")
    driver.find_element("name", "password").send_keys("demo123")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    time.sleep(5)

    # Setting click
    driver.find_element("xpath", "(//div[@role='button'])[8]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//a[@tabindex='0'])[8]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[8]").click()
    time.sleep(3)
    driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("tyre ")
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()
    driver.find_element("xpath", "(//li[@role='option'])[2]").click()
    driver.find_element("xpath", "(//input[@type='number'])[1]").send_keys("5001")
    driver.find_element("xpath", "(//input[@type='number'])[2]").send_keys("15000")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@tabindex='0'])[6]").click()
    time.sleep(1)
    driver.get_screenshot_as_file("../Results&Status/8Maintenance added.png")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[5]").click()
    driver.find_element("xpath", "(//button[@type='button'])[11]").click()
    time.sleep(1)
    driver.get_screenshot_as_file("../Results&Status/8Maintenance delete.png")
    driver.quit()

