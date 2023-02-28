import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

d = webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(5)
d.get("https://www.sodapdf.com/pdf-to-word/")
d.find_element(By.XPATH,"//input[@type='file']").send_keys(r"D:\Pratik Profiles\Pratik_Patel_QA_10+Years_exp.pdf")

time.sleep(5)
d.quit()