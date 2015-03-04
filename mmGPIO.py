'''
Created on 09.07.2014

@author: wdaniel
'''
import RPi.GPIO as GPIO    # @UnresolvedImport
import time

class GPIO_Sync():
    _dict_Pins = {'Pin0': 16, 'Pin1': 18, 'Pin2': 22, 'Pin3':24}
    
    _dict_num2id =  {'0': 0b0001, '1': 0b0010, '2': 0b0011, '3':0b0100,
                     '4': 0b0101, '5': 0b0110, '6': 0b0111, '7':0b1000,
                     '8': 0b1001, '9': 0b1010, 'Datum': 0b1100, 'Zeit': 0b1101,
                     'a': 0b1110, 'Sync': 0b1111}

    def __init__(self,time_on):
        GPIO.setwarnings(False)
        
        # Needs to be BCM. GPIO.BOARD lets you address GPIO ports by periperal
        # connector pin number, and the LED GPIO isn't on the connector
        GPIO.setmode(GPIO.BOARD)
        
        # set up GPIO output channel
        GPIO.setup(self._dict_Pins['Pin0'], GPIO.OUT)
        GPIO.setup(self._dict_Pins['Pin1'], GPIO.OUT)
        GPIO.setup(self._dict_Pins['Pin2'], GPIO.OUT)
        GPIO.setup(self._dict_Pins['Pin3'], GPIO.OUT)
        
        self.setAllSimple(0)   
        
        self.arr_date = self.num2binarray(self._dict_num2id['Datum'])
        self.arr_time = self.num2binarray(self._dict_num2id['Zeit'])
        self.arr_sync = self.num2binarray(self._dict_num2id['Sync']) 
        
        self.time_on = time_on
        
    def num2binarray(self,num):
        return list(bin(num+16)[3:])
    
    def setAllSimple(self,ledState):
        GPIO.output(self._dict_Pins['Pin0'], ledState)
        GPIO.output(self._dict_Pins['Pin1'], ledState)    
        GPIO.output(self._dict_Pins['Pin2'], ledState)    
        GPIO.output(self._dict_Pins['Pin3'], ledState)      
        
    def setArray(self,array):
        GPIO.output(self._dict_Pins['Pin0'], int(array[3]))
        GPIO.output(self._dict_Pins['Pin1'], int(array[2]))    
        GPIO.output(self._dict_Pins['Pin2'], int(array[1]))    
        GPIO.output(self._dict_Pins['Pin3'], int(array[0])) 
        
    def writeDateArray(self,date_str):
        self.setArray(self.arr_date)
        time.sleep(self.time_on)
        for character in date_str:
            arr_info = self.num2binarray(self._dict_num2id[character])
            self.setArray(arr_info)
            time.sleep(self.time_on)
            
    def writeTimeArray(self,time_str):
        self.setArray(self.arr_time)
        time.sleep(self.time_on)
        for character in time_str:
            arr_info = self.num2binarray(self._dict_num2id[character])
            self.setArray(arr_info)
            time.sleep(self.time_on)
            
    def writeOff(self):
        self.setAllSimple(0)   
        
    def writeSyncArray_start(self):
        self.setArray(self.arr_sync)
        
    def writeSyncArray_wait(self):
        time.sleep(self.time_on)
            
if __name__=='__main__':
    from datetime import datetime

    time_on = 0.1-0.0025
    sync = GPIO_Sync(time_on)
    
    time.sleep(5)

    datetime_now = datetime.now()
    date_str= datetime_now.strftime("%Y%m%d")
    time_str = datetime_now.strftime("%H%M%S%f")[:9]
    print(date_str)
    print(time_str)
    
    sync.writeDateArray(date_str)
    sync.writeTimeArray(date_str)
    sync.writeOff()
    
    while(True):  
        time.sleep(16)
        sync.writeSyncArray()
        sync.writeOff()
    
