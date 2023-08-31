from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the main URL
main_url = "https://ns26njj87sh.dataflightit.com/cart/checkout/sign-in/mmh/loginorguestsuccess"
driver.get(main_url)

# Find all the links on the page
main_link_elements = driver.find_elements(By.TAG_NAME, 'a')

# Collect the URLs and text of all the links on the main page
main_link_info = [(link.get_attribute('href'), link.text) for link in main_link_elements if link.get_attribute('href') and "#" not in link.get_attribute('href')]

# Initialize sets to track visited and couldn't visit links
visited_links = set()
template_not_exist_links = []
page_not_found_links = []

# Store URLs, their corresponding clicked element texts, and labels
link_info = []

# Function to smoothly scroll to the bottom of a page
def smooth_scroll():
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    scroll_increment = 100
    current_position = 0
    while current_position < total_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        current_position += scroll_increment
        time.sleep(0.1)  # Adjust sleep time for smoother scrolling

# Function to visit a link and capture clicked element text
def visit_link(link_url, clicked_element_text):
    try:
        driver.get(link_url)
        smooth_scroll()  # Scroll to the bottom smoothly
        
        page_title = driver.title
        
        if "TemplateDoesNotExist" in page_title:
            template_not_exist_links.append((clicked_element_text, link_url))
        elif "Page not found" in page_title:
            page_not_found_links.append((clicked_element_text, link_url))
        else:
            visited_links.add(link_url)
            link_info.append((clicked_element_text, link_url))
            
            # Wait for the page to load completely
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            
            driver.get(main_url)  # Return to the main page
    except TimeoutException:
        print(f"Unable to click and load: {link_url}, Retrying...")

# Navigate to each link on the main page and return to the main page
for main_link_url, main_link_text in main_link_info:
    visit_link(main_link_url, main_link_text)

# Export the visited and couldn't visit links to a txt file
with open("visited_links.txt", "w") as f:
    f.write("Visited Links:\n")
    for text, url in link_info:
        f.write(f"{text}: {url}\n")

    f.write("\nTemplateDoesNotExist Links:\n")
    for text, url in template_not_exist_links:
        f.write(f"{text}: {url}\n")
    
    f.write("\nPage not found Links:\n")
    for text, url in page_not_found_links:
        f.write(f"{text}: {url}\n")

# Close the WebDriver
driver.quit()
