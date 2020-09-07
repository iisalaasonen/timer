from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tabs.canvas import Custom_Canvas

class Timer():
    def __init__(self, master):
        self.master = master
        self.master.title("TIMER")
        self.canvas = Custom_Canvas(self.master, bg="#313332", height=200, width=400)
        self.time_variable = StringVar()
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.time_variable.set(f"0{self.hours}:0{self.minutes}:0{self.seconds}")
        self.my_font = Font(family = "Times New Roman", size=48)
        self.my_text_font = Font(family = "Helvetica", size=24)
        self.timer_frame = Frame(self.master, bg="#313332", padx=50)
        self.timer_frame.pack(pady=10, padx=20)
        self.hours_frame = Frame(self.master, bg="#313332")
        self.hours_frame.pack(pady=5)
        self.minutes_frame = Frame(self.master, bg="#313332")
        self.minutes_frame.pack(pady=5)
        self.seconds_frame = Frame(self.master, bg="#313332")
        self.seconds_frame.pack(pady=5)
        self.button = Button(self.timer_frame, text="ALOITA", command = self.start_Time)
        self.button.pack(pady=10)
        self.label = Label(self.timer_frame, fg="#a11634", bg="#313332", font=self.my_font, textvariable=self.time_variable, width=10, height=2)
        self.label.pack()
        self.down_image = PhotoImage(file = "./images/down.png")
        self.up_image = PhotoImage(file = "./images/up.png")
        self.hour_button_up = Button(self.hours_frame, image=self.up_image, padx=5, command=lambda: self.edit_time_before("hour_up")).pack(side=LEFT, ipadx=5, padx=10)
        self.hour_text = Label(self.hours_frame, text="HOURS", fg="#a11634", bg="#313332", font=self.my_text_font).pack(side=LEFT,padx=5)
        self.hour_button_down = Button(self.hours_frame, image=self.down_image, padx=5, command=lambda: self.edit_time_before("hour_down")).pack(side=LEFT, ipadx=5, padx=10)  
        self.minute_button_up = Button(self.minutes_frame, image=self.up_image, padx=5, command=lambda: self.edit_time_before("minute_up")).pack(side=LEFT, ipadx=5, padx=10)
        self.minute_text = Label(self.minutes_frame, text="MINUTES", fg="#a11634", bg="#313332",font=self.my_text_font).pack(side=LEFT, padx=5)
        self.minute_button_down = Button(self.minutes_frame, image=self.down_image, padx=5, command=lambda: self.edit_time_before("minute_down")).pack(side=LEFT, ipadx=5, padx=10) 
        self.second_button_up = Button(self.seconds_frame, image=self.up_image, padx=5, command=lambda: self.edit_time_before("second_up")).pack(side=LEFT, ipadx=5, padx=10) 
        self.second_text = Label(self.seconds_frame, text="SECONDS", fg="#a11634", bg="#313332", font=self.my_text_font).pack(side=LEFT, padx=5)  
        self.second_button_down = Button(self.seconds_frame, image=self.down_image, padx=5, command=lambda: self.edit_time_before("second_down")).pack(side=LEFT, ipadx=5, padx=10) 

    def start_Time(self):  
        timer_time =  self.hours*3600 + self.minutes*60 + self.seconds
        self.canvas.stop_timer = False
        if timer_time > 0:
            self.canvas.move_pointer(225, 5)
            self.master.after(1000, self.edit_time_after, timer_time)

    def edit_time_after(self, time_in_seconds):
        if time_in_seconds > 0:
            time_in_seconds -= 1
            self.convert_time(time_in_seconds)
            self.master.after(1000, self.edit_time_after, time_in_seconds)
        else: 
            self.canvas.stop_timer = True
            messagebox.showinfo(message="TIME IS UP!")

    def convert_time(self, seconds):

        self.hours = int(seconds/3600)
        remain_seconds = seconds - self.hours*3600
        self.minutes = int(remain_seconds/60)
        self.seconds = remain_seconds - self.minutes*60
        self.edit_time_variable()

    def edit_time_before(self, time):

        h="00"
        m="00"
        s="00"

        if time=="hour_up":
            self.hours += 1
        if time=="hour_down" and self.hours > 0:
            self.hours -= 1
        if time=="minute_up" and self.minutes < 60:
            self.minutes += 1
        if time=="minute_down" and self.minutes > 0:
            self.minutes -= 1
        if time=="second_up" and self.seconds < 60:
            self.seconds += 1
        if time=="second_down" and self.seconds > 0:
            self.seconds -= 1
        self.edit_time_variable()

    def edit_time_variable(self):
        if self.hours < 10:
            h=(f"0{self.hours}")
        else: h=self.hours
        if self.minutes < 10:
            m=(f"0{self.minutes}")
        else: m=self.minutes
        if self.seconds < 10:
            s=(f"0{self.seconds}")
        else: s=self.seconds

        self.time_variable.set(f"{h}:{m}:{s}")    

