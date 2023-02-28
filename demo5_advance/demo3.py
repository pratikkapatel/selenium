import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.google.com/")

actions = webdriver.ActionChains(driver)
actions.key_down(webdriver.Keys.SHIFT)\
    .send_keys("hello world").key_up(webdriver.Keys.SHIFT).pause(1)\
    .send_keys(webdriver.Keys.ARROW_DOWN).send_keys(webdriver.Keys.ARROW_DOWN)\
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1).send_keys(webdriver.Keys.ENTER).perform()

#actions.send_keys(webdriver.Keys.F5).perform()
#driver.refresh()
#driver.back()
#driver.forward()

time.sleep(5)
driver.quit()
