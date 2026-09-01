import tkinter as tk

mywindow = tk.Tk()
mywindow.title("Python GUI Test")
mywindow.geometry("800x600")
mywindow.rowconfigure([0, 1, 2, 4],minsize=50, weight=5)
mywindow.columnconfigure([0, 1, 2],minsize=50, weight=5)
event = []

mylabel = tk.Label(text="", bg="blue",fg="red")
mylabel.grid(row=1, column=1, sticky="nsew")
# mylabel.pack()

myentry = tk.Entry(text="Password", bg="blue",fg="red")
myentry.grid(row=2, column=1, sticky="nsew")
# myentry.pack()

def handle_keypress(event):
    mytext = mylabel["text"]
    mylabel["text"] = mytext + event.char
    print(event.char)

def handle_leftclick(event):
    myentry.insert(2,"*")
    print(event.char)

mywindow.bind("<Key>", handle_keypress)
mywindow.bind("<Button-1>", handle_leftclick)

mywindow.mainloop()

# mywindow.destroy()
print("End program;")