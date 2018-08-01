import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def get_files():
    # get the spiel_auto text
    with open('spiel_auto.txt', 'r') as spiel_file:
        spiel_auto = spiel_file.read()

    # get the spiel_manual text
    with open('spiel_manual.txt', 'r') as spiel_file:
        spiel_manual = spiel_file.read()

    # get the filtered URL
    with open('html.txt', 'r') as html_file:
        filtered_html = html_file.read()

    return spiel_auto, spiel_manual, filtered_html


def get_creds():
    # get login creds
    angel_creds = np.genfromtxt('angel_creds.csv', delimiter=',', dtype=str)
    angel_email_cred = angel_creds[0]
    angel_password_cred = angel_creds[1]

    return angel_email_cred, angel_password_cred


def get_broswer_and_login(angel_email_cred, angel_password_cred,
                          filtered_html):
    # create browser object, navigate to login
    browser = webdriver.Chrome()
    browser.get('https://angel.co/login')

    # try to login, if can't, I think I'll be pre-logged in
    try:
        angel_email_input = browser.find_element_by_id('user_email')
        angel_email_input.send_keys(angel_email_cred)
        angel_password_input = browser.find_element_by_id('user_password')
        angel_password_input.send_keys(angel_password_cred)
        angel_password_input.submit()
    except Exception as e:
        print(e)
        pass

    # navigate to the jobs page this loads the relevant filters
    browser.get(filtered_html)

    return browser


# #TODO: open the filters drop down and select the filters I want.
"""select relevant filters. Angel uses and/or filters it appears, so
I'm not worried about pre selected filters. Since I'm fine with post
match filtering I'll leave any pre-loaded ones on"""


def scroll_through_page(browser):
    # scroll to bottom of page | Load full page
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        print('Scrolling...')
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def apply_to_job(apply_now, spiel, browser):
    # open application window
    apply_now.click()
    time.sleep(3)

    # get recruiter's name
    recruiting_contact = browser.find_element_by_class_name('recruiting-contact')
    recruiter_name = recruiting_contact.find_element_by_class_name('name').text
    recruiter_name_list = recruiter_name.split(' ')
    if len(recruiter_name_list) > 1:
        recruiter_name = recruiter_name_list[0]

    new_spiel = recruiter_name + ',\n\n' + spiel

    text_box_div = browser.find_element_by_class_name('_1xXo9j7wJhYoCN1vk_CNsT')
    text_box = text_box_div.find_element_by_tag_name('textarea')

    text_box.click()
    text_box.send_keys(new_spiel)

    submit_button = text_box_div.find_element_by_class_name('c-button--blue')
    submit_button.click()

    time.sleep(2)
    close_section = browser.find_element_by_class_name('_3Aslx7L3GVI4XM7PUyYKza')
    close_button = close_section.find_element_by_class_name('c-button--blue')
    close_button.click()
    time.sleep(2)
    return recruiter_name


def step_through_jobs(browser, spiel_auto, spiel_manual):
    # get the correct elements
    jms = browser.find_elements_by_class_name('_jm')
    print("number of jm elements: ", len(jms))

    number_of_jobs = 1

    for jm in jms:
        # this is needed to not navigate to a new window
        if 'applicants last week' in jm.text:
            if number_of_jobs % 2:
                spiel = spiel_auto
            else:
                spiel = spiel_manual
            jm.click()
            company_name = jm.find_element_by_class_name('startup-link').text
            time.sleep(3)
            apply_now = jm.find_element_by_class_name('apply-now-button')
            if apply_now.text == 'Apply Now':
                try:
                    recruiter_name = apply_to_job(apply_now, spiel, browser)
                except:
                    recruiter_name = "Dear Hiring Manager,"
                print(company_name + ' | ' + str(number_of_jobs) + ' | ' +
                      recruiter_name)
                time.sleep(2)
                number_of_jobs += 1

    print(number_of_jobs)



# After looking at this some, and seeing that it fails on some job postings,
# It seems like there is an issue with some job postings "attaching"
# themselves to a previous posting. It seems like they wrap a random number if
# jobs in a div this could be a scrolling issue? For now, I'm going to skip
# these
# #TODO: investigate more.


def main():
        spiel_auto, spiel_manual, filtered_html = get_files()
        angel_email_cred, angel_password_cred = get_creds()

        browser = get_broswer_and_login(angel_email_cred, angel_password_cred,
                                        filtered_html)

        # Time to step through the different job postings and click apply
        time.sleep(5)  # w/o sleep get a stale element reference error

        scroll_through_page(browser)

        step_through_jobs(browser, spiel_auto, spiel_manual)


if __name__ == '__main__':
    main()
