import RPi.GPIO as gpio
import time
class stepmotor:
    def __init__(self,p1,p2,p3,p4):
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(p1,gpio.OUT)
        gpio.setup(p2,gpio.OUT)
        gpio.setup(p3,gpio.OUT)
        gpio.setup(p4,gpio.OUT)
        self.i1=p1
        self.i2=p2
        self.i3=p3
        self.i4=p4
        
    def __setStep(self,w1,w2,w3,w4):
        gpio.output(self.i1,w1)
        gpio.output(self.i2,w2)
        gpio.output(self.i3,w3)
        gpio.output(self.i4,w4)
    def __stop(self):
        self.__setStep(0,0,0,0)
    def forward(self,delay,steps):#from in1 to in4 ,GPIO.HIGH
        for i in range(0,steps,1):
            self.__setStep(1,0,0,0)
            time.sleep(delay)
            self.__setStep(0,1,0,0)
            time.sleep(delay)
            self.__setStep(0,0,1,0)
            time.sleep(delay)
            self.__setStep(0,0,0,1)
            time.sleep(delay)
        self.__stop()
    def backward(self,delay,steps):#from in4 to in1,GPIO.HIGH,if steps=512 cycle=360 a round
        for i in range(0,steps,1):
            self.__setStep(0,0,0,1)
            time.sleep(delay)
            self.__setStep(0,0,1,0)
            time.sleep(delay)
            self.__setStep(0,1,0,0)
            time.sleep(delay)
            self.__setStep(1,0,0,0)
            time.sleep(delay)
        self.__stop()
