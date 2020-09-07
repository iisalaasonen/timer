from tkinter import *
from tabs.timer import Timer

root = Tk()
root.title("TIMER")
root.configure(background="#4d2522")
timer = Timer(root)
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()



   