import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
driver.find_element(By.NAME,"UserFirstName").send_keys("John")
driver.find_element(By.NAME,"UserEmail").send_keys("John@gmail.com")

driver.implicitly_wait(5)
select_job=Select(driver.find_element(By.NAME,"UserTitle"))
select_job.select_by_visible_text('IT Manager')
driver.implicitly_wait(5)
select_Emp=Select(driver.find_element(By.NAME,"CompanyEmployees"))
select_Emp.select_by_visible_text('101 - 500 employees')

select_country=Select(driver.find_element(By.NAME,"CompanyCountry"))
select_country.select_by_visible_text('India')


driver.find_element(By.CLASS_NAME,"checkbox-ui").click() #Xpath: //tagname[@attribute=''] or /tagname[text()='']
driver.find_element(By.NAME,'start my free trial').click()

#actual_error=driver.find_element(By.XPATH,'//span[contains(text(),'Enter your')]').text
time.sleep(20)
driver.quit()