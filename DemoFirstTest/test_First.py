import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_login_valid_credentials():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(5)
    driver.find_element("name", "email").send_keys("sumesh@vignancorp.com")
    driver.find_element("name", "password").send_keys("ajNa785#")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()  # Login Button
    print("Title :", driver.title)
    time.sleep(10)
    driver.get_screenshot_as_file("screenshot.png")
    driver.find_element("xpath", "(//div[@role='button'])[11]").click()
    time.sleep(6)
    driver.quit()


def test_login_invalid_credentials():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(5)
    print("Title 3 :", driver.title)
    time.sleep(2)
    driver.find_element("name", "email").send_keys(generate_email_with_time_stamp())
    driver.find_element("name", "password").send_keys(generate_email_with_time_stamp())
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()  # Login_button
    print("Title 4 :", driver.title)
    time.sleep(6)
    driver.quit()


def test_login_empty_credentials():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(5)
    driver.find_element("name", "email").send_keys("")
    driver.find_element("name", "password").send_keys("")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    print("Title :", driver.title)
    time.sleep(6)
    driver.quit()


def generate_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%H_%M_%S")  # "%Y_%m_%d_%H_%M_%S"
    return "Ab" + time_stamp + "@gmail.com"
