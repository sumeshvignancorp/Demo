import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_summary():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://tracking.ontrack-telematics.co.uk/")
    time.sleep(5)
    driver.find_element("name", "email").send_keys("sumeshhiremath13@gmail.com")
    driver.find_element("name", "password").send_keys("Ajnaview@13")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    driver.find_element("xpath", "(//div[@role='button'])[3]").click()  # reports
    driver.find_element("xpath", "(//a[@tabindex='0'])[7]").click()  # summary
    time.sleep(5)
    driver.find_element("xpath", "(//div[@role='combobox'])[3]").click()
    time.sleep(2)
    driver.find_element("xpath", "//li[@data-value='thisWeek']").click()
    # print("Title :", driver.title)
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()
    time.sleep(3)
    driver.find_element("xpath", "//li[@data-value='4']").click()
    time.sleep(4)
    print("Title :", driver.title)
    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "(//button[@type='button'])[3]")
    actions.click(demo).perform()
    time.sleep(3)
    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "(//button[@type='button'])[3]")
    actions.click(demo).perform()
    driver.find_element("xpath", "(//button[@type='button'])[4]").click()
    time.sleep(3)
    print("Summary Report Exported :", driver.title)
    driver.get_screenshot_as_file("../Results&Status/Summary_Report.png")
    time.sleep(2)
    driver.quit()
