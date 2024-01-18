   
import RPi.GPIO as GPIO    
GPIO.setmode(GPIO.BOARD) 
from time import sleep 

Tast1=16                
Tast2=12                 
LED1=22                    
LED2=18
LED3=38


GPIO.setup(Tast1,GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(Tast2,GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(LED1,GPIO.OUT) 
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)

BS1=False                  
BS2=False                 
while(1):                 
        if GPIO.input(Tast1)==0:            
                print ("Tast1 war gedruckt:")
                if BS1==False:             
                        GPIO.output(LED1,True)
                        BS1=True               
                        sleep(.2)             
                else:                         
                        GPIO.output(LED1,False) 
                        BS1=False               
                        sleep(.2)
                        
        if GPIO.input(Tast2)==0: 
                print ("Tast2 war gedruckt:")
                if BS2==False:
                        GPIO.output(LED2,True)
                        BS2=True
                        sleep(.5)
                else:
                        GPIO.output(LED2,False)
                        BS2=False
                        sleep(.5)
                    
        if GPIO.input(Tast2)==1: 
                if BS2==True:
                        GPIO.output(LED3,True)
                        BS2=True 
                        sleep(.5)
                else:
                        GPIO.output(LED3,False)
                        BS2=False
                        sleep(.5)

       
