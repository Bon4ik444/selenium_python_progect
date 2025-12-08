from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

sayt = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(sayt)

    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button1.click()


    browser.switch_to.window("")
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    x_element = browser.find_element(By.ID, "input_value")
    z = x_element.text
    y = calc(int(z))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    button7 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button7.click()



finally:

    time.sleep(10)
    browser.quit()
    