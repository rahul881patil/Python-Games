# global variables
import simplegui
import math

x, y = 500, 500
ball_list = []
ball_radius = 15

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) **2 + (p[1] - q[1]) **2)

# even handlers
def draw(canvas):
    global ball_list, ball_radius
    for ball in ball_list:
        canvas.draw_circle((ball[0], ball[1]),  ball_radius ,1, "Red", ball[2])

def click(pos):
    global ball_list
    add = True
    
    for ball in ball_list:   
        if distance((ball[0], ball[1]), pos) < ball_radius:            
            ball_list.pop(ball_list.index(ball))
            add = False
            
    if add:
        ball_list.append([pos[0], pos[1], "Red"])

# registration
frame = simplegui.create_frame("mouseIP", x, y)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.start()

