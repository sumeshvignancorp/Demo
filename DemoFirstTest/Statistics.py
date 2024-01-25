import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_report():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    driver.implicitly_wait(20)
    time.sleep(3)
    driver.find_element("name", "email").send_keys("sumesh@vignancorp.com")
    driver.find_element("name", "password").send_keys("Sumesh@123")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    time.sleep(10)
    driver.find_element("xpath", "(//div[@role='button'])[4]").click()
    time.sleep(3)
    print("Title :", driver.title)
