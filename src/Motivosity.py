import os, sys
import json
from selenium import webdriver


# Variables, get credentials
base_url = "https://app.motivosity.com/home/"
auth = json.load(open('.\env\credentials.json'))
un = auth['un']
pw = auth['pw']

# Login, enter username & password, click sign-in
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
click_to_show_more = 0
for i in range(click_to_show_more):
    chrome.find_element_by_css_selector("a.btn.green.small").click()
    chrome.implicitly_wait(2)

# Scrape Appreciation elements
elements = chrome.find_elements_by_id("feedContainer")
users = {}
appreciation = []
for e in elements:
    bit = {}
    bit['readabledate'] = e.find_element_by_css_selector("div.post-time.ng-binding").text
    bit['receiver_name'] = e.find_element_by_class_name('post-name').text
    bit['receiver_url'] = e.find_element_by_class_name('post-name').get_attribute('href')
    bit['content'] = e.find_element_by_css_selector('span.ng-binding.ng-scope').text
    bit['giver_name'] = e.find_element_by_css_selector('span.ng-binding').text
    bit['giver_url'] = e.find_element_by_css_selector('a.post-name').get_attribute('href')
    bit['message'] = e.find_element_by_css_selector('p.pre.ng-binding.ng-scope').text
    appreciation.append(bit)

    # Make list of unique receiver_id
    receiver_id = bit['receiver_url'].split('?')[1].split('=')[1]
    if receiver_id not in users:
        users[receiver_id] = ""

    # Make list of unique giver_id
    giver_id = bit['giver_url'].split('?')[1].split('=')[1]
    if giver_id not in users:
        users[giver_id] = ""

# Look up User Info
for id, url in users.items():
    if url == '':
        chrome.get('https://app.motivosity.com/profile/index.xhtml?id={0}'.format(id))
        users[id] = chrome.find_element_by_xpath('//*[@ng-bind="user.department"]').text

# Save Departments file to disk
filepath = os.path.join(os.getcwd(), 'data', 'Motivosity-Users.json')
with open(filepath, 'w') as outfile:
    json.dump(users, outfile)

# Save Appreciation file to disk
filepath = os.path.join(os.getcwd(), 'data', 'Motivosity-Appreciation.json')
with open(filepath, 'w') as outfile:
    json.dump(appreciation, outfile)

# Clean up
chrome.close()
print("Scraping complete. See data/Motivosity-Appreciation.json ")
