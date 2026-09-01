#===========================================================
# Program: CryptoText
# Date: 2023/04/25
#===========================================================
# Create by: Juan Sirgado y Antico
# Copyright: JSyA Innovation Inc
#===========================================================
import os
from pathlib import Path

import rsa
import base64
import hashlib as hl

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import tkinter as tk
import tkinter.scrolledtext as st
import tkinter.messagebox as mb

event = []

class CryptoText: 
    str_user = ""
    str_pass = ""
    str_text = ""
    str_file = ""
    str__MD5 = ""
    bol_user = None
    cls_fernet = Fernet()

def set_variables():
    CryptoText.str_user = ent_user.get()
    CryptoText.str_pass = ent_pass.get()
    CryptoText.str__MD5 = hl.md5(CryptoText.str_user.encode('utf-8')).hexdigest()
    str_filename = "CryptoText_" + CryptoText.str__MD5 + ".bin"
    str_filepath = str(Path.home())
    CryptoText.str_file = str_filepath + "\\CryptoText\\" + str_filename
    CryptoText.bol_user = os.path.isfile(CryptoText.str_file)
    return()

def cmd_login():
    set_variables()
    if(CryptoText.bol_user != True):
        mb.showerror(title="Error", message="User do not exist!")
        return()
    frm_user.pack_forget()
    frm_text.pack()
    lbl_login.config(text="User: " + CryptoText.str_user)
    txt_text.delete("1.0", tk.END)
    file_read()
    return()

def cmd_logout():
    if(CryptoText.bol_user != True):
        mb.showerror(title="Error", message="User not logged!")
        return()
    if(CryptoText.str_text != txt_text.get("0.0", tk.END)):
       lbl_status.config(text="Text changed, save it.")
       return()
    frm_text.pack_forget()
    frm_user.pack()
    lbl_status.config(text="Enter the User and Password then click Login,\nor click Create User for a new User.")
    return()

def file_read():
    with open(CryptoText.str_file, mode="r", encoding="utf-8") as input_file:
        CryptoText.str_text = input_file.read()
        txt_text("1.0", CryptoText.str_text)
#        CryptoText.str_text = txt_text.get("1.0", tk.END)        
    return()

def file_write():
    with open(CryptoText.str_file, mode="w", encoding="utf-8") as output_file:
        CryptoText.str_text = txt_text.get("1.0", tk.END)
        output_file.write(CryptoText.str_text)
    return()

def cmd_save():
    set_variables()
    if(CryptoText.bol_user != True):
        mb.showerror(title="Error", message="User not logged!")
        return()    
    file_write()
    return()

def cmd_create():
    mb.askyesno(title="Create User Confirmation", message="Create a new User?")
    set_variables()
    print("My file: ", CryptoText.str_file)
    cmd_save()
    lbl_status.config(text="User created")
    return()

def cmd_delete():
    set_variables()
    if(CryptoText.bol_user != True):
        mb.showerror(title="Error", message="User not logged!")
        return()     
    mb.askyesno(title="Delete User Confirmation", message="All data will be lost.\nDelete current User?")
    os.remove(CryptoText.str_file)
    lbl_status.config(text="User deleted")
    return()

def cmd_show():
    frm_text.pack()
    lbl_status.config(text="Now you can see the text.")
    return()

def cmd_hide():
    frm_text.pack_forget()
    lbl_status.config(text="Now you can not see the text.")
    return()

def cmd_exit():
    if(CryptoText.bol_user != True):
        exit()
    if(CryptoText.str_text == txt_text.get("1.0", tk.END)):
        exit()
    bol_anser = mb.askyesnocancel(title="The text has been changed!", message="Save current text?")
    if(bol_anser == True): 
        cmd_save()
        exit()
    elif(bol_anser == False):
        exit()
    else:
        return()

#===========================================================
# RSA - Keys\Encrypt\Decrypt
#===========================================================

def rsa_keys():
   publicKey, privateKey = rsa.newkeys(1024)
   print("Private Key: ", privateKey)
   print("Public Key: ", publicKey)
   return(privateKey, publicKey)

def rsa_encrypt(str_decode:str, publicKey):
   byt_encode = str_decode.encode('utf-8')
   byt_encrypt = rsa.encrypt(byt_encode, publicKey)
   print("Decoded string: ", str_decode)
   print("Encoded string: ", byt_encode)
   print("Encrypted string: ", byt_encrypt)
   return(byt_encrypt)

def rsa_decrypt(byt_encrypt:bytes, privateKey):
   byt_decrypt = rsa.decrypt(byt_encrypt, privateKey)
   str_decode = byt_decrypt.decode()
   print("Encrypted string: ", byt_encrypt)
   print("Decrypted string: ", byt_decrypt)
   print("Decoded string: ", str_decode)
   return(str_decode)

