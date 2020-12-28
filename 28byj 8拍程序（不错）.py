import RPi.GPIO as g
import time
in4=5
in3=6
in2=13
in1=19
waittime=0.001
g.setmode(g.BCM)
g.setup(in4,g.OUT)
g.setup(in3,g.OUT)
g.setup(in2,g.OUT)
g.setup(in1,g.OUT)
def setpulse(i4,i3,i2,i1):
    global in4,in3,in2,in1
    g.output(in4,i4)
    g.output(in3,i3)
    g.output(in2,i2)
    g.output(in1,i1)

def zheng():
    global waittime
    setpulse(1,0,0,0)
    time.sleep(waittime)
    setpulse(1,1,0,0)
    time.sleep(waittime)
    setpulse(0,1,0,0)
    time.sleep(waittime)
    setpulse(0,1,1,0)
    time.sleep(waittime)
    setpulse(0,0,1,0)
    time.sleep(waittime)
    setpulse(0,0,1,1)
    time.sleep(waittime)
    setpulse(0,0,0,1)
    time.sleep(waittime)
    setpulse(1,0,0,1)
    time.sleep(waittime)
def fan():
    global waittime
    setpulse(1,0,0,0)
    time.sleep(waittime)
    setpulse(1,0,0,1)
    time.sleep(waittime)
    setpulse(0,0,0,1)
    time.sleep(waittime)
    setpulse(0,0,1,1)
    time.sleep(waittime)
    setpulse(0,0,1,0)
    time.sleep(waittime)
    setpulse(0,1,1,0)
    time.sleep(waittime)
    setpulse(0,1,0,0)
    time.sleep(waittime)
    setpulse(1,1,0,0)
    time.sleep(waittime)
    
for i in range(1000):
   
    zheng()
for i in range(1000):  
    fan()
    
    
    