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

enemies = [] # 1 is alive 0 is dead
enemyStartX = 100
enemyStartY = 50
enemySize = 50
enemySpace = 10
enemySpeedX = 1
enemyMaxSpeed = 1.5
ex = enemyStartX
ey = enemyStartY

hits = 0
lost = False

menu = True
aboutMenu = False
textY = 0
menuShips = True
menuShipsY = 0

def setup():
    global paddleY, paddleX, paddleWidth, enemies, ex, ey, hits, lost, enemyStartX, enemyStartY, enemySpeedX
    size(800, 500)
    noStroke()
    
    # put all the enemies in the list
    enemies = []
    enemies.append([1] * 10)
    enemies.append([1] * 10)
    enemies.append([1] * 10)
    enemies.append([0] * 4 + [1]* 2+ [0]*4)
    
    # set up the variables
    paddleY = height - 30
    paddleX = (width / 2) - (paddleWidth / 2)
    ex = enemyStartX
    ey = enemyStartY
    lost =False
    hits = 0
    enemySpeedX = 1

# reset all variables
def reset():
    global paddleY, paddleX, paddleWidth, enemies, ex, ey, hits, lost, enemyStartX, enemyStartY, enemySpeedX
    enemies = []
    enemies.append([1] * 10)
    enemies.append([1] * 10)
    enemies.append([1] * 10)
    enemies.append([0] * 4 + [1]* 2+ [0]*4)
    paddleY = height - 30
    paddleX = (width / 2) - (paddleWidth / 2)
    ex = enemyStartX
    ey = enemyStartY
    lost =False
    hits = 0
    enemySpeedX = 1

# check if any of the alive enemies cross the red line
# also check if any of the alive enemies bump the edges of the window
# also see if the bullet is hitting any of the enemies
def checkEnemies():
    global enemies, enemySpeedX, ex, ey, enemySize, enemySpace, paddleY, lost, bulletX, bulletY, playerShooting, hits, enemyMaxSpeed
    for y in range( len(enemies) ):
        for x in range( len(enemies[y]) ):
            if enemies[y][x] == 1: # if the enemy is alive
                xPos = (x*enemySize+ex) + (x*enemySpace)
                yPos = (y*enemySize +ey) + (y*enemySpace)
                # if the aliens penetrated the line then the player is lost
                if yPos + enemySize > paddleY + 2:
                    lost = True
                    return
                if xPos + enemySize > width:
                    # if aliens are bumping the right edge of the window then reverse direction
                    if enemySpeedX < enemyMaxSpeed:
                        enemySpeedX *= -1.2 # reverse and speed up a bit
                    else:
                        enemySpeedX *= -1
                    ey += enemySpace # move down
                    return
                elif xPos < 0:
                    if enemySpeedX < enemyMaxSpeed:
                        enemySpeedX *= -1.2 # reverse and speed up a bit
                    else:
                        enemySpeedX *= -1
                    ey += enemySpace
                    return
                # check if the bullet is hitting the enemy
                if bulletX >= xPos and bulletX <= xPos + enemySize and bulletY >= yPos and bulletY <= yPos + enemySize:
                    enemies[y][x] = 0 # the enemy is dead
                    hits = hits + 1
                    playerShooting = False # allow player to shoot again
                    bulletY = -1 # reset the bullet's position