#===========================================================
# String to Base64 to Fernet Key  
#===========================================================
def key_frnt():
    str_md5 = hl.md5(CryptoText.str_pass.encode('utf-8')).hexdigest()
    print("MD5: ", str_md5)
    byt_md5 = str_md5.encode('utf-8')
    byt_salt = str_md5[0:32:2].encode('utf-8')
    print("Salt: ", byt_salt)
#===========================================================
# Recomendation more than 480.000 interactions  
#===========================================================
    cls_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=byt_salt,
        iterations=524288)
#===========================================================
# String to Base64 to Fernet Key  
#===========================================================
    byt_kdf = cls_kdf.derive(byt_md5)
    byt_key = base64.urlsafe_b64encode(byt_kdf)
    CryptoText.cls_fernet = Fernet(byt_key)

def enc_fernet(str_decode:str):    
    byt_encode = str_decode.encode('utf-8')
    byt_encrypt = CryptoText.cls_fernet.encrypt(byt_encode)
    print("Token Encrypt: ", byt_encrypt)

def dec_fernet(byt_encrypt:bytes):    
    byt_decrypt = CryptoText.cls_fernet.decrypt(byt_encrypt)
    str_decode = byt_decrypt.decode('utf-8')
    print("Scmsg Decrypt: ", str_decode)
#===========================================================

def handle_keypress(event):
    return()

def handle_leftclick(event):
    return()

#===========================================================
# GUI Definition
#===========================================================
win_main = tk.Tk()
win_main.title("Python GUI Test")
win_main.geometry("640x640")

#===========================================================
# Frame User
#===========================================================
frm_user = tk.Frame(master=win_main, width=10, height=10, borderwidth=5)
frm_user.pack(fill=tk.BOTH, side=tk.TOP, expand=False)
frm_user.rowconfigure([0, 1, 2, 3], minsize=35, weight=1)
frm_user.columnconfigure([0, 1, 2, 3], minsize=10, weight=1)

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
btn_insert = tk.Button(master=frm_user, text="Create User", command=cmd_create)
btn_insert.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
btn_delete = tk.Button(master=frm_user, text="Delete User", command=cmd_delete)
btn_delete.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

#===========================================================
# Frame Text
#===========================================================
frm_text = tk.Frame(master=win_main, width=10, height=10, borderwidth=5)
frm_text.pack(fill=tk.BOTH,  side=tk.BOTTOM, expand=True)
frm_text.rowconfigure([0, 1, 2], minsize=35, weight=1)
frm_text.columnconfigure([0, 1, 2], minsize=10, weight=1)

lbl_login = tk.Label(master=frm_text ,text="")
lbl_login.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

txt_text = st.ScrolledText(master=frm_text, undo=True)
txt_text.grid(row=1, column=1, sticky="nsew")

lbl_status = tk.Label(master=frm_text ,text="Enter the User and Password then click Login,\nor click Create User for a new User.")
lbl_status.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

#===========================================================
# Frame Control
#===========================================================
frm_ctrl = tk.Frame(master=win_main, width=10, height=10, borderwidth=5)
frm_ctrl.pack(fill=tk.BOTH,  side=tk.BOTTOM, expand=False)
frm_ctrl.rowconfigure([0], minsize=35, weight=1)
frm_ctrl.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=10, weight=1)

btn_save = tk.Button(master=frm_ctrl, text="Save", command=cmd_save)
btn_save.grid(row=0, column=1, padx=5, pady=5, sticky="sew")
btn_show = tk.Button(master=frm_ctrl, text="Show", command=cmd_show)
btn_show.grid(row=0, column=2, padx=5, pady=5, sticky="sew")
btn_hide = tk.Button(master=frm_ctrl, text="Hide", command=cmd_hide)
btn_hide.grid(row=0, column=3, padx=5, pady=5, sticky="sew")
btn_logout = tk.Button(master=frm_ctrl, text="Logout", command=cmd_logout)
btn_logout.grid(row=0, column=4, padx=5, pady=5, sticky="sew")
btn_exit = tk.Button(master=frm_ctrl, text="Exit", command=cmd_exit)
btn_exit.grid(row=0, column=5, padx=5, pady=5, sticky="sew")

#===========================================================
# GUI Control
#===========================================================
win_main.bind("<Key>", handle_keypress)
win_main.bind("<Button-1>", handle_leftclick)

frm_text.pack_forget()
win_main.mainloop()
#win_main.destroy()

#===========================================================
# That is all folks!
#===========================================================