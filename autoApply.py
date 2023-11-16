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