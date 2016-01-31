# global variables
import simplegui
import random
canvas_d = [800 , 100]
display = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
array = []
state, x, y, val_1, val_2  = 0, 50, 25, -1, -1
val_idx_1, val_idx_2 = -1, -1

# helper functions

# handlers
def draw(canvas):
    global array
    i = 1
    if(display[0] != 0):
        canvas.draw_text(str(array[i-1]), ((x*i-25) , canvas_d[1]/2), 20, "White")
    while(i != 16):
        canvas.draw_line((x*i,0), (x*i,canvas_d[1]), 2, "Red")
        if(display[i] != 0):
            canvas.draw_text(str(array[i]), ((x*i+25) , canvas_d[1]/2), 20, "White")
        i += 1

def reset():
    new_game()
                
def new_game():
    global state, x, y, val_1, val_2, val_idx_1, val_idx_2
    array, a1, i = [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], 0   
    while(i != 16):
        display[i] = 0
        i += 1
    i = 0        
    while(i != 8):
        num = random.randint(0, 7)
        array[i] = num
        a1[i] = num
        i += 1
    random.shuffle(a1)
    array.extend(a1)
    state, val_1, val_2  = 0, -1, -1
    val_idx_1, val_idx_2 = -1, -1
    print array
    return array
    
        
def click(position):
    global x, display, state, array, val_1, val_2, val_idx_1, val_idx_2
    
    if(state == 2):
        state = 0
        if(val_1 != val_2):
            display[val_idx_1],  display[val_idx_2] = 0, 0
            val_1, val_2, val_idx_1, val_2 = -1, -1, -1, -1
        
    found, i, y = False, 0, x  
    while(found != True):
        if( i*y <=  position[0] and (i+1)*y >= position[0]):
            found = True
            display[i] = 1
            if(state == 0):
                val_1, val_idx_1 = array[i], i
            elif(state == 1):
                val_2, val_idx_2 = array[i], i                
            state += 1
            break
        else:
            i += 1   

# frame registration 
frame = simplegui.create_frame("C1", canvas_d[0], canvas_d[1])
frame.set_draw_handler(draw)
frame.set_canvas_background("Green")
frame.add_button("Reset", reset)
frame.set_mouseclick_handler(click)

# start frame
array = new_game()
frame.start()