def draw():
    global paddleX, paddleY, paddleWidth, paddleHeight, bulletX, bulletY, bulletSpeed, bulletSize, playerShooting
    global enemyStartX, enemyStartY, enemySize, enemySpace, enemies, enemySpeedX, ex, ey
    global hits, lost, menu, textY, aboutMenu, menuShips, menuShipsY
    # clear background
    background(0, 0, 0)
    # if the user is in the menu
    if menu == True:
        # show the ships if this is the first time opening the menu
        if menuShips == True:
            if menuShipsY < height:
                menuShipsY += 3
            else:
                menuShips = False
            for i in range(10):
                fill(255, 0, 0)
                rect(i * enemySize + i * enemySpace + enemyStartX, menuShipsY + enemyStartY, enemySize, enemySize)
                rect(i * enemySize + i * enemySpace + enemyStartX, menuShipsY + enemyStartY - enemySize*2, enemySize, enemySize)
        else: #menu text
            if textY < 50:
                textY += 2
            textSize(25)
            fill(textY * 4, textY * 4, textY/2)
            t = "Hurry! Aliens are trying to invade your home world!"
            tw = textWidth(t)
            text(t, width/2 - tw/2, textY)
            t = "Use left and right arrow keys to move"
            tw = textWidth(t)
            text(t, width/2 - tw/2, textY + 30)
            t = "and the spacebar to shoot the invaders down."
            tw = textWidth(t)
            text(t, width/2 - tw/2, textY + 60)
            t = "Beware! If any of the aliens cross the red line,"
            tw = textWidth(t)
            text(t, width/2 - tw/2, textY + 90)
            fill(200, 30, 45)
            t = "they will take over your planet!"
            tw = textWidth(t)
            text(t, width/2 - tw/2, textY + 90 + 30)
            t = "About                   Play>"
            tw = textWidth(t)
            fill(0, 255, 30)
            text(t, width/2 - tw/2, height - textY + 10)
            if mouseButton == LEFT:
                # see if user is clicking on the 'about' button
                if mouseX >= 250 and mouseX <= 325 and mouseY >= 445 and mouseY <=460:
                    menu = False
                    aboutMenu = True
                    textY = 0
                # see if user is clicking on the 'play' button
                elif mouseX >= 480 and mouseX <= 540 and mouseY >= 440 and mouseY <= 460:
                    menu = False
                    aboutMenu = False
    elif aboutMenu == True: # if the user is in the about menu screen
        if textY < 50:
            textY += 2
        t = "Defensive measures against aliens brought to you by:"
        tw = textWidth(t)
        text(t, width/2 - tw/2, textY)
        t = "Swarup and Nana"
        tw = textWidth(t)
        fill(0, 45, 200)
        text(t, width/2 - tw/2, textY + 45)
        fill(255)
        t = "We wish you and your planet good luck."
        tw = textWidth(t)
        text(t, width/2 - tw/2, height - textY*2)
        t = "<Back                     Play>"
        tw = textWidth(t)
        fill(0, 255, 30)
        text(t, width/2 - tw/2, height - textY - 10)
        if mousePressed and mouseButton == LEFT:
            # is user pressing the 'back' button
            if mouseX >= 255 and mouseX <= 325 and mouseY >= 425 and mouseY <= 440:
                aboutMenu = False
                menu = True
                textY = 0
            # if the player is pressing the play button
            elif mouseX >= 475 and mouseX <= 540 and mouseY >= 420 and mouseY <= 440:
                aboutMenu = False
                menu = False
    else:
        if lost == False: # if the user is not lost
            stroke(220, 22, 22)
            line(0, paddleY + 1, width, paddleY + 1) # draw the line where the aliens win
            noStroke()
            rect(paddleX, paddleY, paddleWidth, paddleHeight) # draw the player
            triangle(paddleX, paddleY, paddleX + paddleWidth/2, paddleY - 10, paddleX+paddleWidth, paddleY) # draw the player
            
            # go through all the enemies
            for y in range( len(enemies) ):
                for x in range( len(enemies[y]) ):
                    if enemies[y][x] == 1: # if the enemy is alive
                        xPos = (x*enemySize+ex) + (x*enemySpace)
                        yPos = (y*enemySize +ey) + (y*enemySpace)
                        # draw the enemy
                        fill(255, 0, 0)
                        rect(xPos, yPos, enemySize, enemySize)
            
            ex += enemySpeedX #move the enemies by their speed
            checkEnemies()
            
            # if the player is shooting
            if playerShooting == True:
                # draw the bullet until it reaches the top of the window
                fill(200, 33, 155)
                ellipse(bulletX, bulletY, bulletSize, bulletSize)
                bulletY -= bulletSpeed
                if bulletY <= 0:
                    playerShooting = False
        # see if the player hit all 32 aliens    
        if hits == 32:
            textSize(30)
            fill(0, 255, 33)
            t = "Hurray! You saved your planet from the aliens!"
            text(t, width/2 - textWidth(t)/2, height/2)
            t = "Your people crown you as a valiant hero."
            text(t, width/2 - textWidth(t)/2, height/2 + 45)
            t = "(Not a bad thing to have in your resume.)"
            textSize(20)
            text(t, width/2 - textWidth(t)/2, height/2 + 80)
        #display lost text
        if lost == True:
            textSize(30)
            fill(240, 230, 0)
            tW = textWidth("The aliens were able to invade successfully.")
            text("The aliens were able to invade and take over.", width/2 - tW/2, height/2)
            textSize(25)
            fill(0, 255, 20)
            t = "Win Back Your Planet                Main Menu"
            text(t, width/2 - textWidth(t)/2, height - 30)
            if mousePressed and mouseButton == LEFT:
                if mouseX >= 145 and mouseX <= 395 and mouseY >= 450 and mouseY <= 470:
                    reset()
                    menu = False
                elif mouseX >= 525 and mouseX <= 655 and mouseY >= 450 and mouseY <= 470:
                    reset()
                    menu = True
                    textY = 0
    #reset the fill color
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