from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

# Initialize the WebDriver
driver = webdriver.Chrome()

# Read main_url from a text file
with open("main_urls.txt", "r") as file:
    main_urls = file.readlines()

# Function to visit a link and capture clicked element text
def visit_link(link_url, clicked_element_text):
    try:
        driver.get(link_url)

        # Execute JavaScript to interrupt the loading
        driver.execute_script("window.stop();")

        page_title = driver.title

        if "403" in page_title:
            return "not_found"
        elif "404" in page_title:
            return "not_found"
        elif "400" in page_title:
            return "not_found"
        else:
            return "visited"

    except WebDriverException as e:
        print(f"Error accessing {link_url}: {e}")
        return "not_found"

    except Exception as e:
        print(f"An unexpected error occurred while accessing {link_url}: {e}")
        return "not_found"

# Open a single output file for all main URLs
with open("consolidated_output.txt", "w") as f:
    # Iterate through each main_url from the file
    for main_url in main_urls:
        main_url = main_url.strip()  # Remove leading/trailing whitespaces

        try:
            driver.get(main_url)

            # Find all the links on the page
            main_link_elements = driver.find_elements(By.TAG_NAME, 'a')

            # Collect the URLs and text of all the links on the main page
            main_link_info = set((link.get_attribute('href'), link.text) for link in main_link_elements if link.get_attribute('href') and "#" not in link.get_attribute('href'))
            print(len(main_link_info))
            # Initialize sets to track visited and couldn't visit links for each main_url
            visited_links = set()
            page_not_found_links = []

            # Store URLs, their corresponding clicked element texts, and labels
            link_info = []

            # Navigate to each link on the main page and return to the main page
            for main_link_url, main_link_text in main_link_info:
                result = visit_link(main_link_url, main_link_text)

                if result == "visited":
                    visited_links.add(main_link_url)
                    link_info.append((main_link_text, main_link_url))
                elif result == "not_found":
                    page_not_found_links.append((main_link_text, main_link_url))
            print(visited_links)
            # Write to the consolidated output file
            f.write(f"Main URL: {main_url}\n\n")
            f.write(f"Visited Links ({len(visited_links)}):\n")
            f.write(visited_links)
            # for text, url in link_info:
            #     f.write(f"{url}\n")

            f.write(f"\nPage not found Links:{len(page_not_found_links)}\n")
            # for text, url in page_not_found_links:
            #     f.write(f"{url}\n")

            # Separate main URLs by three lines
            f.write("\n" * 3)

        except Exception as e:
            print(f"An error occurred for {main_url}: {e}")
            continue  # Skip to the next URL if an exception occurs

# Close the WebDriver
driver.quit()
