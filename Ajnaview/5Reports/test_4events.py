import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_events():
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
    driver.find_element("xpath", "(//div[@role='button'])[3]").click()  # reports
    driver.find_element("xpath", "(//a[@tabindex='0'])[4]").click()  # events
    time.sleep(5)
    print("Title :", driver.title)
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()
    time.sleep(3)
    driver.find_element("xpath", "//li[@data-value='319']").click()
    time.sleep(4)
    driver.find_element("xpath", "(//div[@role='combobox'])[2]").click()
    time.sleep(2)
    driver.find_element("xpath", "//li[@data-value='today']").click()
    time.sleep(2)
    print("Title :", driver.title)
    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "(//button[@type='button'])[4]")
    actions.click(demo).perform()
    time.sleep(5)
    driver.get_screenshot_as_file("../Results&Status/Events_Report.png")
    time.sleep(2)
    driver.quit()
