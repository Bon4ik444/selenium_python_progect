import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By



try:
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/upload-download")


    xr = browser.find_element(By.ID, "downloadButton")
    xr.click()

    element = browser.find_element(By.ID, "uploadFile")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, "sampleFile.jpeg")           # добавляем к этому пути имя файла 
    element.send_keys(file_path)


finally: 

    time.sleep(10)
    browser.quit()
    