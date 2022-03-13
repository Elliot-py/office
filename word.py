import keyboard as key
import time

key.press('win')
key.press('r')
key.release('win')
key.release('r')
time.sleep(1)
key.write("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
key.send("enter")

import tkinter
from tkinter import messagebox

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

time.sleep(10)
messagebox.showinfo("Glasses", "Одень очки!!")