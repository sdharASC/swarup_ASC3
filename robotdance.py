# Robot dance to Mr. C the slide man Cha Cha Song

from Myro import *

speed = 1
seconds = .5

i = 0
step = 0

while step < 2:

    while i < 3:
        turnBy(90)
        backward(speed, seconds + 1)
        turnBy(20)
        turnBy(-40)
        backward(speed, seconds)
        turnBy(180)
        forward(speed, seconds)
        i = i + 1
        turnBy(360)
        
        
    i = 0
    while i < 3:
        turnBy(-90)
        backward(speed, seconds)
        forward(speed, seconds)
        i = i + 1
        
    step = step + 1