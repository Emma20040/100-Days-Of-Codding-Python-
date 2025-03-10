from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
count_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(count_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check_marks.config(text=" ")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN*60

    
    
    if reps % 8 ==0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN) 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min= math.floor(count/60)
    count_sec = count % 60
    if count_sec <10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        global count_timer
        count_timer=window.after(1000, count_down, count- 1)
    else:
        start_timer()
        marks= ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks +="check"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW )

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
t_image= PhotoImage(file="Day 28/tomato.png")
canvas.create_image(100, 112, image=t_image )
timer_text= canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


start = Button(text="start", highlightthickness=0, command= start_timer)
start.grid(column=0, row=2)

Reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
Reset.grid(column=3, row=2)

timer= Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer.grid(column=1, row=0)

check_marks = Label( fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()  