def randomCircle(x, y):
    radius = random(1, 100)
    fill(random(0, 255), random(0, 255), random(0, 255))
    ellipse(x, y, radius, radius)

def randomSquare(x, y):
    s = random(1, 100)
    fill(random(0, 255), random(0, 255), random(0, 255))
    rect(x, y, s, s)

def createCheckerBackground():
    for y in range(height/10):
        for x in range(width/10):
            fill(random(0, 255), random(0, 255), random(0, 255))
            rect(x * 10, y * 10, 10, 10)

def setup():
    size(800, 600)
    createCheckerBackground()

def draw():
    r = random(0, 100)
    if r < 60:
        randomCircle(mouseX, mouseY)
    else:
        randomSquare(mouseX, mouseY)