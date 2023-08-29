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

url = "https://ns26njj87sh.dataflightit.com/rw/"

browser = driver.maximize_window()
# customize browser screen
# driver.set_window_size(390, 844)
browser = driver.get(url)
time.sleep(5)
print(driver.title)

# mobile view 

# All nav bar test
# Mouse pointer hover test
for i in range(8, 1, -1):
    #nav_list_old = driver.find_element(By.XPATH,f"/html/body/div[6]/div/div/div/ul/li[{i}]/a")
    nav_list = driver.find_element(By.XPATH,f"/html/body/div[6]/div/div/div/ul/li[{i}]/a")
    #/html/body/div[6]/div/div/div/ul/li[1]/a
    element_size = nav_list.size
    print (nav_list.text)
    print(element_size)
    webdriver.ActionChains(driver).move_to_element(nav_list).perform()
    time.sleep(1)
# Click individual nav bar item click
product_list = ('Exp180','Adhoc','Dialogue','Dialect','Identity','Staircase','Bandwidth','Strategy')
for x in product_list:
    element = driver.find_element(By.PARTIAL_LINK_TEXT,f'{x}')
    browser = element.click()
    print(x)
    print(driver.title)
    time.sleep(2)
    driver.back()
    time.sleep(2)