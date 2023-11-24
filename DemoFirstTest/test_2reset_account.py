import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_reset_password():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(5)
    driver.find_element("xpath", "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]").click()
    time.sleep(5)
    driver.find_element("name", "email").send_keys("demo3@gmail.com")
    driver.find_element("xpath", "//button[@type='button']").click()
    time.sleep(5)
    driver.quit()
