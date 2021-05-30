from tkinter import *
import math

 
import os
clear = lambda: os.system('cls')
clear()
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
sessions=''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps,sessions
    reps = 0
    sessions=''
    window.after_cancel(timer)
    timer_label.config(text='Timer',fg=GREEN,bg=YELLOW)
    canvas.itemconfig(timer_text,text="00:00")
    check_mark.config(text=sessions)


 
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    work_sec = WORK_MIN*60-1
    short_break_sec = SHORT_BREAK_MIN*60-1
    long_break_sec =LONG_BREAK_MIN*60-1
    reps+=1
    
    if reps%8==0:
        cut_count(long_break_sec)
        timer_label.config(text="Long Break",fg=RED)
    elif reps%2==0:
        cut_count(short_break_sec)
        timer_label.config(text="Short Break",fg=PINK)
    else:
        timer_label.config(text="Work",fg=GREEN)
        cut_count(work_sec)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def cut_count(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    canvas.itemconfig(timer_text,text=f"{count_min:02d}:{count_sec:02d}")
    if count>0:
        global timer
        timer = window.after(1000,cut_count,count-1)
    else:
        start_timer()
        if reps%2==0:
            global sessions
            sessions+='✔'
            check_mark.config(text=sessions)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')
# window.geometry('700x700')
window.config(padx=100,pady=50,bg=YELLOW)





timer_label = Label(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,'bold'))
timer_label.grid(row=0,column = 1)


# Canvas setting

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0) 
img  = PhotoImage(file='./tomato.png')
canvas.create_image(100,112,image=img)
timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)
 
# Bottom Buttons
start_button = Button(text="Start",font=('Arial',10,'bold'),bg='white',fg='black',command=start_timer)
start_button.grid(row=2,column = 0)




reset_button = Button(text='Reset',font=('Arial',10,'bold'),command=reset_timer)
reset_button.grid(row=2,column =2)

check_mark =  Label(bg  = YELLOW,fg = GREEN,font=('Arial',20,'bold'))
check_mark.grid(row=3,column = 1)

window.mainloop()
