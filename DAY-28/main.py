from tkinter import *
reps = 0

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
tick_mark = "✓"
checkmarks = ""
timer_clock = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global  checkmarks
    global  reps
    window.after_cancel(timer_clock)
    canvas.itemconfig(timer, text='00:00')
    timer_text.config(text="Timer",fg=GREEN)
    checkmarks = ""
    tick.config(text=checkmarks)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global tick_mark
    global checkmarks

    reps += 1
    work_sec = 25*60
    short_break = 5*60
    long_break = 20*60

    start = [1,3,5,7]
    breaks = [2,4,6]
    checks = [3,5,7]


    if reps in checks:
        checkmarks += tick_mark
        tick.config(text=checkmarks)

    if reps in start:
        timer_text.config(text="Work",fg=GREEN)
        count_down(work_sec)
    elif reps in breaks:
        timer_text.config(text="Break", fg=PINK)
        count_down(short_break)
    elif reps == 8:
        timer_text.config(text="Break", fg=RED)
        count_down(long_break)
    else:
        reps = 0
        timer_text.config(text="Timer", fg=GREEN)
        return


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minute = int(count/60)
    second = count%60

    if minute < 10:
        minute = f"0{minute}"

    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer ,text=f"{minute}:{second}")
    if count > 0:
        global  timer_clock
        timer_clock = window.after(1000,count_down, count-1)

    if minute == "00" and second == "00":
        print("hi")
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PROMODORO")
window.config(padx=100,pady=50, bg=YELLOW)



canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomate_img)
timer = canvas.create_text(100,140,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)


timer_text = Label()
timer_text.config(bg=YELLOW,fg=GREEN)
timer_text.config(text="Timer", font=(FONT_NAME,20,'bold'))
timer_text.grid(row=0,column=1)

start_btn = Button()
start_btn.config(text="Start",highlightthickness=0,command=start_timer)
start_btn.grid(row=2,column=0)

reset_btn = Button()
reset_btn.config(text="Reset",highlightthickness=0,command=reset_timer)
reset_btn.grid(row=2,column=2)

tick_mark = "✓"

tick = Label()
tick.config(text=" ",fg=GREEN,font=(FONT_NAME, 20 , 'bold'),bg=YELLOW)
tick.grid(row=3,column=1)

window.mainloop()