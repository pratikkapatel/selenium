import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.online.citibank.co.in/")

#driver.find_element(By.XPATH,"//a[@title='close']").click()
#print(len(driver.find_element(By.XPATH,"//a[@title='close']")))

print(driver.find_element(By.XPATH,"//a[@href='/press-room/citi-in-india.htm?eOfferCode=INHOGNTHEABOUS']").is_displayed())

if len(driver.find_elements(By.XPATH,"//a[@title='close']"))>0:
    driver.find_element(By.XPATH, "//a[@title='close']").click()

time.sleep(5)
driver.quit()