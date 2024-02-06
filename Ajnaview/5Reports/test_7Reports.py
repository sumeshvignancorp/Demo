import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_report():
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(3)
    driver.find_element("name", "email").send_keys("demo123@gmail.com")
    driver.find_element("name", "password").send_keys("demo123")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    time.sleep(10)
    driver.find_element("xpath", "(//div[@role='button'])[3]").click()  # reports
    driver.find_element("xpath", "(//a[@tabindex='0'])[3]").click()  # route
    time.sleep(5)

    driver.find_element("xpath", "(//div[@role='combobox'])[2]").click() # Period
    time.sleep(3)
    driver.find_element("xpath", "(//li[@data-value='today'])").click()
    time.sleep(3)

    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()  # dropdown for device
    time.sleep(2)
    driver.find_element("xpath", "(//li[@role='option'])[2]").click()  # item click
    time.sleep(4)
    driver.find_element("xpath", "(//a[@tabindex='0'])[3]").click()  # route
    time.sleep(6)
    driver.find_element("xpath", "(//a[@tabindex='0'])[3]").click()
    time.sleep(8)
    driver.find_element("xpath", "(//button[@tabindex='0'])[4]").click()
    # time.sleep(1)
    driver.find_element("xpath", "(//button[@type='button'])[5]").click()
    driver.find_element("xpath", "(//li[@role='menuitem'])[1]").click()
    driver.get_screenshot_as_file("12report_page.png")
    driver.quit()
    # drop = Select(driver.find_element("xpath", "(//input[@tabindex='-1'])[1]"))
    # drop.select_by_index(2)
    # driver.find_element("xpath", "//div[@role='combobox'][1]").click() # dropdown
    # driver.refresh()
    # drop = Select(driver.find_element("xpath", "(//input[@tabindex='-1'])[1]"))  # dropdown for device
    # drop.select_by_index(2)
    # drop = Select(driver.find_element("xpath", "(//div[@tabindex='0'])[12]"))  # PERIOD
    # drop.select_by_index(1)
    # time.sleep(5)
    # driver.find_element("xpath", "(// button[@ type='button'])[3]").click()  # show
    # time.sleep(5)