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

typing_speed = 0.5
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://ns26njj87sh.dataflightit.com/app/mmhauth/v2/signin"

browser = driver.maximize_window()
# customize browser screen
# driver.set_window_size(390, 844)
browser = driver.get(url)
time.sleep(2)
print(driver.title)
action = webdriver.ActionChains(driver)

email = driver.find_element(By.XPATH,'//*[@id="id_email"]')
email.click()
email_input = action.send_keys("skshihab531@gmail.com").perform()
time.sleep(2)
password = driver.find_element(By.XPATH,'//*[@id="id_password"]')
password.click()
password_input = action.send_keys("GgAPnN6FkQzePma").perform()
time.sleep(2)
login = driver.find_element(By.XPATH,'/html/body/section/div/div/div[1]/div/div/div[2]/form/button')
login.click()
time.sleep(1)

element = driver.find_element(By.PARTIAL_LINK_TEXT,f'Exp180')
browser = element.click()
time.sleep(5)

item = driver.find_element(By.XPATH,"/html/body/section[4]")
item2 = driver.find_element(By.PARTIAL_LINK_TEXT,"Show All")
item2.click()
time.sleep(5)
select_1 = driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div/div[2]/div/div")
select_item = driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div/div[2]/div/div/p[3]/a")
select_item.click()
time.sleep(5)


cart_1 = driver.find_element(By.XPATH,"/html/body/section[1]")
cart_2 = driver.find_element(By.XPATH,"/html/body/section[1]/div/div[3]/div[1]/div/div/div[3]/button")
cart_2.click()
time.sleep(5)

cart_3 = driver.find_element(By.XPATH,"/html/body/div[5]/nav[1]/div")
cart_4 = driver.find_element(By.XPATH,"/html/body/div[5]/nav[1]/div/div/div/div/a")
cart_4.click()
time.sleep(5)

card_2 = driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/div[1]/div[2]")
continue_btn = driver.find_element(By.PARTIAL_LINK_TEXT,"Continue 2209")
continue_btn.click()
time.sleep(3)

card_3 = driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div[2]")
cv_upload = driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div[2]/div/form/div/p/input")
cv_upload.send_keys("C:/Users/jamil/OneDrive/Desktop/Cv Document/Sadiquzzaman.docx")
time.sleep(2)
upload_button = driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div[2]/div/form/button")
upload_button.click()
time.sleep(5)

card_4 = driver.find_element(By.XPATH,"/html/body/div/div")
payment_btn = driver.find_element(By.XPATH,"/html/body/div/div")
payment_btn.click()
time.sleep(3)

card_number = 4111111111111111
exp = "03/2027"
csc = 123
first_name = "DJango"
last_name = "account"
zip_code = 94588
mobile = 4087419680
email = "django712345@protonmail.com"

card_5 = driver.find_element(By.XPATH,"/html/body")
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
time.sleep(5)
