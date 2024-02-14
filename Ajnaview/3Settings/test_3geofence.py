import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_Add_Geofence():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(5)
    driver.find_element("name", "email").send_keys("demo123@gmail.com")
    driver.find_element("name", "password").send_keys("demo123")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()

    # Setting click
    driver.find_element("xpath", "(//div[@role='button'])[8]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//a[@tabindex='0'])[3]").click()
    time.sleep(3)
    driver.find_element("xpath", "(//button[@ title='Marker tool (m)'])").click()
    time.sleep(1)
    driver.find_element("xpath", "//canvas[@role='region']").click()
    time.sleep(3)
    driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("Test_School")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[6]").click()
    time.sleep(2)
    driver.get_screenshot_as_file("../Results&Status/Add Geofence.png")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[21]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[22]").click()
    time.sleep(1)
    driver.get_screenshot_as_file("../Results&Status/Delete Geofence.png")
    time.sleep(3)
    driver.quit()