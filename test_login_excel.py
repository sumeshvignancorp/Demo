import time
from datetime import datetime

import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Utilities import ExcelReader

excel_path = "ExcelFiles/Ajnaviewlogindata.xlsx"
workbook = openpyxl.load_workbook(excel_path)
sheet = workbook.active


@pytest.mark.parametrize('execution_number', range(5))
def run_multiple_times(execution_number):
    assert True


@pytest.mark.parametrize("username,password",
                         ExcelReader.get_data_from_excel("ExcelFiles/Ajnaviewlogindata.xlsx", "LoginTest"))
def test_login_valid_credentials(username, password):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://pg.ajnaview.net/')
    time.sleep(5)
    driver.find_element("name", "email").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath", "(//button[@type='button'])[2]").click()  # Login Button
    print("Title :", driver.title)
    time.sleep(10)
    driver.close()

