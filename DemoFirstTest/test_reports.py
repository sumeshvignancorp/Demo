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
    driver.find_element("xpath", "(//div[@role='button'])[3]").click()  # reports
    driver.find_element("xpath", "(//a[@tabindex='0'])[3]").click()  # route
    time.sleep(5)

    driver.refresh()
    drop = Select(driver.find_element("xpath", "(//input[@tabindex='-1'])[1]"))  # dropdown for device
    drop.select_by_index(2)

    drop = Select(driver.find_element("xpath", "(//div[@tabindex='0'])[12]"))  # PERIOD
    drop.select_by_index(1)
    time.sleep(5)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @class='button']")))
    Next = driver.find_element_by_xpath("//input[@type='button' and @class='button']")
    Next.click()
    driver.find_element("xpath", "(// button[@ type='button'])[3]").click()  # show
    time.sleep(5)

    # driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()  # dropdown for device
    # time.sleep(5)
    # driver.find_element("xpath", "(//li[@role='option'])[1]").click()  # item click
    # time.sleep(5)

    # wait = WebDriverWait(driver, 10)
    # button = wait.until(EC.element_to_be_clickable((By.XPATH, "(// button[@ type='button'])[3]")))
    # button.click()

    # driver.get_screenshot_as_file("report_page.png")
    # drop = Select(driver.find_element("xpath", "(//input[@tabindex='-1'])[1]"))
    # drop.select_by_index(2)

    # driver.find_element("xpath", "//div[@role='combobox'][1]").click() # dropdown
