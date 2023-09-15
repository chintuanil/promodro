from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_restart():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="TIMER",fg="GREEN")
    check_mark.config(text="")
    global reps
    reps=0




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_set():
    global reps
    reps+=1
    if reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        timer_label.config(text="LONG BREAK",fg="GREEN")

    elif reps%2==0:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text="SHORT BREAK",fg="RED")
    else:
        count_down(WORK_MIN*60)
        timer_label.config(text="work",fg="GREEN")


    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=count//60
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        timer_set()
        marks=""
        work_no=reps//2
        for i in range(work_no):
            marks+="✓"
        check_mark.config(text=marks)
       
    

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("pomodromo project")
window.config(padx=20,pady=20,bg="blue")
window.minsize(width=100,height=100)


timer_label=Label(text="Timer",font=(FONT_NAME,30,"bold") ,bg="blue",fg="white",highlightthickness=0)
timer_label.grid(column=1,row=0 )

canvas=Canvas(width=210,height=234, bg="blue",highlightthickness=0)
photo=PhotoImage(file="C:/Users/balla/Downloads/pomodoro-start (2) - Copy/pomodoro-start/tomato.png")
canvas.create_image(103 , 119, image=photo)
timer_text=canvas.create_text(100,130,text="00:00" ,fill="white",font=(FONT_NAME ,30, "bold"))
canvas.grid(column=1,row=1)


start_button=Button(text="start",font=(FONT_NAME,10,"bold"),highlightthickness=0,bg="pink",command=timer_set)
start_button.grid(column=0,row=4)

check_mark=Label(text="",font=(FONT_NAME,20,"bold"),highlightthickness=0,bg="blue",fg=GREEN)
check_mark.grid(column=1,row=3)

restart_button=Button(text="Restart",font=(FONT_NAME,10,"bold"),highlightthickness=0,bg="pink",command=timer_restart)
restart_button.grid(column=2,row=4)






window.mainloop()