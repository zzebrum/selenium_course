from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    #parser.addoption('--browser_name', \
                    #action = 'store', \
                   # default = "chrome", \
                   # help = "Choose browser:chrome or firefox")
    parser.addoption('--language', \
                    action = 'store', \
                    default = None, \
                    help = "Choose language: ru, en, ...")


@pytest.fixture(scope = "function")
def browser(request):
    #browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    #if user_language == "chrome":
    options = Options()
    options.add_experimental_option('prefs', \
                                    {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()