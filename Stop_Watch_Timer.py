# global variables
import simplegui

time = 0
start = False
stop = False
x = 0
y = 0

# helper functions
def format():
    global time
    d = time %10
    c = time %100
    c = (c - d)/10
    b = time %1000
    b = (b - (c + d))/100
    a = (time - (b*100 + c*10 + d ))/1000
    t_time = int(str(a)+str(b)+str(c))
    minute = t_time % 60
    if(minute <= 9):
        b, c = 0, minute
    else:
        c, b = minute % 10, (minute - c)/10     
    a = t_time / 60
    return str(a) + " : " + str(b)+str(c) + " : " + str(d) 

def check(txt):
    global x, stop
    c_time = int(txt)
    if(c_time % 10 == 0):
        digi, rem, div = 0, 1, 10
        while(rem != c_time):
            rem = c_time % div
            digi += 1
            div *= 10   
        if((c_time % (10**(digi-2)) == 0) and stop != True):
            x += 1
        
# handler
def draw(canvas):
    global x, y
    message = str(x) +" / "+ str(y)
    canvas.draw_text(message, (50,50), 40, "Red")
    canvas.draw_text(format(), (120,150), 40, "Red")

def timer():
    global time
    if(start == True):
        time += 1

def start():
    global start, stop
    start, stop = True, False
    
def stop():
    global stop, start, time, y
    check(time)  
    if(stop != True):
        y += 1  
    stop, start, time = True, False, 0
    
def reset():
    global x, y, start, stop, time 
    x, y, start, stop, time = 0, 0, False, False, 0
    
# frames
frame = simplegui.create_frame("gui", 300, 300)
start = frame.add_button("Start",start, 100)
stop = frame.add_button("Stop",stop, 100)
stop = frame.add_button("Reset",reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer)

# register 
frame.start()
timer.start()