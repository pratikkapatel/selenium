import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://netbanking.hdfcbank.com/netbanking/")

driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))#Frame xpath

driver.find_element(By.XPATH,"//input[@name='fldLoginUserId']").send_keys("Test11")
driver.find_element(By.LINK_TEXT,'CONTINUE').click()

#main HTML

driver.switch_to.default_content()

time.sleep(5)
driver.quit()