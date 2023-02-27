import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")
#driver.find_element(By.NAME,'fldLoginUserId').send_keys('6777')
driver.find_element(By.XPATH,"//img[@alt='Go']").click()
time.sleep(5)
actual_alert_text= driver.switch_to.alert.text
print(actual_alert_text)

time.sleep(5)
driver.switch_to.alert.accept()

driver.quit()