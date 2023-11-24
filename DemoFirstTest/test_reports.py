import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_report():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(3)
    driver.find_element("name", "email").send_keys("sumesh@vignancorp.com")
    driver.find_element("name", "password").send_keys("ajNa785#")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    time.sleep(5)

    driver.find_element("xpath", "(//div[@role='button'])[3]").click() # reports
    driver.find_element("xpath", "(//a[@tabindex='0'])[2]").click() # combined
    driver.refresh()
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click() # dropdown
    time.sleep(5)
    driver.find_element("xpath", "//li[@role='option'][1]").click() # item click
    # driver.find_element("xpath", "(//div[@role='combobox'])[2]").click() # PERIOD
    time.sleep(3)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    time.sleep(5)
    driver.get_screenshot_as_file("report_page.png")
    time.sleep(4)
    # drop = Select(driver.find_element("xpath", "(//input[@tabindex='-1'])[1]"))
    # drop.select_by_index(2)

    # driver.find_element("xpath", "//div[@role='combobox'][1]").click() # dropdown

