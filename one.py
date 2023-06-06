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

from selenium.webdriver.edge.service import Service as eService
from selenium.webdriver.edge.options import Options as eOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

#Other imports
import getpass
import os
import time


# # start edge browser
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
# edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')
# edge_service = eService(edge_driver_path)
# edge_options = eOptions()
# edge_options.add_argument(f'user=agent={user_agent}')
# driver = webdriver.Edge(service=edge_service, options=edge_options)
# driver.maximize_window()

# start chrome browser
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# use getpadd
# my_password = getpass.getpass("What is your password?")

# navigate to google
driver.get("https://www.google.com/")
print(driver.title)

# search for cats
search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'q')))
search_field.clear()
search_field.send_keys("cats")
search_field.send_keys(Keys.ENTER)

time.sleep(15)
# driver.quit()
