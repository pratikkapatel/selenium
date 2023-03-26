import time

from selenium import webdriver
from selenium.common import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serv_driver = Service(executable_path=r"C:\Users\JiDi\Downloads\chromedriver_win32 (5)\chromedriver.exe")

driver = webdriver.Chrome(service=serv_driver)
driver.maximize_window()

driver.get("https://www.google.com")  # wait for page load to complete

# fluent wait
# wait = WebDriverWait(driver=driver, timeout=25, poll_frequency=1,
#                      ignored_exceptions=(NoSuchElementException, InvalidSelectorException))

wait = WebDriverWait(driver=driver,
                     timeout=25,
                     # poll_frequency=1,
                     ignored_exceptions=(Exception))


wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@name='q'"))).send_keys('hello')


wait.until(expected_conditions.alert_is_present()).accept()

is_available=wait.until(expected_conditions.title_is('Google'))
print(is_available)
time.sleep(5)
driver.quit()

# click on create new account
# driver.find_element(By.LINK_TEXT, "Create new account").click()

# driver.find_element(By.NAME, "firstname").send_keys("bala")
