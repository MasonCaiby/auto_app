import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# get login creds
angel_creds = np.genfromtxt('angel_creds.csv', delimiter=',', dtype=str)
angel_email_cred = angel_creds[0]
angel_password_cred = angel_creds[1]

# create browser object, navigate to login
browser = webdriver.Chrome()
browser.get('https://angel.co/login')

# try to login, if can't, I think I'll be pre-logged in
angel_email_input = browser.find_element_by_id('user_email')
angel_email_input.send_keys(angel_email_cred)
angel_password_input = browser.find_element_by_id('user_password')
angel_password_input.send_keys(angel_password_cred)
angel_password_input.submit()

# navigate to the jobs page this loads the relevant filters
browser.get('https://angel.co/jobs#find/f!%7B%22roles%22%3A%5B%22Data%20Scientist%22%5D%2C%22locations%22%3A%5B%221621-Boulder%2C%20CO%22%5D%2C%22remote%22%3Atrue%2C%22types%22%3A%5B%22full-time%22%2C%22contract%22%2C%22internship%22%5D%7D')

# #TODO: open the filters drop down and select the filters I want.
"""select relevant filters. Angel uses and/or filters it appears, so
I'm not worried about pre selected filters. Since I'm fine with post
match filtering I'll leave any pre-loaded ones on"""

# Time to step through the different job postings and click apply
time.sleep(5) # w/o sleep get a stale element reference error

# scroll to bottom of page | Load full page
SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#get the correct elements
jms = browser.find_elements_by_class_name('_jm')
print("number of jm elements: ", len(jms))

number_of_jobs = 0
for jm in jms[:1]:
    # this is needed to not navigate to a new window
    if 'applicants last week' in jm.text:
        jm.click()
        time.sleep(0.5)
        apply_now = jm.find_element_by_class_name('apply-now-button')
        if apply_now.text == 'Apply Now':
            number_of_jobs += 1
        company_name = jm.find_element_by_class_name('startup-link').text
        print(apply_now.text + ' | ' + company_name + ' | ' + str(number_of_jobs))
        time.sleep(0.5)
# After looking at this some, and seeing that it fails on some job postings,
# It seems like there is an issue with some job postings "attaching" themselves
# to a previous posting. It seems like they wrap a random number if jobs in a div
# this could be a scrolling issue? For now, I'm going to skip these
# #TODO: investigate more.
print(number_of_jobs)

# open application window
apply_now.click()
time.sleep(3)

# get recruiter's name
recruiting_contact = browser.find_element_by_class_name('recruiting-contact')
recruiter_name = recruiting_contact.find_element_by_class_name('name').text
print('recruiter_name = ', recruiter_name)
recruiter_name_list = recruiter_name.split(' ')
if len(recruiter_name_list) > 1:
    recruiter_name = recruiter_name_list[0]


with open('spiel.txt', 'r') as spiel_file:
    spiel = spiel_file.read()

new_spiel = recruiter_name + spiel

text_box = browser.find_element_by_tag_name('textarea')
print(text_box.is_displayed())

browser.execute_script("arguments[0].style.visibility = 'visible';", text_box)
print(text_box.is_displayed())

text_box.click()
text_box.send_keys(spiel)
