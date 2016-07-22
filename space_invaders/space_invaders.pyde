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

# 1: square, 2: triangle, 3: circle, 0 = dead
enemies = []
enemyStartX = 100
enemyStartY = 50
enemySize = 50
enemySpace = 10
enemySpeedX = 1
ex = enemyStartX
ey = enemyStartY
hits = 0

lost = False
menu = True
textY = 0

def setup():
    global paddleY, paddleX, paddleWidth, enemies
    size(800, 500)
    noStroke()
    paddleY = height - 30
    paddleX = (width / 2) - (paddleWidth / 2)
    # put all the enemies in the list
    enemies.append([1] * 10)
    enemies.append([1] * 10)
    enemies.append([1] * 10)
    enemies.append([0] * 4 + [1]* 2+ [0]*4)

def draw():
    global paddleX, paddleY, paddleWidth, paddleHeight, bulletX, bulletY, bulletSpeed, bulletSize, playerShooting
    global enemyStartX, enemyStartY, enemySize, enemySpace, enemies, enemySpeedX, ex, ey
    global hits, lost, menu, textY
    background(0, 0, 0)
    if menu == True:
        if textY < 50:
            textY += 1
        textSize(25)
        fill(textY * 4, textY * 3, textY)
        t = "Hurry! Aliens are trying to invade your home world!"
        tw = textWidth(t)
        text(t, width/2 - tw/2, textY)
        t = "Use left and right arrow keys to move"
        tw = textWidth(t)
        text(t, width/2 - tw/2, textY + 30)
        t = "and use the spacebar to shoot the invaders down."
        tw = textWidth(t)
        text(t, width/2 - tw/2, textY + 60)
    else:
        if lost == False:
            rect(paddleX, paddleY, paddleWidth, paddleHeight)
            triangle(paddleX, paddleY, paddleX + paddleWidth/2, paddleY - 10, paddleX+paddleWidth, paddleY)
            
            for y in range( len(enemies) ):
                for x in range( len(enemies[y]) ):
                    if enemies[y][x] == 1:
                        fill(255, 0, 0)
                        rect((x*enemySize+ex) + (x*enemySpace), (y*enemySize +ey) + (y*enemySpace), enemySize, enemySize)
        
        
            ex += enemySpeedX
            
            x = (len(enemies[0]))
            
            if  (x*enemySize+ex) + (x*enemySpace) >= width:
                enemySpeedX *= -1
                ey += enemySpace
            elif ex <= 0:
                enemySpeedX *= -1
                ey += enemySpace
            
            if playerShooting == True:
                fill(200, 33, 155)
                ellipse(bulletX, bulletY, bulletSize, bulletSize)
                bulletY -= bulletSpeed
                if bulletY <= 0:
                    playerShooting = False
                for y in range( len(enemies) ):
                    for x in range( len(enemies[y]) ):
                        if(enemies[y][x] == 1):
                            distance = dist(bulletX, bulletY, (x*enemySize+ex) + (x*enemySpace) + (enemySize/2), (y*enemySize +ey) + (y*enemySpace) + (enemySize/2))
                            if distance <= enemySize/2:
                                enemies[y][x] = 0
                                hits = hits + 1
                                playerShooting = False
                                break
                            
        if hits == 32:
            textSize(50)
            fill(200, 200, 33)
            text("You Win!", width/2, height/2)
        y = len(enemies)
        if (y*enemySize +ey) + (y*enemySpace)>= paddleY:
            lost = True
    
        if lost == True:
            textSize(30)
            fill(240, 230, 0)
            tW = textWidth("The aliens were able to invade successfully.")
            text("The aliens were able to invade successfully.", width/2 - tW/2, height/2)
    
    fill(255, 255, 255)

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
        if playerShooting == False:
            playerShooting = True
            bulletX = paddleX + paddleWidth/2
            bulletY = paddleY - 10
        
    # check if the paddle is going off the screen
    # if yes, then put the paddle in the screen
    if paddleX <= 0:
        paddleX = 0
    elif paddleX + paddleWidth >= width:
        paddleX = width - paddleWidth