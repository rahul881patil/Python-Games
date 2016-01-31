# program for simple gui calculator
import simplegui

# global variables
op_1 = 0
op_2 = 0
op_3 = 0

# helper function
def add():
    global op_1, op_2, op_3
    op_3 = op_1 + op_2
    print op_1, " + ", op_2, " = ", op_3, "\n" 
    op_3 = 0

def prin():
     global op_1, op_2, op_3
     print "op_1 = ", op_1
     print "op_2 = ", op_2  
     print "op_3 = ", op_3  
    

# event handler
def add_button():
    add()

def print_button():
    prin()
 
def enter_op1(val):
    global op_1
    op_1 = float(val)
    
def enter_op2(val):
    global op_2
    op_2 = float(val)
    
# frame
frame = simplegui.create_frame("calculator", 200, 200)
frame.add_input("op1", enter_op1, 100)
frame.add_input("op2", enter_op2, 100)
frame.add_button("Addition", add_button, 200)
frame.add_button("Print", print_button, 200)

# start
frame.start()


