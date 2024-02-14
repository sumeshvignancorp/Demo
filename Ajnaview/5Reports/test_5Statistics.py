import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_Statistics():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(3)
    driver.find_element("name", "email").send_keys("demo123@gmail.com")
    driver.find_element("name", "password").send_keys("demo123")
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    time.sleep(3)
    driver.find_element("xpath", "(//div[@role='button'])[4]").click()  # Statistics
    time.sleep(2)
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()
    driver.find_element("xpath", "//li[@data-value='319']").click()
    driver.find_element("xpath", "(//div[@role='combobox'])[2]").click()
    driver.find_element("xpath", "(//li[@data-value='today'])").click()
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[4]").click()
    time.sleep(3)
    driver.get_screenshot_as_file("../Results&Status/Statistics.png")
    time.sleep(1)
    driver.quit()
