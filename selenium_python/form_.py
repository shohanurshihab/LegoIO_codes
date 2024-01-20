from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Define the number of times to run the code
num_runs = 200

# Function to select specific options for the provided questions
def select_specific_options(question, option_value):
            option_xpath = f"//div[@data-value='{option_value}']"
            driver.find_element(By.XPATH, option_xpath).click()

for run in range(num_runs):
    try:
        # Set the path to your chromedriver.exe
        driver = webdriver.Chrome()

        # Open the Google Form
        driver.get("https://forms.gle/aDxsvnv9Z1uwqyd9A")

        # Wait for the form to load
        time.sleep(1)

        # Iterate through the pages
        while True:
            # Look for each question and click the specified options if found
            for question, answer in [
                ("How would you rate your overall experience with the Bangladesh government website?", "2"),
                ("How frequently do you visit the Bangladesh government websites?", "Rarely"),
                ("How easy was it to find the information you were looking for on the website?", "Difficult"),
                ("Did you encounter any issues while navigating between different sections of the website?", "Yes"),
                ("How would you rate the clarity and comprehensibility of the content on the website?", "Poor"),
                ("Were you able to find up-to-date and relevant information on the website?", "No"),
                ("Did you experience any technical issues or errors while using the website?", "Yes"),
                ("How satisfied are you with the functionality of interactive elements (e.g., forms, search functionality)?", "Unsatisfied"),
                ("How visually appealing do you find the design and layout of the website?", "Very Unappealing"),
                ("Were you able to easily understand the hierarchy and organization of information on the website?", "No"),
                ("How well does the website perform on mobile devices in terms of responsiveness and functionality?", "Poor"),
                ("How easy is it to find and access user support (e.g., help guides, contact information) on the website?", "Difficult"),
                ("Were you able to find the necessary assistance or support when needed?", "No"),
                ("How confident are you in the security measures employed by the website, especially when providing personal information?", "Not at all Confident"),
                ("Did you experience any concerns regarding the privacy of your information while using the website?", "Yes"),
                ("How well does the website communicate important updates, announcements, or changes?", "Very Poorly"),
                ("Were you able to easily find information about recent updates or changes to the website?", "No"),
                ("Have you ever provided feedback or suggestions to the website? If yes, how satisfied were you with the response?", "Very Unsatisfied"),
                ("How important do you think it is for the government website to actively seek and consider user feedback?", "Very Important")
            ]:
                try:
                    select_specific_options(question, answer)
                except:
                    pass  # Continue to the next question if not found

            # Check if the "Next" button is present
            try:
                next_button = driver.find_element(By.XPATH, "//span[text()='পরবর্তী']")
                next_button.click()
                time.sleep(1)  # Add a delay to ensure the page loads
            except:
                print("not_working")
                break  # If the "Next" button is not found, break out of the loop

        # Submit the form
        submit_link = driver.find_element(By.XPATH, "//span[text()='জমা দিন']")
        print("joma")
        submit_link.click()

        # Close the browser
        driver.quit()

    except Exception as e:
        print(f"An error occurred in iteration {run + 1}: {str(e)}")
