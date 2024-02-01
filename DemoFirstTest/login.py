from selenium import webdriver

driver = webdriver.Chrome(r"D:\chromedriver.exe")
driver.get("https://pg.ajnaview.net/")
print(driver.title)
driver.quit()