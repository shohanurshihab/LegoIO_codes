from turtle import onclick
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys
import time
import re

typing_speed = 0.5
driver = webdriver.Chrome()

url = "https://ns26njj87sh.dataflightit.com/cart/checkout/sign-in/mmh/loginorguestsuccess"

browser = driver.maximize_window()
# customize browser screen
# driver.set_window_size(390, 844)
browser = driver.get(url)
time.sleep(10)
print(driver.title)
action = webdriver.ActionChains(driver)


# payment_btn = driver.find_element(By.XPATH,"/html/body/div/div")
payment_btn = driver.find_element(By.XPATH,"//div[@aria-label='Debit or Credit Card']")
payment_btn.click()
time.sleep(3)

card_number = 4032031956134851
exp = "03/2027"
csc = 123
first_name = "Thana"
last_name = "tos"
zip_code = 94588
mobile = 4083516772
email = "devile741@gmail.com"

card_number = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[2]/div/div[1]/div/div/div/input")
card_number.send_keys(card_number)
expires = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[3]/div[1]/div[1]/input")
expires.send_keys(exp)
csc = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[3]/div[3]/div[1]/input")
csc.send_keys(csc)
first_name = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[4]/div[2]/div[1]/div[1]/input")
first_name.send_keys(first_name)
last_name = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[4]/div[2]/div[3]/div[1]/input")
last_name.send_keys(last_name)
zip_code = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[4]/div[3]/div/div/div[1]/input")
zip_code.send_keys(zip_code)
mobile = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[5]/div/div[1]/div/input")
mobile.send_keys(mobile)
email = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[6]/div/div[1]/input")
email.send_keys(email)

pay_now = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[8]/button")
pay_now.click()
time.sleep(1)
