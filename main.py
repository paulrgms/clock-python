from tkinter import Tk
from tkinter import Label

from time import strftime
import sys

master =Tk()
master.title("Digital Clock")

def time():
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

label =Label(master, font=("Calibri",80), bg="black", fg="white")
label.pack(anchor="center")

time()

master.mainloop()