import logging
import os
import sys 
from datetime import datetime

filename = (os.path.basename(sys.argv[0]).split('.')[0])
print(filename)

class log_gen:
  @staticmethod
  def logen(__name__):
    logger = logging.getLogger(__name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFromantter(formantter)
    
    file_handler = loggin.FileHandler(os.path.join(f'logs/{datetime.now():%Y-%m-%d %H-%M-%S}-{filename}.log'), 'w', 'utf-8')    
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)  
    logger.addhandler(stdout_handler)
    
    return logger
