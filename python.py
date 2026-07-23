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

# Password
#mypassword = driver.find_element(By.ID, "password")
#mypassword.send_keys("secret_sauce")
#time.sleep(3)


# Login Button
#mylogin = driver.find_element(By.ID, "login-button")
#mylogin.click()
#driver.implicitly_wait(5)
#time.sleep(5)

#my_code=driver.find_element(By.CLASS_NAME,"product_sort_container")
#my_code.send_keys("Price(low to high)")
#time.sleep(10)
# Close Browser
driver.quit()