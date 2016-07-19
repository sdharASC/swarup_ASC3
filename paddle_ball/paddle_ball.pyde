from paddle import Paddle
from ball import Ball
from bricks import Brick

ball = 0
paddle = 0
brick_list = []
highScore = 0
h = False

def setup():
    global ball, paddle, brick_list, h
    size(1200, 600)
    paddle = Paddle(150, 30)
    ball = Ball(width/2, height/2)
    h = False
    brick_list = []
    brick_list.append(Brick(random(100, width-100), random(100, height-300)))
    
def draw():
    global ball, paddle, brick_list, highScore, h
    background(51)
    noStroke()
    for b in brick_list:
        b.render()
    if ball.gameOver == False:
        textSize(15)
        fill(255)
        text(str(ball.score), 10, 30)
        ball.update(width, height)
        ball.checkCollision(paddle)
        ball.checkBrick(brick_list)
        if len(brick_list) == 0:
            for i in range(10):
                brick_list.append(Brick(random(100, width-100), random(100, height - 300)))
    else:
        if highScore < ball.score:
            highScore = ball.score
            h = True
        ''' Score '''
        textSize(50)
        fill(255, 255, 255)
        t = "Game Over! Your Score is: " + str(ball.score)
        tW = textWidth(t)
        text(t, width/2 - tW/2, height/2)
        ''' High Score '''
        textSize(40)
        if h:
            t = "New High Score!"
        else:
            t = "High Score: " + str(highScore)
        tW = textWidth(t)
        text(t, width/2 - tW/2, height/2 + 60)
        ''' Replay '''
        textSize(25)
        t = "Press r to play again"
        tW = textWidth(t)
        text(t, width/2 - tW/2, height - 50)
    ball.render()
    paddle.update(mouseX - paddle.width/2, height - 20)
    paddle.render()

def keyTyped():
    global ball
    if ball.gameOver:
        if key == 'r' or key == "R":
            setup()