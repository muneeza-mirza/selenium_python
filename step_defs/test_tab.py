import time

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

scenarios('../features/newTab.feature')

@pytest.mark.usefixtures("home_pg4")
@when(parsers.parse('the user clicks on new tab'))
def cklog(browser):
    browser.find_element('id', 'tabButton').click()
    time.sleep(2)

@then(parsers.parse('the user should see a new tab open'))
def regi():
    print("opened New tab")


@when(parsers.parse('the user clicks on new window'))
def cklog(browser):
    browser.find_element('id', 'windowButton').click()
    time.sleep(2)

@then(parsers.parse('the user should see a new window open'))
def regi():
    print("opened New window")


@when(parsers.parse('the user clicks on new window message'))
def cklog(browser):
    browser.find_element('id', 'messageWindowButton').click()
    time.sleep(2)

@then(parsers.parse('the user should see a pop up message'))
def regi():
    print("New window message displayed")