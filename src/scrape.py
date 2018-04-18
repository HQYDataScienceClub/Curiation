import os
import json
from selenium import webdriver


# Variables
base_url = "https://app.motivosity.com/home/"
un = ""
pw = ""


# Login
print("Scraping started...")
chrome = webdriver.Chrome('env/chromedriver') # this will open a chrome browser
chrome.get(base_url)

login = chrome.find_element_by_id("email")
login.send_keys(un)

login = chrome.find_element_by_id("j_password")
login.send_keys(pw)

chrome.find_element_by_id("signInLink").click()
chrome.implicitly_wait(5)


# Snooze Survey
chrome.find_element_by_css_selector("span.btn.black.anchor").click()
chrome.implicitly_wait(2)


# Show More Records
click_to_show_more = 1 # each click is 15 addtl records
for i in range(click_to_show_more):
    chrome.find_element_by_css_selector("a.btn.green.small").click()
    chrome.implicitly_wait(1)


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
filepath = os.path.join('src', 'appreciation.json')
with open(filepath, 'w') as outfile:
    json.dump(appreciation, outfile)


# Clean up
chrome.close()
print("Scraping complete. See src/appreication ")
