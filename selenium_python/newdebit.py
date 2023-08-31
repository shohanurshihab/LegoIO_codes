from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://ns26njj87sh.dataflightit.com/cart/checkout/sign-in/mmh/loginorguestsuccess")
time.sleep(1)

# # Find the element that you want to start from (for example, a point before the tab navigation)
# starting_element = driver.find_element(By.XPATH,"/html/body")

# # Click on the starting element to give it focus

# time.sleep(1)
# # Simulate pressing the Tab key 12 times
# for _ in range(12):
#     starting_element.send_keys(Keys.TAB)
#     time.sleep(1)
# # Simulate pressing the Enter key
# starting_element.send_keys(Keys.ENTER)
# time.sleep(3)
# payment_options_container = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "mmh_paypal_button_container"))
# )

# # You might need to wait for the specific payment options to load within the container
# # Here, I'm using a generic wait for demonstration
# # You'll need to identify the appropriate conditions for your scenario
# WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Debit or Credit Card')]"))
# ).click()

target_text = "Debit"
iframes = driver.find_elements(By.TAG_NAME, "iframe")
iframe = iframes[0] # first iframe
driver.switch_to.frame(iframe)
if iframe:
    
    # Find the element containing the target text
    element = driver.find_element(By.XPATH,f"//*[contains(text(), '{target_text}')]")
    
    # Click on the element
    element.click()
    time.sleep(3)
else:
    print("No iframe with allowpaymentrequest attribute found on the page.")


