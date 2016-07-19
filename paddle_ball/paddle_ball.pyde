from paddle import Paddle
from ball import Ball
from bricks import Brick

ball = 0
paddle = 0
brick_list = []

def setup():
    global ball, paddle, brick_list
    size(1200, 600)
    paddle = Paddle(100, 30)
    ball = Ball(width/2, height/2)
    brick_list = []
    brick_list.append(Brick(random(100, width-100), random(100, height-300)))
    
def draw():
    global ball, paddle, brick_list
    background(51)
    noStroke()
    for b in brick_list:
        b.render()
    if ball.gameOver != True:
        ball.update(width, height)
        ball.checkCollision(paddle)
        ball.checkBrick(brick_list)
        if len(brick_list) == 0:
            for i in range(10):
                brick_list.append(Brick(random(100, width-100), random(100, height - 300)))
    else:
        textSize(50)
        fill(255, 255, 255)
        t = "Game Over! Your Score is: " + str(ball.score)
        tW = textWidth(t)
        text(t, width/2 - tW/2, height/2)
        textSize(25)
        t = "Press r to retry"
        tW = textWidth(t)
        text(t, width/2 - tW/2, height/2 + tW)
    ball.render()
    paddle.update(mouseX, height - 20)
    paddle.render()

def keyTyped():
    global ball
    if ball.gameOver:
        if key == 'r' or key == "R":
            setup()