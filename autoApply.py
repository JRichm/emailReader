from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import os

from dotenv import load_dotenv

load_dotenv()

linkedinEmail = os.getenv("LINKEDIN_EMAIL")
linkedinPass = os.getenv("LINKEDIN_PASS")

# Load your work experience and education data
with open('myInfo.json') as p:
    user_data = json.load(p)

# Create a new instance of the chrome driver
driver = webdriver.Chrome()

# Log in to LinkedIn
driver.get('https://www.linkedin.com/login')
driver.find_element_by_id('username').send_keys(linkedinEmail)
driver.find_element_by_id('password').send_keys(linkedinPass)
driver.find_element_by_xpath('//button[text()="Sign in"]').click()

# Wait for the user to log in manually (you may need to add a delay here)
time.sleep(10)

# loop through job links and apply
job_links = ['url1', 'url2', 'url3']    # replace with a call to /get_links or something
for job_link in job_links:
    driver.get(job_link)

    # check if the job has an "easy apply" button
    easy_apply_button = driver.find_elements_by_xpath('//button[text()=Easy Apply]')
    if easy_apply_button:
        easy_apply_button[0].click()

        # Fill in the application form using your JSON
        # (need to inspect the page and replace the following lines with the actual form field names)
        driver.find_element_by_name('field_name_1').send_keys(user_data['experience']['job_title'])
        driver.find_element_by_name('field_name_2').send_keys(user_data['education']['degree'])

        # You may need to handle other fields like text areas, dropdowns, etc.

        # Submit the application
        driver.find_element_by_xpath('//button[text()="Submit application"]').click()

    else:
        # Log information about jobs that can't be applied through "Easy Apply"
        print(f"Job at {job_link} requires manual application.")

# Close the browser
driver.quit()