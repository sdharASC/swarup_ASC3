from ball import Ball

ball_list = []

def setup():
    global ball_list
    size(1200, 700)
    noStroke()
    rad = 100
    for i in range(10):
        ball_list.append(Ball((i * rad) + 150, rad*2, rad))
    
def draw():
    global ball_list
    # reset the background
    background(200)
    for i in ball_list:
        i.collision(ball_list)
        i.update(width, height)
        i.render()
    