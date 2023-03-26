import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://google.com/")

size=driver.find_element(By.LINK_TEXT,"Gmail").size
print(size)
loc=driver.find_element(By.LINK_TEXT,"Gmail").location
print(loc)

print(driver.get_window_size())

print(len(driver.find_elements(By.XPATH, "//*[@id='123']")))

# presence or not by using count - then doing operation
# elements=driver.find_elements(By.XPATH,"//a[text()='Gmail']")
# print(len(elements))

# will check for visiblity - element should be present (count>0)
# print(driver.find_element(By.XPATH,"//a[text()='Gmail']").is_displayed())

# presence
if len(driver.find_elements(By.XPATH,"//a[text()='Gmail']"))>0:
    #visibility
    if driver.find_element(By.XPATH,"//a[text()='Gmail']").is_displayed():
        driver.find_element(By.XPATH, "//a[text()='Gmail']").click()

# element should be present and then move forward
wait=WebDriverWait(driver,20)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//a[text()='BALA']")))


#presence
# print(len(driver.find_elements(By.XPATH,"//a[text()='Members Listing']")))

#check for visiblity so element should be  present
# print(driver.find_element(By.XPATH,"//a[text()='Members Listing']").is_displayed() )
#
# time.sleep(5)
# driver.quit()