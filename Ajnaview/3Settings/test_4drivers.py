import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_Add_Driver():
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
    time.sleep(5)

    # Setting click
    driver.find_element("xpath", "(//div[@role='button'])[7]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//a[@tabindex='0'])[5]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[11]").click()
    time.sleep(3)
    driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("Driver")
    driver.find_element("xpath", "(//input[@type='text'])[2]").send_keys("KA01")
    driver.find_element("xpath", "(//input[@type='text'])[3]").send_keys("45673443")
    driver.find_element("xpath", "(//button[@type='button'])[5]").click()
    time.sleep(1)
    driver.get_screenshot_as_file("../Results&Status/8Driver added.png")
    time.sleep(4)
    driver.find_element("xpath", "(//button[@type='button'])[8]").click()
    driver.find_element("xpath", "(//button[@type='button'])[14]").click()
    driver.get_screenshot_as_file("../Results&Status/8.1Driver deleted.png")
    time.sleep(2)
    driver.quit()

