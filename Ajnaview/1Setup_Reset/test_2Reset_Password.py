import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_reset_password1():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://tracking.ontrack-telematics.co.uk/")
    driver.refresh()
    driver.find_element("xpath", "//a[text()='Reset Password']").click()
    time.sleep(3)
    driver.find_element("name", "email").send_keys("sumeshhiremath13@gmail.com")
    driver.find_element("xpath", "//button[@type='button']").click()
    time.sleep(2)
    print("Url : ", driver.current_url)
    driver.get_screenshot_as_file("../Results&Status/2Reset password success.png")
    driver.quit()
