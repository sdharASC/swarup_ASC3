paddleX = 400
paddleY = 0
paddleWidth = 80
paddleHeight = 8
paddleSpeed = 10

playerShooting = False
bulletX = 0
bulletY = 0
bulletSpeed = 10
bulletSize = 10 

def setup():
    global paddleY, paddleX, paddleWidth
    size(800, 500)
    noStroke()
    paddleY = height - 30
    paddleX = (width / 2) - (paddleWidth / 2)

def draw():
    global paddleX, paddleY, paddleWidth, paddleHeight, bulletX, bulletY, bulletSpeed, bulletSize, playerShooting
    background(0, 0, 0)
    fi
    rect(paddleX, paddleY, paddleWidth, paddleHeight)
    triangle(paddleX, paddleY, paddleX + paddleWidth/2, paddleY - 10, paddleX+paddleWidth, paddleY)
    
    if playerShooting == True:
        fill(0, 255, 255)
        ellipse(bulletX, bulletY, bulletSize, bulletSize)

def keyPressed():
    # see if the player pressed left or right arrow key and then move the ship to the right or left
    # right = 39, left = 37
    global paddleX, paddleY, paddleSpeed, paddleWidth, bulletX, bulletY, playerShooting
    if keyCode == 39:
        paddleX += paddleSpeed
    elif keyCode == 37:
        paddleX -= paddleSpeed
        
    # if the player is pressing space, then shoot
    if keyCode == 32:
        playerShooting = True
        bulletX = paddleX
        bulletY = paddleY
        
        
    # check if the paddle is going off the screen
    # if yes, then put the paddle in the screen
    if paddleX <= 0:
        paddleX = 0
    elif paddleX + paddleWidth >= width:
        paddleX = width - paddleWidth