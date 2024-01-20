from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def check_link_status(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False

def get_links(driver, url):
    try:
        driver.get(url)
        links = driver.find_elements(By.TAG_NAME, "a")
        return [link.get_attribute('href') for link in links if link.get_attribute('href')]
    except Exception as e:
        print(f"Error getting links from {url}: {e}")
        return []

def main():
    urls_file = "main_urls copy.txt" 

    # Initialize WebDriver
    driver = webdriver.Chrome()

    try:
        with open(urls_file, 'r') as file:
            main_urls = file.readlines()

        with open('link_status_summary1.txt', 'w') as result_file:
            for main_url in main_urls:
                main_url = main_url.strip()
                print(f"Checking links on: {main_url}")
                links = get_links(driver, main_url)
                alive_count, dead_count = 0, 0

                for link in links:
                    try:
                        if check_link_status(link):
                            print(link)
                            alive_count += 1
                        else:
                            dead_count += 1
                    except Exception as e:
                        print(f"Error checking link {link}: {e}")

                result = f"{main_url} = Dead: {dead_count} -- Alive: {alive_count}\n"
                print(result)
                result_file.write(result)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
