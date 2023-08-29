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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


typing_speed = 0.1
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://ns26njj87sh.dataflightit.com/rw/"

browser = driver.maximize_window()
# customize browser screen
# driver.set_window_size(390, 844)
browser = driver.get(url)
time.sleep(2)
print(driver.title)
# #Multiple item search 
# search = driver.find_element(By.XPATH, '//*[@id="id_globalsearchquery"]')
# action = webdriver.ActionChains(driver)
# search_list = ('search_op1','search_op2','search_op3','search_op4')
# for x in search_list:
#     input = action.send_keys_to_element(search, f"{x}").perform()
#     time.sleep(3)
#     search.send_keys(Keys.ENTER)
#     time.sleep(10)
#     search.clear()

#search by one by one charecter 
search = driver.find_element(By.XPATH, '//*[@id="id_globalsearchquery"]')
action = webdriver.ActionChains(driver)
search_list = ('search_op1','search_op2','search_op3','search_op4')
for search_item in search_list:
    search_list = search_item
    search = driver.find_element(By.XPATH, '//*[@id="id_globalsearchquery"]')
    action = webdriver.ActionChains(driver)
    for x in search_list:
        input = action.send_keys_to_element(search, f"{x}").perform()
        time.sleep(typing_speed)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    #removed "search.clear() any action related to search expression causes an error"
