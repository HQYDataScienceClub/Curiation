import os, sys
import json
from selenium import webdriver


# Variables
base_url = "https://app.motivosity.com/home/"
auth = json.load(open('.\env\credentials.json'))
un = auth['un']
pw = auth['pw']


# Login
if un == "":
    print("You must manually enter credentials into the src\scrape.py script")
    sys.exit()
print("Scraping started...")
chrome = webdriver.Chrome('env/chromedriver') # this will open a chrome browser
chrome.get(base_url)

login = chrome.find_element_by_id("email")
login.send_keys(un)

login = chrome.find_element_by_id("j_password")
login.send_keys(pw)

chrome.find_element_by_id("signInLink").click()
chrome.implicitly_wait(3)


# Snooze Survey
chrome.find_element_by_css_selector("span.btn.black.anchor").click()
chrome.refresh()

# Show More Records
for i in range(click_to_show_more):
    chrome.find_element_by_css_selector("a.btn.green.small").click()
    chrome.implicitly_wait(5)


# Scrape Appreciation elements
elements = chrome.find_elements_by_id("feedContainer")


# Gather Appreciation attributes
appreciation = []
for element in elements:
    bit = {}
    bit['readabledate'] = element.find_element_by_css_selector("div.post-time.ng-binding").text
    bit['giver'] = element.find_element_by_css_selector("a.post-name").text
    bit['giver_url'] = element.find_element_by_css_selector("a.post-name").get_attribute('href')
    appreciation.append(bit)


# Save file to disk
filepath = os.path.join(os.getcwd(), 'src', 'appreciation.json')
with open(filepath, 'w') as outfile:
    json.dump(appreciation, outfile)


# Clean up
chrome.close()
print("Scraping complete. See src/appreication ")
