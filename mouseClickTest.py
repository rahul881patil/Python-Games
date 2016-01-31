# global variables
import simplegui
import math

x, y = 500, 500
ball_color = "Blue" 
ball_position =  [x/2, y/2]
ball_radius = 30

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) **2 + (p[1] - q[1]) **2)

# even handlers
def draw(canvas):
    global ball_color, ball_position, ball_radius
    canvas.draw_circle(ball_position, ball_radius ,1, "Red", ball_color)

def click(position):
    global ball_color, ball_position
    
    if( distance(ball_position, position) < ball_radius):
        ball_position = position
        ball_color = "Green"
    else:
        ball_position = position
        ball_color = "Blue" 
    

# registration
frame = simplegui.create_frame("mouseIP", x, y)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.start()

