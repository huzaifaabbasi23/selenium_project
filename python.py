from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

dropdown = driver.find_element(By.ID, "searchLanguage")

select = Select(dropdown)

options = select.options
print("Total languages:", len(options))

driver.quit()
