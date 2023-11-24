import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_dropdown():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(3)

    driver.find_element("xpath", "//div[@role='combobox']").click()
    driver.find_element("xpath", "//input[@value='en']")
    # drop = Select(driver.find_element("xpath", "//input[@value='en']"))
    # drop.select_by_index(3)
    time.sleep(6)
