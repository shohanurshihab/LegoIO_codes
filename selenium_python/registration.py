from lib2to3.pgen2.driver import Driver
from turtle import onclick
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import re
import random

typing_speed = 0.5
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.resumenalyzer.com/rw/"

browser = driver.maximize_window()
# customize browser screen
# driver.set_window_size(390, 844)
browser = driver.get(url)
time.sleep(5)
print(driver.title)
action = webdriver.ActionChains(driver)
#user account 
user_account = driver.find_element(By.XPATH,'//*[@id="navbarAccount"]')
webdriver.ActionChains(driver).move_to_element(user_account).perform()
browser = user_account.click()
time.sleep(2)
#sign up
sign_up = driver.find_element(By.XPATH,'//*[@id="navbarLogo"]/ul/li/ul/div/a[2]/div/h6[2]')
webdriver.ActionChains(driver).move_to_element(sign_up).perform()
browser = sign_up.click()
time.sleep(2)
#names
first_names = ('John','Andy','Joe')
last_names = ('Johnson','Smith','Williams')
emails = ('devile741@gmail.com')
passwords = ('GgAPnN6FkQzePma')
#First name
name1 = driver.find_element(By.XPATH,'//*[@id="id_first_name"]')
name1.click()
first_name = random.choice(first_names)
print(first_name)
first_name_input = action.send_keys(first_name).perform()
time.sleep(2)
#Second name
name2 = driver.find_element(By.XPATH,'//*[@id="id_last_name"]')
name2.click()
second_name = random.choice(last_names)
print(second_name)
second_name_input = action.send_keys(second_name).perform()
time.sleep(2)
#Email
email = driver.find_element(By.XPATH,'//*[@id="id_email"]')
email.click()
email = emails
print(email)
email_input = action.send_keys(email).perform()
time.sleep(2)
#Password
password = driver.find_element(By.XPATH,'//*[@id="id_password1"]')
password.click()
password = passwords
print(password)
passwords_input = action.send_keys(password).perform()
time.sleep(2)
#Re_Password
re_password = driver.find_element(By.XPATH,'//*[@id="id_password2"]')
re_password.click()
print(password)
re_password_input = action.send_keys(password).perform()
time.sleep(2)
#signup_button
signuup_button = driver.find_element(By.XPATH,'/html/body/section/div/div/div[1]/div/div/div[2]/form/button')
signuup_button.click()
time.sleep(2)

