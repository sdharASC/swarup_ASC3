def randColor():
    return color(random(0, 255), random(0, 255), random(0, 255))


class Ball:
    def __init__(self, x, y, diam):
        self.x = x
        self.y = y
        self.diam = diam
        self.rad = self.diam / 2
        self.velX = random(0, 5)
        self.velY = random(0, 5)
        if(random(0, 1) == 1):
            self.velX *= -1
        if random(0, 1) == 1:
            self.velY *= -1
        self.col = randColor()
    
    # draw the ball
    def render(self):
        fill(self.col)
        ellipse(self.x, self.y, self.diam, self.diam)
    
    #update the position and check for edge collision
    def update(self, w, h):
        self.x += self.velX
        self.y += self.velY
        if self.x + self.rad >= w or self.x - self.rad <= 0:
            self.velX *= -1
            self.col = randColor()
        if self.y + self.rad >= h or self.y - self.rad <= 0:
            self.velY *= -1
            self.col = randColor()
    
    # check for collisions between other balls
    def collision(self, balls):
        for i in balls:
            if i != self:
                distance = dist(self.x, self.y, i.x, i.y)
                if(distance <= self.rad + i.rad):
                    self.velX *= -1
                    self.velY *= -1
                    break