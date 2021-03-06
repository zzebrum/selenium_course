from selenium import webdriver
import pytest
import time

def test_add_button_availability_in_different_languages(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements_by_css_selector("#add_to_basket_form>.btn")
    assert len(button) > 0, "no button"
