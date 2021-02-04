# pip install selenium
# selenium is an old tool of web automation and testing which is written in java but we have its python binding as well.
# selenium needs web driver (each browser has its web driver). Install it first.
# get() function is used to open any particular URL in browser
# find_element_by_id() function is used to select element by its ID
# send_keys() function is used to send the values to the element
# click() function is used to click any button

## THIS CODE WILL LOGIN TO FACEBOOK ACCOUNT AND LET YOU POST THE CONTENT ##

import time
from selenium import webdriver

# To automatically block the notifications on browser window
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs", prefs)

# To start a browser session
browser = webdriver.Chrome(options=options)   # Creating a browser object for Chrome. The browser window will open after execution of this line. If doesn't open, we need to specify the complete path of driver's exe file inside panathesis inside ""

browser.maximize_window()   # To maximize the window

# To open a webpage
browser.get("https://www.facebook.com/")     # Opening the given URL

# Now for doing authentication, we need to check where we have to send username/email/mobile and password. For this, inspect the elements of the webpage
username_element = browser.find_element_by_id("email")      # selecting the username element(field) by its id
user = input("Enter the email address or phone number: ")       # Getting email/phone number from user
username_element.send_keys(user)                        # passing email/phone number to the email/phone number element(field)

password_element = browser.find_element_by_id("pass")      # selecting the password element(field) by its id
from getpass import getpass                                     # Using getpass to hide the password while entering
password_element.send_keys(getpass("Enter password: "))         # passing password to the password element(field)
browser.find_element_by_id("u_0_b").click()                     # clicking the login button
time.sleep(5)                                                   # waiting for 5s to load the page

# Clicking on the form for posting the content
browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span').click()

ques_text = input("Want to write the post? (y/n): ")

if ques_text == 'y':
    post_text_element = browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')    # Selecting the textarea to write the post
    post = input("Enter the text: ")                    # Getting text from user
    post_text_element.send_keys(post)                   # Adding text to the textarea

ques_pic = input("Want to post a picture? (y/n): ")

if ques_pic == 'y':
    post_pic_element = browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/span/div/div/div/div/div[1]/i').click()      # Clicking the upload button to upload the picture

confirm = input("Are you confirm to post the content? (y/n): ")

if confirm == 'y':      # Confirming whether user wants to post the content or not
    post_element = browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]/div/span/span').click()
else:
    browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[1]/div[1]/div[2]/div/i').click()
