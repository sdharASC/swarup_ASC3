#Made my Swarup and Julian

#Variables
GRID_SIZE = 10
SQUARE_SIZE = 0
BOARD = []
SHIPS = 3 #number of ships
LIFE = 25
WIN = False #if user won
LOST = False #if user lost

def start_setup():
    #reset function, R is reset
    global GRID_SIZE, SQUARE_SIZE, BOARD, SHIPS, LIFE, LOST, WIN
    SHIPS = 5
    LIFE = 20
    LOST = False
    WIN = False
    
    BOARD = [] #empty the board
    
    for i in range(GRID_SIZE):
        BOARD.append(['0'] * GRID_SIZE)

    for i in range(SHIPS):
        r = int(random(0, GRID_SIZE))
        c = int(random(0, GRID_SIZE))
        if BOARD[r][c] != 'x':
            r = int(random(0, GRID_SIZE))
            c = int(random(0, GRID_SIZE))
            if BOARD[r][c] != 'x':
                r = int(random(0, GRID_SIZE))
                c = int(random(0, GRID_SIZE))
        BOARD[r][c] = 'x'
    fill(0, 0, 255)

def getSquare(x, y):
    global BOARD, SQUARE_SIZE
    return BOARD[int(y/SQUARE_SIZE)][int(x/SQUARE_SIZE)]

# This will go through the BOARD and draw all the squares
def drawBoard():
    global BOARD, SQUARE_SIZE
    for i in range(len(BOARD)):
        #set different colors for different types of squares
        # 'x' is a ship
        # '!' is an empty square that was clicked by the user
        # 'k' is a square with a ship that was clicked by the user
        for j in range(len(BOARD[i])):
            stroke(255, 0, 0)
            #hack, remove comment to turn on
            '''if BOARD[i][j] == 'x':
                fill(0, 200, 0)
            el'''
            if BOARD[i][j] == 'k':
                fill(255,0,255)
            elif BOARD[i][j] == '!':
                fill(0, 255, 255)
            else:
                fill(0, 0, 255)
            rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)


def setup():
    global SQUARE_SIZE, GRID_SIZE, BOARD
    size(700, 700)
    SQUARE_SIZE = width / GRID_SIZE
    for i in range(GRID_SIZE):
        BOARD.append(['0'] * GRID_SIZE)

    for i in range(SHIPS):
        BOARD[int(random(0, GRID_SIZE))][int(random(0, GRID_SIZE))] = 'x'
    fill(0, 0, 255)
 
def draw():
    global SQUARE_SIZE, BOARD, SHIPS, LIFE
    if LIFE > 0 and SHIPS > 0:
        drawBoard()
        fill(245, 245, 22)
        textSize(15)
        text("Lives remaining:"+str(LIFE),10, 15 )

def mousePressed():
    global SQUARE_SIZE, BOARD, SHIPS, LIFE, WIN, LOST
    
    if WIN == False and LOST == False:
        if getSquare(mouseX, mouseY) != 'k' and getSquare(mouseX, mouseY) != '!':
            if mouseButton == LEFT and getSquare(mouseX, mouseY) == 'x':
                print("KABOOM")
                x = int(mouseX / SQUARE_SIZE)
                y = int(mouseY / SQUARE_SIZE)
                BOARD[y][x] = 'k'
                SHIPS = SHIPS - 1
                drawBoard()
            elif mouseButton == LEFT and getSquare(mouseX, mouseY) != 'x':
                LIFE -= 1
                print("You just lost a life!", LIFE)
                x = int(mouseX / SQUARE_SIZE)
                y = int(mouseY / SQUARE_SIZE)
                BOARD[y][x] = '!' #changes the value to !, which represents a miss
                drawBoard()
    
    if SHIPS == 0:
        print("You win!")
        WIN = True
        textSize(50)
        w = textWidth("You Win, you lucky dog!")
        fill(255)
        text("You Win, you lucky dog!", width/2 - w/2, height/2)
    if LIFE == 0:
        # show all the places where there was a ship
        for i in range(len(BOARD)):
            for j in range(len(BOARD[i])):
                stroke(255, 0, 0)
                if BOARD[i][j] == 'x':
                    fill(0, 200, 0)
                    rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        print("BOOO! You lost!")
        LOST = True
        textSize(50)
        w = textWidth('BOOO! You lost!')
        fill(255)
        text('BOOO! You lost!', width/2 - w/2, height/2)
        w = textWidth('Better luck next time!')
        text('Better luck next time!', width/2 - w/2, height/2 + 50)
        textSize(30)
        text("Press r to restart.", width/2 - textWidth("Press r to restart.")/2, height - 60)
#RESET
def keyPressed():
    if keyCode == 82: 
            start_setup()
#RESET