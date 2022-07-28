import logging
import os
import sys 
from datetime import datetime

class log_gen:
  @staticmethod
  def logen(__name__):
    loggin.basicConfig(filename=os.path.join(f'logs/{datetime.now():%Y-%m-%d %H-%M-%S}-{sys.arvg{0}}.log'), format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    logging.basicConfig(logging.INFO)
    # file_handler = loggin.FileHandler(f'logs/{datetime.now():%Y-%m-%d %H-%M-%S}-{sys.arvg{0}}.log')
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    # file_handler.setFormatter(formatter)
    # logger.addHandler(filrhandler)    
    return logger
    
  
