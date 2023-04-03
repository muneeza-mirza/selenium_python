import time

import pytest
from pytest import fixture
from pytest_bdd import given
from selenium import webdriver
import json

Product_store= 'https://demoqa.com/books'
login_store= 'https://demoqa.com/login'
form_store= 'https://demoqa.com/text-box'
tab_store= 'https://demoqa.com/browser-windows'


@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome('../chromedriver/chromedriver.exe')
    yield browser

@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b


@given('the Homepage is displayed')
def home_pg1(browser):
    browser.get(Product_store)


@given('the Homepage is login')
def home_pg2(browser):
    browser.get(login_store)

@given('the Homepage is form')
def home_pg3(browser):
    browser.maximize_window()
    browser.get(form_store)
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 1080)")

@fixture(scope='module')
@given('the website is open')
def home_pg4(browser):
    browser.get(tab_store)