import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_view():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(5)
    driver.find_element("name", "email").send_keys("sumesh@vignancorp.com")
    driver.find_element("name", "password").send_keys("ajNa785#")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()

    # Add_device
    driver.find_element("xpath", "(//button[@type='button'])[5]").click()
    time.sleep(5)
    # Device_details
    driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("GPS")

    driver.find_element("xpath", "(//input[@type='text'])[2]").send_keys("5478765455")

    driver.find_element("xpath", "(//input[@type='text'])[3]").send_keys("FM00012")

    time.sleep(5)

    # drop = Select(driver.find_element("xpath", "(//div[@role='combobox'])[1]"))
    # drop.select_by_visible_text("Car")
    # time.sleep(5)
    #drop = Select(driver.find_element("xpath", "(//div[@role='combobox'])[1]"))

    driver.find_element("xpath", "(//input[@type='text'])[4]").send_keys("user")

    driver.find_element("xpath", "(//input[@type='text'])[5]").send_keys("8985969855")
    time.sleep(3)
    # Vehicle details
    driver.find_element("xpath", "(//input[@type='text'])[6]").send_keys("23455")
    driver.find_element("xpath", "(//input[@type='text'])[7]").send_keys("KA01ZX0099")
    time.sleep(3)
    # FuelInfo
    # drop2 = Select(driver.find_element("xpath", "(//div[@role='button'])[2]"))
    # drop2.select_by_visible_text('petrol')

    driver.find_element("xpath", "(//input[@type='number'])[1]").send_keys("102")

    driver.find_element("xpath", "(//input[@type='number'])[2]").send_keys("45")

    driver.find_element("xpath", "(//input[@type='number'])[3]").send_keys("20")
    time.sleep(5)
    driver.find_element("xpath", "(//input[@type='text'])[8]").send_keys("12345")

    driver.find_element("xpath", "(//input[@type='text'])[9]").send_keys("12345")

    driver.find_element("xpath", "(//input[@type='text'])[10]").send_keys("Jio")

    driver.find_element("xpath", "(//input[@type='date'])[2]").send_keys("01062023")

    driver.find_element("xpath", "(//input[@type='date'])[3]").send_keys("01012024")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[6]").click()
    time.sleep(6)
    driver.quit()
