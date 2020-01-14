from selenium import webdriver
import pytest
import time

def test_lang(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = len(browser.find_elements_by_css_selector("#add_to_basket_form>.btn"))
    assert button > 0, "no button"
