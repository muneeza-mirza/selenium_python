import time

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

scenarios('../features/form.feature')

@when(parsers.parse('the user goes to page and enter name "{name}", email "{email}", current address "{cadd}" and permanent address "{padd}"'))
def login_u(browser,name,email,cadd,padd):
    browser.find_element('id', 'userName').send_keys(name)
    time.sleep(1)
    browser.find_element('id', 'userEmail').send_keys(email)
    time.sleep(1)
    browser.find_element('id', 'currentAddress').send_keys(cadd)
    time.sleep(1)
    browser.find_element('id', 'permanentAddress').send_keys(padd)
    time.sleep(1)

@when(parsers.parse('the user clicks on submit button'))
def cklog(browser):
    element=browser.find_element('xpath', '//*[@id="submit"]')
    time.sleep(1)
    element.location_once_scrolled_into_view
    element.click()

@then(parsers.parse('the user can see details below'))
def regi():
    print("Details")
