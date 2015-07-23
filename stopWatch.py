# template for "Stopwatch: The Game"
import simplegui
# define global variables
cntr,x,y = 0,0,0
timer_has_been_stopped = None


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t // 600
    B = (t%600)//100
    C = (t%100)//10
    D = t%10
    
    return str(A)+":"+str(B)+str(C)+"."+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global timer_has_been_stopped
    timer.start()
    timer_has_been_stopped = False
    
def stop_handler():
    global y,x,timer_has_been_stopped
    timer.stop()
    if(timer_has_been_stopped == False):
        y +=1
        timer_has_been_stopped=True
    	if(cntr % 10 == 0):
        	x+=1
    
def reset_handler():
    global cntr,x,y
    timer.stop()
    cntr,x,y = 0,0,0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global cntr
    cntr += 1
    #print cntr

# define draw handler
def draw_handler(canvas):
    global x,y
    canvas.draw_text(format(cntr),[50,100],40,"Red")
    canvas.draw_text(str(x)+"/"+str(y),[130,25],25,"Green")
    
# create frame
frame = simplegui.create_frame("Stop watch",180,180)

# register event handlers
timer =  simplegui.create_timer(100,timer_handler)
startbutton = frame.add_button("Start",start_handler,150)
stopbutton = frame.add_button("Stop",stop_handler,150)
resetbutton = frame.add_button("Reset",reset_handler,150)
frame.set_draw_handler(draw_handler)

# start frame
#timer.start()
frame.start()


# Please remember to review the grading rubric
