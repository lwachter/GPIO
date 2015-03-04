'''
Created on 09.07.2014

@author: wdaniel
'''
import RPi.GPIO as GPIO    # @UnresolvedImport
import time

class GPIO_Simple():
    def __init__(self,time_on,pin_id):
        GPIO.setwarnings(False)
        
        self._dict_pin_id = pin_id
        
        # Needs to be BCM. GPIO.BOARD lets you address GPIO ports by periperal
        # connector pin number, and the LED GPIO isn't on the connector
        GPIO.setmode(GPIO.BOARD)
        
        # set up GPIO output channel
        GPIO.setup(self._dict_pin_id, GPIO.OUT)

        self.setSimple(0)   
        
        self.time_on = time_on
    
    def setSimple(self,ledState):
        GPIO.output(self._dict_pin_id, ledState)
        
    def writeOutput(self,cnt):
        
        for _ in range(cnt):
            self.setSimple(1)
            time.sleep(self.time_on)
            self.setSimple(0)
            time.sleep(self.time_on)
            
    def writeStart(self):
        self.setSimple(1)
        
#    def writeOff(self):
#        self.setSimple(0)   
        
            
if __name__=='__main__':

    time_on = 0.1-0.0025
    sync = GPIO_Simple(time_on,22)
    cnt = 0
    
    while(True): 
        cnt = cnt % 4
        cnt +=1 
        sync.writeStart()
        sync.writeOutput(cnt)
    
        time.sleep(5)
