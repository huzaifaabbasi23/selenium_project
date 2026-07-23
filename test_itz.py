import pytest
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def setup_function():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://alnafi.com/auth/sign-in")
    driver.maximize_window()

def teardown_function():
    driver.quit()

@pytest.mark.parametrize("username,password", [
    ("huzaif01@gmail.com", "$16767788"),
    ("aill@gmail.com", "12@@4522"),
    ("huzzi@gmail.com", "tgy123")
])

def test_login(username, password):
    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys(username)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[2]/div/div/input').send_keys(password)
    time.sleep(3)