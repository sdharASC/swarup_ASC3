from Myro import *

init("sim")

right = -90
left = 90

def drawP():
    penDown()
    forward(1, 2)
    turnBy(right)
    forward(1, 1)
    turnBy(right)
    forward(1, 1)
    turnBy(right)
    forward(1, 1)
    turnBy(left)
    forward(1, 1)
    penUp()
    turnBy(left)
    
    
def drawO():
    penDown()
    forward(1, 2)
    turnBy(right)
    forward(1, 1)
    turnBy(right)
    forward(1, 2)
    turnBy(right)
    forward(1, 1)
    penUp()
    turnBy(180)

def drawK():
    penDown()
    forward(1, 2)
    turnBy(180)
    forward(1, 1)
    turnBy(140)
    forward(1, 1)
    turnBy(180)
    wait(0.1)
    forward(1, 1.1)
    turnBy(80)
    wait(0.1)
    forward(1, 1.1)
    penUp()
    turnBy(50)

#turnBy(50)

def drawE():
    penDown()
    forward(1, 1.5)
    backward(1, 1.5)
    turnBy(left)
    forward(1, 1)
    turnBy(right)
    forward(1, 1)
    backward(1, 1)
    turnBy(left)
    forward(1, 1)
    turnBy(right)
    forward(1, 1.5)
    penUp()
    turnBy(right)
    forward(1, 2)
    turnBy(left)
    
    

drawE()