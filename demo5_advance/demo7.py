import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com")

elements=driver.find_elements(By.XPATH,"//a")
print(len(elements))

#href=elements[0].get_attribute("aria-label")
#print(href)

for i in range(0,len(elements)):
    print(i, elements[i].text)
    print(elements[i].get_attribute("href"))
    print(15*'-')