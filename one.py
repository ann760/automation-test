# Steps
# 1 download python
# 2 check pip package is installed by typing pip into the cmd  
# 3 install selenium by typing pip3 install selenium into the cmd
# 4 install webdriver-manager by typing pip3 install webdriver-manager into the cmd
# 5 install msedge-selenium-tools by typing pip3 install msedge-selenium-tools selenium==3.141
# 6 get webdriver and place into the path 

#Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

#Other imports
import getpass
import os
import time


PATH = r'C:/Users/annie/Documents/code/drivers/chromedriver.exe'
# driver = webdriver.Edge(PATH)

# driver = webdriver.Edge(r'C:/Users/annie/Documents/code/drivers/msedgedriver.exe')


# options = Options()
# options.binary_location = r"C:/Users/annie/Documents/code/drivers/msedgedriver.exe"
# driver = webdriver.Edge(options = options)


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


#Log in to insta
# my_password = getpass.getpass("What is your password?")
driver.get("https://www.google.com/")
print(driver.title)

search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'q')))
search_field.clear()
search_field.send_keys("cats")

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btnk'))).click()
time.sleep(5)
# driver.quit()
