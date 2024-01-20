from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Define the number of times to run the code
num_runs = 100

for run in range(num_runs):
    try:
        # Set the path to your chromedriver.exe
        driver = webdriver.Chrome()

        # Open the Google Form
        driver.get("https://forms.gle/aDxsvnv9Z1uwqyd9A")

        # Wait for the form to load
        time.sleep(1)

        # Iterate through the first 2 sections and click the "Next" button
        for _ in range(2):
            next_button = driver.find_element(By.XPATH, "//span[text()='পরবর্তী']")
            next_button.click()
            time.sleep(1)

        def select_random_option():
            options = driver.find_elements(By.XPATH, "//div[@role='radio']")
            if options:
                option_to_select = random.choice(options).get_attribute("data-value")
                option_xpath = f"//div[@role='radio'][@data-value='{option_to_select}']"
                driver.find_element(By.XPATH, option_xpath).click()

        # Iterate through the pages
        while True:
            select_random_option()

            # Check if the "Next" button is present
            next_button = driver.find_element(By.XPATH, "//span[text()='পরবর্তী']")
            next_button.click()

            time.sleep(1)  # Add a delay to ensure the page loads

            # Check if it's the last page by checking the absence of the "Next" button
            try:
                next_button = driver.find_element(By.XPATH, "//span[text()='পরবর্তী']")
                print("working")
            except:
                # If the "Next" button is not found, break out of the loop
                print("not_working")
                break

        for _ in range(5):
            select_random_option()

        submit_link = driver.find_element(By.XPATH, "//span[text()='জমা দিন']")
        print("joma")
        submit_link.click()

        # Close the browser
        driver.quit()

    except Exception as e:
        print(f"An error occurred in iteration {run + 1}: {str(e)}")

# End of the loop
