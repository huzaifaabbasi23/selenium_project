from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
#options.set_capability("browserName", "firefox")

driver = webdriver.Remote(
    command_executor="http://192.168.10.13:4444",
    options=options
)

time.sleep(3)

driver.get("https://alnafi.com")

time.sleep(3)

print(driver.title)

