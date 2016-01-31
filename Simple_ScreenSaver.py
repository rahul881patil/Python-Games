# global variables
import simplegui
import random

x = 150
y = 150
change = False
message = "Hello!"

# helper functions
def changeCartetian():
    global change, x, y
    if(change == True): 
        x = random.randrange(10, 400)
        y = random.randrange(10, 400)

# handlers
def draw(canvas):
    global x, y, change, message
    print x, y, change
    canvas.draw_text(message, (x, y), 30, "Red")
    
def toggle():
    global change
    if (change == False):
        change = True
    else: 
        change = False

def update_message(txt):
    global message
    message = txt
    
# create frame
frame = simplegui.create_frame("screensaver", 500, 500)
toggle = frame.add_button("Toggle", toggle, 100)
input_txt = frame.add_input("message",update_message, 200)
timer = simplegui.create_timer(1000, changeCartetian)
frame.set_draw_handler(draw)

# register
frame.start()
timer.start()