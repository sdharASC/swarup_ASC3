class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.col = color(200, random(100), random(100))
        self.size = 50
    
    def render(self):
        fill(self.col)
        rect(self.x, self.y, self.size, self.size)