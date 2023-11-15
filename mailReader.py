import requests
import imaplib
import email
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

imapEmail = os.getenv("IMAP_EMAIL")
imapPass = os.getenv("IMAP_PASS")

# connect to the server
mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
status = mail.login(imapEmail, imapPass)
print("Login status:", status)

# select the mailbox you want to search
status, messages = mail.select("inbox")
print("Select status:", status)
print("Number of messages in the mailbox:", messages[0])

# dictionary to store job IDs and links
job_links = {}

# retrieve all messages in the inbox from the specified email addresses
key = 'FROM'
value = 'jobalerts-noreply@linkedin.com'
result, data = mail.search(None, key, value)
message_numbers = data[0].split()

# iterate through each email
for num in message_numbers:
    _, msg_data = mail.fetch(num, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    # extract HTML content
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)

                # Process HTML content with BeautifulSoup
                soup = BeautifulSoup(html_body, "html.parser")
                
                # Perform additional processing or extraction based on your needs
                # For example, find all links in the HTML content
                links = soup.find_all("a", href=True)

                for link in links:
                    href = link["href"]
                    if href.startswith("https://www.linkedin.com/comm/jobs/view/"):

                        # extract job ID
                        job_id = href.split("/")[6]
                        print("job_id")
                        print(job_id)

                        # add link to dictionary if job ID is not present
                        if job_id not in job_links:
                            job_links[job_id] = href
                            print("Job Posting Link:", href, "\n\n")

# print final job links
print("Final Job Posting Links:")
for job_id, link in job_links.items():
    print(f"Job ID: {job_id}, Link: {link}", "\n")

# logout from the server
mail.logout()

url = 'http://localhost:5000/addLink'
headers = {
    'user-agent': 'mailReader/0.0.1',
    'methods': 'POST'
}

body = {
    'key': 'value'
}
response = requests.post(url, headers=headers, json=body)
print(response.json())