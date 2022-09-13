get_columns = []
columns = driver.find_elements_by_xpath("//*[@id='name']//th")
for i in columns:
  get_columns.append(i.text)
  
  for idx, cols in enumerate(get_columns):
    loggrt.info(f" {idx} column name {cols}")
  
  # check for table
  
  # click header
  driver.find_element_by_xpath("//*[@id='name']//th/lable[text()='" + cols + "']").click
  time.sleep(3)
  
  # get first row
  first_row =[]
  first_table_row = driver.find_element_by_xpath("//*[@id='name']//tr[1]/td")
  for i in first_table_row:
    first_row.append(i.text)
    
  # get last row
  last_row =[]
  last_table_row = driver.find_element_by_xpath("//*[@id='name']//tr[last()]/td")
  for i in last_table_row:
    last_row.append(i.text)
    
  # confirm sort
  print(f"The first row is {first_row{idx]} and the last row is {last_row{idx}}"
  self.assertTrue(first_row[idx] <= last_row[idx])
  
