import crypt
import tkinter as tk

max_attempts = 3     
attempt = 0          
stored_pw_hash = 'aa0GPiClW35DQ'

try:

     while attempt < max_attempts:

        uname = input('Username: ')  
        entered_pw_hash = crypt.crypt(input('pass: '), stored_pw_hash)

        if uname == 'admin' and entered_pw_hash == stored_pw_hash:
            print('Welcome Admin')
            break
        else:
            attempt += 1
            if attempt == max_attempts:
                raise RuntimeError("\nYou've reached the maximum number of attempts allowed.")

            else:
                print('Wrong credentials.\n Try again or press <ctrl+c> to exit.\n')
                continue

except KeyboardInterrupt:
    print('Terminated by the user.\nGood-bye.')

except RuntimeError as excep:
    print("Goodbye")

win_main = tk.Tk()
win_main.title("Python GUI Test")
win_main.geometry("800x600")

event = []

frm_user = tk.Frame(master=win_main, width=150, height=150, borderwidth=1)
frm_user.pack(fill=tk.X, side=tk.TOP, expand=True)
frm_user.rowconfigure([0, 1, 2, 4],minsize=50, weight=5)
frm_user.columnconfigure([0, 1, 2],minsize=50, weight=5)

frm_text = tk.Frame(master=win_main, width=150, height=150, borderwidth=1)
frm_text.pack(fill=tk.X,  side=tk.BOTTOM, expand=True)
frm_text.rowconfigure([0],minsize=50, weight=5)
frm_text.columnconfigure([0],minsize=50, weight=5)

lbl_user = tk.Label(master=frm_user,text="User:")
lbl_user.grid(row=1, column=1, sticky="nsew")

ent_user = tk.Entry(master=frm_user,text="")
ent_user.grid(row=2, column=1, sticky="nsew")

lbl_pass = tk.Label(master=frm_user,text="Password:")
ent_pass = tk.Entry(master=frm_user,text="")

txt_text = tk.Text(text="")
btn_login = tk.Button(text="Login")
btn_logout = tk.Button(text="Logout")
btn_insert = tk.Button(text="Insert")
btn_delete = tk.Button(text="Delete")

def handle_keypress(event):
    cur_text = txt_text["text"]
    txt_text["text"] = cur_text + event.char
    #print(event.char)

def handle_leftclick(event):
    ent_pass.insert(tk.END,"*")
    print(event.char)

mywindow.bind("<Key>", handle_keypress)
mywindow.bind("<Button-1>", handle_leftclick)

mywindow.mainloop()

# mywindow.destroy()
print("End program;")