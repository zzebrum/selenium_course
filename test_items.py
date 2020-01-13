from selenium import webdriver
import pytest
import time

def test_lang(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert button is not None, "no button"
    time.sleep(10)

