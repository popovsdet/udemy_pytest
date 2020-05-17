# import time
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# # driver.maximize_window()
# driver.implicitly_wait(2)
# driver.get(url='https://google.com')
# element = driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
# element.send_keys('Novosibirsk')
# button = driver.find_element_by_xpath('//div[@class="tfB0Bf"]//input[@class="gNO89b"]')
# button.click()
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.ui import WebDriverWait

# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# element = WebDriverWait(driver=driver, timeout=3).until(
#     method=exp_cond.presence_of_element_located(locator=(By.NAME, "q")),
#     message='Error message: no search bar')

# try:
#     # Wait as long as required, or maximum of 5 sec for element to appear
#     # If successful, retrieves the element
#     element = WebDriverWait(driver, 3).until(method=exp_cond.presence_of_element_located((By.NAME, "q11")))
#     element.send_keys("selenium")
#     element.send_keys(Keys.ENTER)
#
# # except TimeoutException:
# #     print("Failed to load search bar at www.google.com")
# finally:
# driver.quit()

# element = driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
# element.send_keys('Boar')
# button = driver.find_element_by_xpath('//div[@class="tfB0Bf"]//input[@class="gNO89b"]')
# button.click()
