from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")


def time():
    time_format = strftime("%I:%M:%S %p")
    label.config(text=time_format)  # pass time format to the label
    label.after(1000, time)  # run the function every one second


label = Label(root, font="ds-digital 100", background="dark blue", foreground="green")
label.pack(anchor="center")

time()

mainloop()

