import tkinter as tk

mywindow = tk.Tk()
myframe = tk.Frame()
myframe.pack()

mylabel = tk.Label(master=myframe, text="Name", width=10, height=5, bg="blue",fg="red")
myentry = tk.Entry(master=myframe, text="Password", width=10, bg="blue",fg="red")
mybutton = tk.Button(master=myframe, text="Button", width=10, height=5, bg="blue",fg="red")

mylabel.pack()
myentry.pack()
mybutton.pack()

mywindow.mainloop()

myname = myentry.get()
myentry.delete(0, tk.END)
myentry.insert(0,"Password")

print("Name: ", myname)

mywindow.destroy()