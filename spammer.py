import pyautogui
import logging

import time

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

time.sleep(2)

for i in range (12):
     pyautogui.typewrite("kaise hai tu")
     pyautogui.press("enter")
