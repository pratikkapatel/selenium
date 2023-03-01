import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt=webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
opt.accept_insecure_certs
#opt.add_argument("--headless")

dic_pref={"download.default_directory":r"D:\Smalls"}
opt.add_experimental_option("prefs",dic_pref)

driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.selenium.dev/downloads")
print(driver.title)

driver.find_element(By.XPATH,"//a[normalize-space()='32 bit Windows IE']").click()

time.sleep(15)
driver.quit()