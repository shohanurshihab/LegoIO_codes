from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the main URL
main_url = "https://bangladesh.gov.bd/"
driver.get(main_url)

# Find all the links on the page
main_link_elements = driver.find_elements(By.TAG_NAME, 'a')

# Collect the URLs and text of all the links on the main page
main_link_info = set((link.get_attribute('href'), link.text) for link in main_link_elements if link.get_attribute('href') and "#" not in link.get_attribute('href'))

# Initialize sets to track visited and couldn't visit links
visited_links = set()
template_not_exist_links = []
page_not_found_links = []

# Store URLs, their corresponding clicked element texts, and labels
link_info = []



# Function to visit a link and capture clicked element text
def visit_link(link_url, clicked_element_text):
    try:
        driver.get(link_url)

        # Execute JavaScript to interrupt the loading
        driver.execute_script("window.stop();")

        page_title = driver.title

        if "403" in page_title:
            page_not_found_links.append((clicked_element_text, link_url))
        else:
            visited_links.add(link_url)
            link_info.append((clicked_element_text, link_url))

    except WebDriverException as e:
        print(f"Error accessing {link_url}: {e}")
        page_not_found_links.append((clicked_element_text, link_url))

    except Exception as e:
        print(f"An unexpected error occurred while accessing {link_url}: {e}")
        page_not_found_links.append((clicked_element_text, link_url))


# Navigate to each link on the main page and return to the main page
for main_link_url, main_link_text in main_link_info:
    visit_link(main_link_url, main_link_text)
   
# Export the visited and couldn't visit links to a txt file
with open("visited_links.txt", "w") as f:
    f.write("Visited Links:\n")
    for text, url in link_info:
        f.write(f"{url}\n")
    
    f.write("\nPage not found Links:\n")
    for text, url in page_not_found_links:
        f.write(f"{url}\n")

# Close the WebDriver
driver.quit()
