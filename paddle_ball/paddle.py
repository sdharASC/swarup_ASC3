class Paddle:
    def __init__(self, _width, _height):
        self.width = _width
        self.height = _height
        self.x = 0
        self.y = 0
        self.velX = 5
        self.col = color(random(255), random(255), random(255))
    
    def update(self, x, y):
        self.x = x
        self.y = y
    
    def render(self):
        fill(self.col)
        rect(self.x, self.y, self.width, self.height)