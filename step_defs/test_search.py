import time

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

Product_store= 'https://demoqa.com/books'

scenarios('../features/search.feature')

@when(parsers.parse('the user enters valid name of the book "{phrase}"'))
def login_u(browser,phrase):
    browser.find_element('id', 'searchBox').send_keys(phrase)
    time.sleep(1)

@then(parsers.parse('the user should see that book'))
def regi(browser):
    if browser.find_element('xpath', '//*[@id="see-book-Git Pocket Guide"]/a'):
        print("Book exists")

@when(parsers.parse('the user enters name of the book "{phrase}" and clicks on it'))
def login_u(browser,phrase):
    browser.find_element('id', 'searchBox').send_keys(phrase)
    time.sleep(1)
    browser.find_element('xpath', '//*[@id="see-book-Git Pocket Guide"]/a').click()

@then(parsers.parse('the user should see book details'))
def regi(browser):
    if browser.find_element('xpath','//*[@id="userName-value"]'):
        print("Book details")

