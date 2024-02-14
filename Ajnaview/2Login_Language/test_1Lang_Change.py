import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_language():
    # driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@role='combobox']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//li[@role='option'][4]").click()
    time.sleep(2)
    driver.get_screenshot_as_file("../Results&Status/3Language change.png")
    time.sleep(2)
    driver.quit()
