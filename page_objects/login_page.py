# imports 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdrive.suppoert import expected_conditions as EC

import time

class login:
  # veriables
  delay = WebdriverWait(self.driver, 3)
  username_field_id = "username"
  password_field_id = "password"
  login_btn_id = "loginBtn"
  
  def enter_username(self, username):
    delay = WebdriverWait(self.driver, 3)
    username_field = delay.until(EC.element_to_be_clickable((By.ID, login.username_field_id)))
    username.clear()
    username_field.send_keys(username)
    
  def enter_username(self, username):
    delay = WebdriverWait(self.driver, 3)
    password_field = delay.until(EC.element_to_be_clickable((By.ID, login.password_field_id)))
    password.clear()
    password_field.send_keys(password)
    
  def click_login(self):    
    delay.until(EC.element_to_be_clickable((By.ID, login.login_btn_id))).click()
    
  def login(self, username, password):
    try:
      login.enter_username(self, username)
      login.enter_password(self, password)
      login.click_login(slef)
      time.sleep(3)
      login_page_element = delay.until(EC.element_to_be_clickable((By.ID, element.login_element_id)))
      Return True, f "Login successful"
    except TimeoutException:
      login_error_msg = delay.until(EC.element_to_be_clickable((By.ID, element.login_msg_id)))
      return False, f" {login_error_msg}"
    
    def start_driver(self, browser, url):
      try:
        if browser == "firefox":
          self.driver == webdriver.Firefox(executable_path=".\driver\geckodriver.exe")
          driver = self.driver
          driver.get(url)
        elif browser == "chrome":
          options = webdriver.ChromeOption()
          options.add_argument('--ignore-certificates-errors')
          options.add_argument('--ignore-ssl-errors')
          self.driver == webdriver.Chrome(PATH, options=options)
          driver = self.driver
          driver.get(url
        elif browser == "edge":
          driver = self.driver
          driver.get(url)
        else:
          return False, f"Driver Unknown"
         return True, f" {url} opened with {browser} browser."            
     except TimeoutExcption:
          return False, f" Driver failed"
    
    
