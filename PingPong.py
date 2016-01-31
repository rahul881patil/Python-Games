# ping pong game 
import simplegui
import random

can = [900, 600]
ball = [can[0]//2, can[1]//2]
ball_vel = []
ball_radius = 20
score_1, score_2 = 0, 0
pad_d = [100, 20] # [height, width]
pad_1 = [[0,can[1]//2 - pad_d[0]//2], [pad_d[1], can[1]//2 - pad_d[0]//2], 
         [pad_d[1], can[1]//2 + pad_d[0]//2], [0,can[1]//2 + pad_d[0]//2]]
pad_2 = [[can[0] - pad_d[1], can[1]//2 - pad_d[0]//2], [can[0], can[1]//2 - pad_d[0]//2], 
         [can[0], can[1]//2 + pad_d[0]//2], [can[0] - pad_d[1], can[1]//2 + pad_d[0]//2]]

# helper 
def on_paddle(ball, direction):
    global pad_1, score_1, score_2 
    if direction == "RIGHT":
        if (ball[1] >= pad_1[0][1] and ball[1] <= pad_1[2][1]):
            pass
        else:
            score_2 += 1        
    elif direction == "LEFT":
        if (ball[1] >= pad_2[0][1] and ball[1] <= pad_1[2][1]):
            pass
        else:
            score_1 += 1 

# handler
def draw(canvas):
    global score_1
    canvas.draw_line((20, 0), (20, can[1]), 2, "White")
    canvas.draw_line((0+pad_d[1], can[1]//2), (can[0]-pad_d[1], can[1]//2), 1, "White")
    canvas.draw_line((can[0]-20, 0), (can[0]-20, can[1]), 2, "White")
    canvas.draw_line((can[0]//2, 0), (can[0]//2, can[1]), 1, "White")
    canvas.draw_circle(ball, ball_radius, 1, "Red", "Red")
    canvas.draw_circle((can[0]//2, can[1]//2), 50, 1, "White")
    
    canvas.draw_polygon(pad_1, 2, "Red")
    canvas.draw_polygon(pad_2, 2, "Red")
    
    canvas.draw_text(str(score_1), (((can[0]//2)//2), 40), 30, "RED")
    canvas.draw_text(str(score_2), (670, 40), 30, "RED")
    
    if (ball[1] <= ball_radius):
        if ball_vel[1] < 0: 
            ball_vel[1] = -ball_vel[1]  
        else: 
            ball_vel[1] = +ball_vel[1]   
    if (ball[1] >= can[1]-ball_radius):
        if ball_vel[1] > 0: 
            ball_vel[1] = -ball_vel[1]  
        else: 
            ball_vel[1] = +ball_vel[1] 
    if (ball[0] <= ball_radius + pad_d[1]):
        on_paddle(ball, "RIGHT")
        if ball_vel[0] < 0: 
            ball_vel[0] = -ball_vel[0]  
        else: 
            ball_vel[0] = +ball_vel[0]
    elif (ball[0] >= can[0] - pad_d[1] - ball_radius):
        on_paddle(ball, "LEFT")
        if ball_vel[0] > 0: 
            ball_vel[0] = -ball_vel[0]  
        else: 
            ball_vel[0] = +ball_vel[0]

    ball[0] += ball_vel[0]/40    
    ball[1] += ball_vel[1]/40 
    
def spawn_ball(direction):  
    global ball, ball_vel 
    ball = [can[0]//2, can[1]//2]  
    ball_vel = [random.randrange(120, 240), random.randrange(60, 180)]  
    if (direction == 'RIGHT'):  
        ball_vel[1] = -ball_vel[1]  
    if (direction == 'LEFT'):  
        ball_vel[0] = -ball_vel[0]  
        ball_vel[1] = -ball_vel[1] 
    
def keydown(key):
    global pad_1, pad_2
    vel = 40
    if key == simplegui.KEY_MAP['up'] and pad_1[0][1] - vel > 0:
        pad_1[0][1] -= vel 
        pad_1[1][1] -= vel
        pad_1[2][1] -= vel
        pad_1[3][1] -= vel
    elif key == simplegui.KEY_MAP['down'] and pad_1[2][1] + vel < can[1]:
        pad_1[0][1] += vel 
        pad_1[1][1] += vel
        pad_1[2][1] += vel
        pad_1[3][1] += vel       
    elif key == simplegui.KEY_MAP['s'] and pad_2[2][1] + vel < can[1]:
        pad_2[0][1] += vel 
        pad_2[1][1] += vel
        pad_2[2][1] += vel
        pad_2[3][1] += vel    
    elif key == simplegui.KEY_MAP['w'] and pad_2[0][1] - vel > 0:
        pad_2[0][1] -= vel 
        pad_2[1][1] -= vel
        pad_2[2][1] -= vel
        pad_2[3][1] -= vel
        
# register
frame =  simplegui.create_frame("PingPong", can[0], can[1]) 
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start
frame.start()
spawn_ball('LEFT')
    
    
    