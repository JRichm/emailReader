from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import json
import os

from dotenv import load_dotenv

load_dotenv()

linkedinEmail = os.getenv("LINKEDIN_EMAIL")
linkedinPass = os.getenv("LINKEDIN_PASS")

# Load your work experience and education data
with open('./data/data.json') as p:
    user_data = json.load(p)

# Create a new instance of the chrome driver
driver = webdriver.Chrome()

# Log in to LinkedIn
driver.get('https://www.linkedin.com/login')
driver.find_element('name', 'session_key').send_keys(linkedinEmail)
driver.find_element('name', 'session_password').send_keys(linkedinPass)
driver.find_element('tag name', 'button').click()

# Wait for the user to log in manually (you may need to add a delay here)
time.sleep(2)

# loop through job links and apply
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get('http://localhost:5000/get_new_links', headers=headers)

# job_links = ['https://www.linkedin.com/jobs/view/3764749852/?refId=ByteString(length%3D16%2Cbytes%3D92a8ac5f...c2300f16)&trackingId=84wvPvkW7yI%2FsIUXrU3IqA%3D%3D']

if response.status_code == 200:
    # Extract job links from the response JSON
    job_links = response.json().get('new_links', [])
    print(f"Fetched {len(job_links)} new job links: {job_links}")
    
    # Now you can loop through job_links and perform your Selenium actions
    for job_link in job_links:
        driver.get(job_link['link'])
# if True:
#     for job_link in job_links:
#         driver.get(job_link)

        wait = WebDriverWait(driver, 10)

        # check if the job has an "easy apply" button
        easy_apply_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Easy Apply")]')))
        time.sleep(1)

        if easy_apply_button:
            driver.execute_script("arguments[0].scrollIntoView();", easy_apply_button)
            easy_apply_button.click()

            # Continue with the rest of your code
        else:
            # Log information about jobs that can't be applied through "Easy Apply"
            print(f"Job at {job_link} requires manual application.")

else:
    print(f"Failed to fetch new job links. Status code: {response.status_code}, Error: {response.text}")


# Close the browser
driver.quit()