from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = ('https://suninjuly.github.io/selects1.html')




try:
    opkloze = webdriver.Chrome()
    opkloze.get(link)

    num1 = opkloze.find_element(By.ID, 'num1')
    num2 = opkloze.find_element(By.ID, 'num2')

    x1 = num1.text
    x2 = num2.text
    y = int(x1) + int(x2)

    select = Select(opkloze.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(y)) # ищем элемент с текстом "Python"

    button = opkloze.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()
finally:
    time.sleep(10)
    opkloze.quit()
