from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


username = (By.XPATH,"//input[@id='user-name']")
password = (By.XPATH,"//input[@id='password']")
username_list = ["standard_user","performance_glitch_user","visual_user"]
password_word = "secret_sauce"

def type_in(username,password,username_list,password_word):
  j = 1
  for i in username_list:
    us = driver.find_element(*username)
    us.send_keys(i)
    time.sleep(3)
    pas = driver.find_element(*password)
    pas.send_keys(password_word)
    time.sleep(5)
    if j != 3:
      us.clear()
      pas.clear()

  else:
    pas.send_keys(Keys.ENTER)


val = (username,password,username_list,password_word)
type_in(*val)

# driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'nearest'});",element)

