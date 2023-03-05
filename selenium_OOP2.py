from selenium import webdriver
from selenium_OOP import LoginPage
import time
from selenium1 import make_screenshot

driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
time.sleep(0.5)
page.enter_username('standard_user')
time.sleep(0.5)
page.enter_password('secret_sauce')
time.sleep(0.5)
page.click_login()

try:
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
except AssertionError:
    print ('Assercja nie przeszła')
else:
    print ('Assercja przeszła')
finally:
    print ('Po assercji')
    driver.quit

time.sleep(0.5)
make_screenshot(driver)
driver.quit()
