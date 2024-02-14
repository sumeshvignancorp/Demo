import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_Add_Notification():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(r"D:\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://pg.ajnaview.net/")
    time.sleep(5)
    driver.find_element("name", "email").send_keys("demo123@gmail.com")
    driver.find_element("name", "password").send_keys("demo123")
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()
    time.sleep(5)

    # Setting click
    driver.find_element("xpath", "(//div[@role='button'])[8]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[8]").click()  # Add Notification
    time.sleep(2)
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()
    driver.find_element("xpath", "(//li[@data-value='deviceOverspeed'])[1]").click()
    driver.find_element("xpath", "(//div[@role='combobox'])[2]").click()
    time.sleep(2)
    driver.find_element("xpath", "//li[ @ data-value='mail']").click()
    driver.find_element("xpath", "//li[@data-value='firebase']").click()
    time.sleep(4)
    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "(//button[@type='button'])[4]")
    actions.click(demo).perform()
    time.sleep(3)

    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "(//button[@type='button'])[6]")
    actions.click(demo).perform()
    driver.get_screenshot_as_file("../Results&Status/Add Notification.png")
    time.sleep(1)
    driver.find_element("xpath", "(//button[@type='button'])[5]").click()
    driver.find_element("xpath", "(//button[@type='button'])[11]").click()
    driver.get_screenshot_as_file("../Results&Status/Delete Notification.png")
    time.sleep(2)
    driver.quit()

