import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#serv_driver = Service(executable_path=r"C:\Users\JiDi\Downloads\chromedriver_win32 (5)\chromedriver.exe")

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.openemr.io/b/openemr")

driver.find_element(By.ID,"authUser").send_keys("admin")

app_desc=driver.find_element(By.XPATH,"//p[contains(text(),'most')]").text
print(app_desc)

attr=driver.find_element(By.XPATH,"//p[contains(text(),'most')]").get_attribute("class")
print(attr)

href=driver.find_element(By.PARTIAL_LINK_TEXT,"Acknowledgments").get_attribute("href")
print(href)

placeholder=driver.find_element(By.ID,"authUser").get_attribute("placeholder")
print(placeholder)

value=driver.find_element(By.ID,"authUser").get_attribute("value")
print(value)

size=driver.find_element(By.ID,"authUser").size
print(size)

loc=driver.find_element(By.ID,"authUser").location
print(loc)
print(loc['y'])

tagname=driver.find_element(By.ID,"authUser").tag_name
print(tagname)
time.sleep(5)
driver.quit()