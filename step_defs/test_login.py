import time

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

scenarios('../features/login.feature')

@when(parsers.parse('the user goes to login page and enter username "{user}" and password "{passw}"'))
def login_u(browser,user,passw):
    browser.find_element('id', 'userName').send_keys(user)
    time.sleep(1)
    browser.find_element('id', 'password').send_keys(passw)
    time.sleep(1)

@when(parsers.parse('the user clicks on login button'))
def clicklog(browser):
    browser.find_element('id', 'login').click()
    time.sleep(1)

@then(parsers.parse('the user is logged in successfully'))
def regi():
    print("user logged in successfully")
