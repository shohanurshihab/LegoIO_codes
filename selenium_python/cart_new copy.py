from turtle import onclick
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

typing_speed = 0.5
driver = webdriver.Chrome()

url = "https://ns26njj87sh.dataflightit.com/rw/"

driver.maximize_window()
browser = driver.get(url)
WebDriverWait(driver, 10).until(EC.title_contains("Home"))

def check_new_cookies(previous_cookies, current_cookies):
    new_cookies = [cookie for cookie in current_cookies if cookie not in previous_cookies]
    return new_cookies

def print_new_cookies(new_cookies):
    for cookie in new_cookies:
        print("New Cookie:", cookie['name'], "->", cookie['value'])

def get_cookies(driver):
    return driver.get_cookies()

def click_element(element):
    element.click()
    time.sleep(1)

element = driver.find_element(By.PARTIAL_LINK_TEXT, f'Exp180')
click_element(element)

item2 = driver.find_element(By.PARTIAL_LINK_TEXT, "See the Service list")
click_element(item2)

select_item = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div[1]/div/p[2]/a")
click_element(select_item)

cart_2 = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[1]/div[1]/div/div/div[4]/button")
click_element(cart_2)

cart_4 = driver.find_element(By.XPATH, "/html/body/div[6]/nav[1]/div/div/div[3]/div/div/a")
click_element(cart_4)

continue_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Continue")
click_element(continue_btn)

cv_upload = driver.find_element(By.XPATH, "/html/body/div[7]/div/section/div/div[1]/div/div[2]/div/form/p/input")
cv_upload.send_keys("E:/LegoIO\ME/selenium_python/res.docx")

upload_button = driver.find_element(By.XPATH, "/html/body/div[7]/div/section/div/div[1]/div/div[2]/div/form/button")
click_element(upload_button)

continue_btn_guest = driver.find_element(By.XPATH, "/html/body/div[7]/div/section/div/div[1]/div/div[2]/div[3]/div/div/div[1]/p[3]")
click_element(continue_btn_guest)

email_input = driver.find_element(By.XPATH, '/html/body/div[7]/div/section/div/div[1]/div/div[2]/div[3]/div/div/div[2]/div/form/p/input')
email_input.send_keys("devile741@gmail.com")

continue_btn_guest = driver.find_element(By.XPATH, "/html/body/div[7]/div/section/div/div[1]/div/div[2]/div[3]/div/div/div[2]/div/form/button")
click_element(continue_btn_guest)

previous_cookies = get_cookies(driver)

payment_options_container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "mmh_paypal_button_container"))
)

time.sleep(30)

current_cookies = get_cookies(driver)
new_cookies = check_new_cookies(previous_cookies, current_cookies)
print_new_cookies(new_cookies)

# Rest of the code...

# target_text = "Debit"
# iframes = driver.find_elements(By.TAG_NAME, "iframe")
# iframe = iframes[0] # first iframe

# driver.switch_to.frame(iframe)
# if iframe:
    
#     # Find the element containing the target text
#     element = driver.find_element(By.XPATH,f"//*[contains(text(), '{target_text}')]")
#     if element:
#         print("Found element",element.text)
#     else:
#         print("null")
#     # Click on the element
#     element.click()
#     time.sleep(3)
    

    
# else:
#     print("No iframe found on the page.")

# time.sleep(30)
# iframes1 = driver.find_elements(By.TAG_NAME, "iframe")
# iframe1 = iframes1[0] # first iframe
# driver.switch_to.frame(iframe1)
# time.sleep(5)
# card_no = 4032031956134851
# exp = "03/27"
# csc = 123
# first_name = "Thana"
# last_name = "tos"
# zip_code = 94588
# mobile = 4083516772
# email = "devile741@gmail.com"



# card_number = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[2]/div/div[1]/div/div/div/input")
# card_number.click()
# time.sleep(3)
# card_number_input = card_number.send_keys("4032031956134851")
# time.sleep(1)
# expires = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[3]/div[1]/div[1]/input")
# expires.click()
# expires.send_keys(exp)
# csc_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[3]/div[3]/div[1]/input")
# csc_inp.click()
# csc_inp.send_keys(csc)
# first_name_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[4]/div[2]/div[1]/div[1]/input")
# first_name_inp.click()
# first_name_inp.send_keys(first_name)
# last_name_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[4]/div[2]/div[3]/div[1]/input")
# last_name_inp.click()
# last_name_inp.send_keys(last_name)
# zip_code_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[4]/div[3]/div/div/div[1]/input")
# zip_code_inp.click()
# zip_code_inp.send_keys(zip_code)
# mobile_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[5]/div/div[1]/div/input")
# mobile_inp.click()
# mobile_inp.send_keys(mobile)
# email_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[6]/div/div[1]/input")
# email_inp.click()
# email_inp.send_keys(email)

# pay_now = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[8]/button")
# pay_now.click()

# time.sleep(15)
# driver.quit()
