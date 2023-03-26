import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


serv=Service(executable_path=r"C:\Users\JiDi\Downloads\chromedriver_win32 (5)\chromedriver.exe")
opt=webdriver.ChromeOptions()

driver = webdriver.Chrome(service=serv,options=opt)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://netbanking.hdfcbank.com/netbanking/")

# //frame[contains(@src,'RSNBLogin')]
driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))

#enter userid as test123
driver.find_element(By.NAME,"fldLoginUserId").send_keys("test123")
driver.find_element(By.LINK_TEXT,"").click()

#switch to main html
driver.switch_to.default_content()



time.sleep(5)
driver.quit()