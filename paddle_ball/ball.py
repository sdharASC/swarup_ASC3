def randColor():
    return color(random(0, 255), random(0, 255), random(0, 255))

class Ball:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velX = 3
        self.velY = -3
        self.diam = 30
        self.rad = self.diam/2
        self.col = randColor()
        self.gameOver = False
        self.score = 0
        self.rate = 1.05
        self.bounceScore = 1
        self.brickScore = 5
    
    def render(self):
        fill(self.col)
        ellipse(self.x, self.y, self.diam, self.diam)
    
    def update(self, w, h):
        self.x += self.velX
        self.y += self.velY
        
        ''' Check if the ball hits the wall '''
        if self.x + self.rad >= w or self.x - self.rad <= 0:
            self.velX *= -self.rate
        if self.y + self.rad >= h:
            self.gameOver = True
        if self.y - self.rad <= 0:
            self.velY *= -self.rate
        
    def checkCollision(self, paddle):
        global wallScore
        if self.x+self.rad >= paddle.x and self.x-self.rad <= paddle.x + paddle.width:
            if self.y + self.rad >= paddle.y - 1:
                self.velY *= -1
                self.score += self.bounceScore
    
    def checkBrick(self, brick_list):
        global brickScore
        for b in brick_list:
            if (dist(self.x, self.y, b.x + b.size/2, b.y+b.size/2) <= self.rad+b.size/2):
                brick_list.remove(b)
                self.score += self.brickScore
                self.velX *= -1
                self.velY *= -1