import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_Statistics():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://tracking.ontrack-telematics.co.uk/")
    time.sleep(3)
    driver.find_element("name", "email").send_keys("sumeshhiremath13@gmail.com")
    driver.find_element("name", "password").send_keys("Ajnaview@13")
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    time.sleep(3)
    driver.find_element("xpath", "(//div[@role='button'])[4]").click()  # Statistics
    time.sleep(2)
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()
    driver.find_element("xpath", "//li[@data-value='4']").click()
    driver.find_element("xpath", "(//div[@role='combobox'])[2]").click()
    driver.find_element("xpath", "(//li[@data-value='thisWeek'])").click()
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[4]").click()
    time.sleep(3)
    print("Statistics Report Exported :", driver.title)
    driver.get_screenshot_as_file("../Results&Status/Statistics.png")
    time.sleep(1)
    driver.quit()
