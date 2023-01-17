# Steps
# 1 download python
# 2 check pip package is installed by typing pip into the cmd  
# 3 install selenium by typing pip3 install selenium into the cmd
# 4 install webdriver-manager by typing pip3 install webdriver-manager into the cmd
# 5 get webdriver and place into the path 

#Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

#Other imports
import os
import getpass


PATH = r"C:\Users\annie\Documents\code\drivers\chromedriver.exe"
# driver = webdriver.Edge(PATH)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


#Log in to insta
my_password = getpass.getpass("What is your password?")
driver.get("https://www.instagram.com/")
print(driver.title)
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name= 'username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name= 'password']")))

username.clear()
password.clear()
username.send_keys("anniedillier@gmail.com")
password.send_keys(my_password)

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type= 'submit']"))).click()
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
# driver.quit()
