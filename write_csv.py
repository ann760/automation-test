# gather links for list
list = []
condition = Ture
while condition:
  list_el = driver.find_elements_by_class_name('classname')
  ppp = list_el[0]
  # loop through displayed list
  for idx, ppp in enumerate(issue_list):
    print(f " {idx]")
    ppp1 = ppp.find_elements_by_tag_name('a')[-1]
    list.append(ppp1.get_property('href'))
  # get the next page
  try:
    next_btn_el = driver.find_element_by_xpath("//*[@id='element-id']/div[3]/div/button[2]")
    disabled = next_btn_el.get_property('disabled')
  except:
    disabled = True
    
  # reset condition
  if disabled == False:
    next_btn_el.send_keys(Keys.ENTER)
    time.sleep(2)
    print(f" Next")
    condition = True
  else:
    condition = False
    print(f" End")

time.sleep(3)
print(f"Number of links list = {len(list)}")
    
# get all details
alldetail[]
for idx, i in enumerate(list):
  print(f" {idx}")
  # i is the href from above
  driver.get(i)
  # wait for page to load
  time.sleep(5)
  
  try:
    column1 = delay.until(EC.presence_of_element_location((By.XPATH, "//*id='element-id))).text
  except TimeoutException:
    column1 = 'None'
                                     
  try:
    column2 = delay.until(EC.presence_of_element_location((By.XPATH, "//*id='element-id))).text
  except TimeoutException:
    column2 = 'None'
  
  try:
    column3 = delay.until(EC.presence_of_element_location((By.XPATH, "//*id='element-id))).text
  except TimeoutException:
    column3 = 'None'
  
  tempJ = {'column1' : column1,
           'column2' : column2,
           'column3' : column3,}
  alldetails.append(tempJ)
  
# write to csv
csv_columns = ['column1, column2, column3]
try:
  with open(csv_file, 'w') as csvfile:
  thewriter = csv.DictWriter(csvfile, fieldnames=csv_columns)
  thewrither.writeheader()
  
  for issue in alldetails:
      thewriter.writerow(issue)
except IOError:
      print(f"I/O Error")
               
# close browser
driver.quit()
print(f" DONE")
