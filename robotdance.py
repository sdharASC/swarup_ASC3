from Myro import *

speed = 1
seconds = 1

i = 0
while i < 3:
    turnBy(90)
    forward(speed, seconds)
    backward(speed, seconds)
    turnBy(180)
    forward(speed, seconds)
    i = i + 1
    turnBy(360)
    
    
i = 0
while i < 3:
    turnBy(90)
    backward(speed, seconds)
    forward(speed, seconds)
    i = i + 1