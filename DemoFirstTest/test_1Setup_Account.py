import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_new_acc():
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(5)
    driver.refresh()
    driver.find_element("xpath", "(//button[@type='button'])[3]").click()
    time.sleep(5)
    driver.find_element("name", "name").send_keys("Testing")
    driver.find_element("xpath", "//input[@autocomplete='new-email']").send_keys(generate_email_with_time_stamp())
    driver.find_element("xpath", "//input[@autocomplete='new-password']").send_keys("Sqwer@1we")
    driver.find_element("name", "phone").send_keys("012345678")
    time.sleep(5)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    time.sleep(1)
    driver.get_screenshot_as_file("Account created.png")
    time.sleep(2)
    driver.quit()


def generate_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%H_%M_%S")  # "%Y_%m_%d_%H_%M_%S"
    return "Test" + time_stamp + "@gmail.com"
