from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    #browser.implicitly_wait(10)
    browser.get(link)

    x = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    button1 = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    el = browser.find_element_by_id("input_value")
    x = el.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    button1.click()

finally:
    time.sleep(15)
    browser.quit()