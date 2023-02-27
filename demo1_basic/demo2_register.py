import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.implicitly_wait(5)
driver.find_element(By.NAME,"firstname").send_keys('Tobi')
driver.find_element(By.NAME,"lastname").send_keys('Mylan')
driver.find_element(By.NAME,"reg_email__").send_keys("tobi.mylan2@gmail.com")
driver.find_element(By.NAME,"reg_passwd__").send_keys("tobi@2020")
driver.implicitly_wait(5)
select_day=Select(driver.find_element(By.NAME,"birthday_day"))
select_day.select_by_visible_text('18')

select_month=Select(driver.find_element(By.ID,"month"))
select_month.select_by_visible_text('Aug')

select_year=Select(driver.find_element(By.ID,"year"))
select_year.select_by_visible_text('1988')

driver.find_element(By.XPATH,"//label[text()='Custom']").click()
driver.find_element(By.LINK_TEXT,"Sign Up").click()
time.sleep(20)
print("program executed")
#driver.quit()


