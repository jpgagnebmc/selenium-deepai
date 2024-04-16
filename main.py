from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://deepai.org")

print(driver.title)

login = driver.find_element(By.ID, 'headerLoginButton')
login.click()
time.sleep(1)

signupToggle = driver.find_element(By.ID, 'signupToggle')
signupToggle.click()
time.sleep(1)

signupWithEmail = driver.find_element(By.CLASS_NAME, 'login-with-email')
signupWithEmail.click()
time.sleep(1)

userEmail = driver.find_element(By.ID, 'user-email')
userEmail.send_keys("test1711727148@deepai.org")
time.sleep(1)

print(driver.get_log('browser'))
driver.close()
