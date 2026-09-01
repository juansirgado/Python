import os
from pathlib import Path
import tkinter as tk
import tkinter.scrolledtext as st
import tkinter.messagebox as mb

win_main = tk.Tk()
win_main.title("Python GUI Test")
win_main.geometry("640x640")

event = []

def file_exist():
    return os.path.isfile(filepath)

def cmd_login():
    lbl_login.config(text="User: " + ent_user.get())
    frm_user.destroy()
    txt_text.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_text.insert(tk.END, text)
    return

def cmd_insert():
    mb.askyesno(title="Insert User Confirmation", message="Insert new User?")
    lbl_status.config(text="User inserted")
    return

def cmd_delete():
    mb.askyesno(title="Delete User Confirmation", message="All data will be lost.\nDelete current User?")
    lbl_status.config(text="User deleted")
    return

def cmd_save():
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_text.get("1.0", tk.END)
        output_file.write(text)
    return

def cmd_exit():
    mb.askyesnocancel(title="The text has been changed!", message="Save current text?")
    return

def cmd_show():
    lbl_status.config(text="Now you can see the text.")
    return

def cmd_hide():
    lbl_status.config(text="Now you can not see the text.")
    return

def handle_keypress(event):
    #cur_text = txt_text.get("0.0",tk.END)
    #txt_text.insert(tk.END, cur_text + event.char)
    #print(event.char)
    return

def handle_leftclick(event):
    #ent_pass.insert(tk.END,"*")
    #frm_user.destroy()
    #print(event.char)
    return

frm_user = tk.Frame(master=win_main, width=10, height=10, borderwidth=5)
frm_user.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
frm_user.rowconfigure([0, 1, 2, 3], minsize=25, weight=1)
frm_user.columnconfigure([0, 1, 2, 3], minsize=10, weight=1)

frm_ctrl = tk.Frame(master=win_main, width=10, height=10, borderwidth=5)
frm_ctrl.pack(fill=tk.BOTH,  side=tk.BOTTOM, expand=False)
frm_ctrl.rowconfigure([0], minsize=35, weight=1)
frm_ctrl.columnconfigure([0, 1, 2, 3, 4, 5], minsize=10, weight=1)

frm_text = tk.Frame(master=win_main, width=10, height=10, borderwidth=5)
frm_text.pack(fill=tk.BOTH,  side=tk.BOTTOM, expand=True)
frm_text.rowconfigure([0, 1, 2], minsize=35, weight=1)
frm_text.columnconfigure([0, 1, 2], minsize=10, weight=2)

lbl_user = tk.Label(master=frm_user ,text="User:")
lbl_user.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
ent_user = tk.Entry(master=frm_user ,text="")
ent_user.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

lbl_pass = tk.Label(master=frm_user ,text="Password:")
lbl_pass.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
ent_pass = tk.Entry(master=frm_user ,text="")
ent_pass.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

btn_login = tk.Button(master=frm_user, text="Login", command=cmd_login)
btn_login.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
btn_insert = tk.Button(master=frm_user, text="Insert User", command=cmd_insert)
btn_insert.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
btn_delete = tk.Button(master=frm_user, text="Delete User", command=cmd_delete)
btn_delete.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

btn_save = tk.Button(master=frm_ctrl, text="Save", command=cmd_save)
btn_save.grid(row=0, column=1, padx=5, pady=5, sticky="sew")
btn_show = tk.Button(master=frm_ctrl, text="Show", command=cmd_show)
btn_show.grid(row=0, column=2, padx=5, pady=5, sticky="sew")
btn_hide = tk.Button(master=frm_ctrl, text="Hide", command=cmd_hide)
btn_hide.grid(row=0, column=3, padx=5, pady=5, sticky="sew")
btn_exit = tk.Button(master=frm_ctrl, text="Exit", command=cmd_exit)
btn_exit.grid(row=0, column=4, padx=5, pady=5, sticky="sew")

lbl_login = tk.Label(master=frm_text ,text="")
lbl_login.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

#txt_text = tk.Text(master=frm_text )
txt_text = st.ScrolledText(master=frm_text, undo=True)
txt_text.grid(row=1, column=1, sticky="nsew")
txt_text.insert(tk.END, "My text is here.")

lbl_status = tk.Label(master=frm_text ,text="Enter the User and Password then click Login.")
lbl_status.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

#filepath = os.path.abspath(os.path.curdir)
filepath = str(Path.home())
filename = filepath + "/MD5.JSON"

win_main.bind("<Key>", handle_keypress)
win_main.bind("<Button-1>", handle_leftclick)

win_main.mainloop()

# mywindow.destroy()
print("End program;")