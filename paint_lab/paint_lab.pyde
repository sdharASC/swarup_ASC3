#christina and swarup's code
r=color (255,0,0)
o=color (237,142,17)
y=color (237,237,17)
g=color (0,255,0)
b=color (0,0,255)
p=color (200,10,200)
w=color (255,255,255)
blck=color (0,0,0)
myColors = [r,o,y,g,b,p,w,blck]
pickColor = 0

def setup ():
    size(400,600)

def draw ():
    global myColors, pickColor
    # draw the color selections
    for i in range(len(myColors)):
        fill (myColors[i])
        rect(i*50,0,50,50)

    #check if the left mouse button is pressed
    if mouseButton == LEFT :
        if mouseY < 50 : #if the user is in the color choosing pallet
            for i in range(len(myColors)): # loop through the colors and see which color the user chose
                if(mouseX > i * 50 and mouseX < (i * 50)+ 50):
                    pickColor = i
                    break
        else : # the user is trying to paint
            fill (myColors[pickColor])
            ellipse(mouseX,mouseY,5,5)