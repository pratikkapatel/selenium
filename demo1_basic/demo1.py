import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.ID,"email").send_keys("tobi.mylan2@gmail.com")
driver.find_element(By.NAME,"pass").send_keys("pratikp111")
driver.find_element(By.NAME,"login").click()

time.sleep(5)
print(driver.title)
driver.quit()

