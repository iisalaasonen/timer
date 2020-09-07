from tkinter import *
import math
import random

class Custom_Canvas(Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.pack(pady=10)
        self.update()
        self.drawTree(self.winfo_width()/4, self.winfo_height(), 270, "#4d2522", self.winfo_height()/8, 2, 7)
        self.drawTree(self.winfo_width()*0.75, self.winfo_height(), 270, "#4d2522", self.winfo_height()/8, 2, 7)
        self.oval_size=20
        self.create_oval(self.winfo_width()/2-self.oval_size, self.winfo_height()-self.oval_size, self.winfo_width()/2+self.oval_size, self.winfo_height()+self.oval_size, fill="white")
        self.line = {"x":self.winfo_width()/2, "y":self.winfo_height(), "angle":270, "color":"white", "length":150, "linewidth":5.5}
        endx, endy = self.new_xy(self.line["x"], self.line["y"], self.line["angle"], self.line["length"] )
        self.line_id = self.create_line(self.line["x"],self.line["y"], endx, endy, fill=self.line["color"], width=self.line["linewidth"], smooth=True, capstyle="round")
        self.stop_timer = False

    def new_xy(self, x, y, angle, length):
        newX = int(x + math.cos(angle*math.pi/180)*length)
        newY = int(y + math.sin(angle*math.pi/180)*length)
        return newX, newY
        
    def move_pointer(self, angle, direction):
        a = angle
        d = direction
        if a == 225:
            d = 5
        if a == 315:
            d = -5
        a = a + direction
        newX = int(self.line["x"] + math.cos(a*math.pi/180)*self.line["length"])
        newY = int(self.line["y"] + math.sin(a*math.pi/180)*self.line["length"])
        self.coords(self.line_id, self.line["x"],self.line["y"], newX, newY)
        if self.stop_timer == False:
            self.after(55, self.move_pointer, a, d)
    
    def drawTree(self, x, y, angle, color, length, width, index):
        x2, y2 = self.new_xy(x,y, angle, length)
        self.create_line(x, y, x2, y2, fill=color, width=width)
        index -= 1
        if index == 0:
            return 
        else: 
            self.drawTree(x2, y2, angle-random.randint(10, 30), color, random.randint(10, 40), width, index)
            self.drawTree(x2, y2, angle+random.randint(10, 30), color, random.randint(10, 40), width, index)


    

        



    