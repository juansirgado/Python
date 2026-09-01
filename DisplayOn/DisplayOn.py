#===========================================================
# Program: DisplayOn
# Date: 2023/09/28
#===========================================================
# Create by: Juan Sirgado y Antico
# Copyright: JSyA Innovation Inc
#===========================================================
# Commands to create the file DisplayOn.exe
# set path=%path%;C:\Users\Juan\AppData\Local\Packages\ & 
# PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\ & 
# LocalCache\local-packages\Python311\Scripts
# pyinstaller --console --noconfirm --onefile DisplayOn.py
#===========================================================
import tkinter as tk
import ctypes as ct 
import sys as so
#===========================================================
window = tk.Tk()
#===========================================================
class DisplayOn:
    message = ""
#===========================================================
def display_on():
    ct.windll.kernel32.SetThreadExecutionState(0x80000002)
    window.title("Display - ON")
#===========================================================
def display_off():
    ct.windll.kernel32.SetThreadExecutionState(0x80000000)
    window.title("Display - OFF")
#===========================================================
def display_quit():
    ct.windll.kernel32.SetThreadExecutionState(0x80000000)
    so.exit(0)
#===========================================================
window.geometry("260x40")
window.title("Display - App")
frame = tk.Frame(window)
frame.pack()
#===========================================================
slogan = tk.Button(frame, text="    ON    ", command=display_on)
slogan.pack(side=tk.LEFT)
slogan = tk.Button(frame, text="    OFF    ", command=display_off)
slogan.pack(side=tk.LEFT)
button = tk.Button(frame, text="    Quit    ", command=display_quit)
button.pack(side=tk.LEFT)
#===========================================================
window.mainloop()
so.exit(0)
#===========================================================
# That is all folks! 
#===========================================================