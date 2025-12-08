import time 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


sayt = "https://www.google.com"

try:
    browser = webdriver.Chrome()
    browser.get(sayt)

    input1 = browser.find_element(By.CLASS_NAME, "gLFyf")
    input1.send_keys("Ivan")

    input1.send_keys(Keys.ENTER)

finally:

    time.sleep(100)
    browser.quit