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

browser = driver.maximize_window()
# customize browser screen
# driver.set_window_size(390, 844)
browser = driver.get(url)
time.sleep(2)
print(driver.title)
action = webdriver.ActionChains(driver)

element = driver.find_element(By.PARTIAL_LINK_TEXT,f'Exp180')
element.click()
time.sleep(1)

item2 = driver.find_element(By.PARTIAL_LINK_TEXT,"See the Service list")
item2.click()
time.sleep(1)

select_item = driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div[1]/div/p[2]/a")
select_item.click()
time.sleep(1)


cart_2 = driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[1]/div[1]/div/div/div[4]/button")
cart_2.click()
time.sleep(1)

# cart_4 = driver.find_element(By.XPATH,"/html/body/div[5]/nav[1]/div/div/div/div/a")
cart_4 = driver.find_element(By.XPATH,"/html/body/div[6]/nav[1]/div/div/div[3]/div/div/a")
cart_4.click()
time.sleep(1)

continue_btn = driver.find_element(By.PARTIAL_LINK_TEXT,"Continue")
continue_btn.click()
time.sleep(3)

# cv_upload = driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div[2]/div/form/div/p/input")
cv_upload = driver.find_element(By.XPATH,"/html/body/div[7]/div/section/div/div[1]/div/div[2]/div/form/p/input")
cv_upload.send_keys("E:/LegoIO\ME/selenium_python/res.docx")
time.sleep(2)
# upload_button = driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div[2]/div/form/button")
upload_button = driver.find_element(By.XPATH,"/html/body/div[7]/div/section/div/div[1]/div/div[2]/div/form/button")
upload_button.click()


# cookies_from_first_page = driver.get_cookies()
#Click on the Continue as Guest
continue_btn_guest = driver.find_element(By.XPATH,"/html/body/div[7]/div/section/div/div[1]/div/div[2]/div[3]/div/div/div[1]/p[3]")
continue_btn_guest.click()
time.sleep(3)

#Fill guest email
email = driver.find_element(By.XPATH,'/html/body/div[7]/div/section/div/div[1]/div/div[2]/div[3]/div/div/div[2]/div/form/p/input')
email_input = email.send_keys("devile741@gmail.com")

#Click Submit and continue as guest
continue_btn_guest_1 = driver.find_element(By.XPATH,f"//*[contains(text(), 'Submit')]")
# continue_btn_guest_1.click()
continue_btn_guest_1.send_keys(Keys.SPACE) 

# Set the captured cookies on the browser session for the second page
driver.refresh()

payment_options_container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "mmh_paypal_button_container"))
)


target_text = "Debit"
iframes = driver.find_elements(By.TAG_NAME, "iframe")
iframe = iframes[0] # first iframe

driver.switch_to.frame(iframe)
if iframe:
    
    # Find the element containing the target text
    element = driver.find_element(By.XPATH,f"//*[contains(text(), '{target_text}')]")
    if element:
        print("Found element",element.text)
    else:
        print("null")
    # Click on the element
    element.click()
    time.sleep(3)
    

    
else:
    print("No iframe found on the page.")

time.sleep(3)
iframes1 = driver.find_elements(By.TAG_NAME, "iframe")
iframe1 = iframes1[0] # first iframe
driver.switch_to.frame(iframe1)
time.sleep(5)
card_no = 4032031956134851
exp = "03/27"
csc = 123
first_name = "Thana"
last_name = "tos"
zip_code = 94588
mobile = 4083516772
email = "devile741@gmail.com"



card_number = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[2]/div/div[1]/div/div/div/input")
card_number.click()
time.sleep(3)
card_number_input = card_number.send_keys("4032031956134851")
time.sleep(1)
expires = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[3]/div[1]/div[1]/input")
expires.click()
expires.send_keys(exp)
csc_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[3]/div[3]/div[1]/input")
csc_inp.click()
csc_inp.send_keys(csc)
first_name_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[4]/div[2]/div[1]/div[1]/input")
first_name_inp.click()
first_name_inp.send_keys(first_name)
last_name_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[4]/div[2]/div[3]/div[1]/input")
last_name_inp.click()
last_name_inp.send_keys(last_name)
zip_code_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[4]/div[3]/div/div/div[1]/input")
zip_code_inp.click()
zip_code_inp.send_keys(zip_code)
mobile_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[5]/div/div[1]/div/input")
mobile_inp.click()
mobile_inp.send_keys(mobile)
email_inp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[6]/div/div[1]/input")
email_inp.click()
email_inp.send_keys(email)

pay_now = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/div/div[8]/button")
pay_now.click()

time.sleep(15)
driver.quit()
