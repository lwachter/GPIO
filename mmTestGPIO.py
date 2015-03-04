'''
Created on 04.08.2014

@author: wdaniel
'''

import RPi.GPIO as GPIO    # @UnresolvedImport
import time

GPIO.setwarnings(False)
        
GPIO.setmode(GPIO.BOARD)
        
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


GPIO.output(16, 0)
GPIO.output(18, 0)
GPIO.output(22, 0)
GPIO.output(24, 0)
GPIO.output(26, 1)

while(True):  
    GPIO.output(16, 1)
    time.sleep(0.1)
    GPIO.output(16, 0)
    
    GPIO.output(18, 1)
    time.sleep(0.2)
    GPIO.output(18, 0)
    
    GPIO.output(22, 1)
    time.sleep(0.4)
    GPIO.output(22, 0)
    
    GPIO.output(24, 1)
    time.sleep(0.8)
    GPIO.output(24, 0)