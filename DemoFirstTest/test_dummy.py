import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_language():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(3)
    # drop = Select(driver.find_element(By.XPATH, "//*[contains(text(),='English']")) #language
    # drop = Select(driver.find_element("xpath", "//*[@id='demo-simple-select']"))
    # drop.select_by_index(3)
    driver.find_element(By.XPATH, "//div[@role='combobox']").click()
    # drop = Select(driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/div/div/div/div/div[2]/div[4]/div/div'))
    # drop.select_by_index(3)
    time.sleep(3)
    driver.find_element(By.XPATH, "//li[@role='option'][4]").click()
    time.sleep(2)
    driver.get_screenshot_as_file("sumesh.png")
    time.sleep(6)
    driver.quit()
