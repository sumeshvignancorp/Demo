import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_connect():
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
    time.sleep(5)
    driver.find_element("xpath", "(//button[@ type='button'])[13]").click()
    driver.find_element("xpath", "(//li[@role='menuitem'])[2]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//input[@type='checkbox'])[2]").click()
    time.sleep(5)
    driver.find_element("xpath", "(//div[@role='button'])[19]").click()
    # driver.find_element("xpath", "(//input[@type='checkbox'])[2]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//div[@role='button'])[20]").click()
    time.sleep(2)
    driver.get_screenshot_as_file("../Results&Status/Associated.png")
    driver.quit()
