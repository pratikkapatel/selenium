import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://nasscom.in/")

#presence
print(len(driver.find_elements(By.XPATH,"//a[normalize-space()='Members Listing']")))

actions=webdriver.ActionChains(driver)
actions.move_to_element(driver.find_element(By.XPATH,"//a[@class='nav-link dropdown-toggle'][normalize-space()='Membership']")).perform()
#check visibility
print(driver.find_element(By.XPATH,"//a[normalize-space()='Members Listing']").is_displayed())

time.sleep(5)
driver.quit()