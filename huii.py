from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time as t

driver = webdriver.Chrome()

now = datetime.now()

filename = now.strftime("Screenshot__%B_%d_%Y__%I_%M_%p.png")

driver.get("https://alnafi.com/auth/sign-in")
driver.maximize_window()
t.sleep(2)
driver.maximize_window()
my_email = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[1]/div/div/input')
my_passwd = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[2]/div/div/input')
driver.execute_script("arguments[0].setAttribute('style','background: yellow; border:2px solid red;');",my_email)
driver.execute_script("arguments[0].setAttribute('style','background: yellow;');",my_passwd)

t.sleep(3)
driver.save_screenshot(filename)
driver.quit()