from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the initial URL
url = "https://ns26njj87sh.dataflightit.com/rw/"
driver.get(url)

# Collect all the links on the main page
links = driver.find_elements(By.TAG_NAME, 'a')
link_urls = [link.get_attribute('href') for link in links if link.get_attribute('href') and '#' not in link.get_attribute('href')]

# Initialize lists to store visited and couldn't-visit links
visited_links = set()
couldnt_visit_links = []
template_not_exist_links = []

# Navigate to each link and return to the main page
for link_url in link_urls:
    if link_url not in visited_links:
        try:
            driver.get(link_url)
            print(f"Clicked and loaded: {link_url}")
            
            # Check if the title contains "TemplateDoesNotExist"
            if "TemplateDoesNotExist" in driver.title:
                template_not_exist_links.append(link_url)
            else:
                visited_links.add(link_url)
            
            # Wait for the page to load completely before going back
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            
            driver.back()  # Return to the main page
        except TimeoutException:
            print(f"Unable to click and load: {link_url}, Retrying...")
            couldnt_visit_links.append(link_url)
            continue

# Close the WebDriver
driver.quit()

# Write visited, couldn't-visit, and TemplateDoesNotExist links to a text file
with open('link_status.txt', 'w') as file:
    file.write("Visited Links:\n")
    for visited_link in visited_links:
        file.write(visited_link + '\n')
    
    file.write("\nCouldn't Visit Links:\n")
    for couldnt_visit_link in couldnt_visit_links:
        file.write(couldnt_visit_link + '\n')
    
    file.write("\nTemplateDoesNotExist Links:\n")
    for template_not_exist_link in template_not_exist_links:
        file.write(template_not_exist_link + '\n')

print("Links exported to link_status.txt")
