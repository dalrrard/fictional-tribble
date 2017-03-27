#! python3
# commandLineEmailer.py - email from command line

from selenium import webdriver
import sys
import time

if len(sys.argv) > 2:
    # get email address and message
    email = sys.argv[1]
    message = ' '.join(sys.argv[2:])
else:
    print('Usage - example@example.com How is your day going?')
    sys.exit()

browser = webdriver.Firefox()
browser.get('http://mail.google.com')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('example@example.com')
emailElem.submit()

time.sleep(1)

passwordElem = browser.find_element_by_name('Passwd')
passwordElem.send_keys('Password')
passwordElem.submit()

time.sleep(4)

composeElem = browser.find_element_by_xpath("//*[contains(text(), 'COMPOSE')]")
composeElem.click()

time.sleep(1)

toFieldElem = browser.find_element_by_class_name('vO')
toFieldElem.send_keys(email)

time.sleep(1)

bodyFieldElem = browser.find_element_by_class_name('LW-avf')
bodyFieldElem.send_keys(message)

sendElem = browser.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO T-I-atl L3']")
sendElem.click()