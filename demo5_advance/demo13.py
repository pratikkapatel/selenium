import time

from selenium import webdriver
from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com/")  # wait for page load to complete

#fluent wait
wait = WebDriverWait(driver=driver, timeout=20, poll_frequency=1,
                     ignored_exceptions=[Exception])

wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Create new account"))).click()

wait.until(expected_conditions.visibility_of_element_located((By.NAME, "firstname"))).send_keys('king')

time.sleep(5)
driver.quit()

# click on create new account
# driver.find_element(By.LINK_TEXT, "Create new account").click()

# driver.find_element(By.NAME, "firstname").send_keys("bala")