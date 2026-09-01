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
key = Fernet.generate_key()
#===========================================================
# Common variables
#===========================================================
class CryptoText: 
    str_user = ""
    str_pass = ""
    str_text = ""
    str_file = ""
    str_sufix = ""
    bol_user = False
    bol_new_user = False
    cls_fernet = Fernet(key)

def set_variables():
    CryptoText.str_user = ent_user.get()
    CryptoText.str_pass = ent_pass.get()
    str_base_MD5 = cmd_shuffle(CryptoText.str_user, CryptoText.str_pass)
    str_encode_MD5 = hl.md5(str_base_MD5.encode('utf-8')).hexdigest()
    str_filename = "CryptoText_" + str_encode_MD5 + ".bin"
    str_filepath = str(Path.home())
    CryptoText.str_file = "CryptoText/" + str_filename
    CryptoText.str_sufix = "_" + str_encode_MD5 + ".bin"
    return()

#===========================================================
# User control functions
#===========================================================
def cmd_login():
    set_variables()
    fernet_generate_key()
    check_user()
    if(CryptoText.bol_user != True):
        mb.showerror(title="Error", message="Invalid User and\\or Password\nYou are not logged!")
        return()
    frm_user.pack_forget()
    frm_text.pack()
    lbl_login.config(text="User: " + CryptoText.str_user)
    txt_text.delete("1.0", tk.END)
    file_read()
    lbl_status.config(text="User logged in successfully.")
    return()

def cmd_logout():
    if(CryptoText.bol_user != True):
        mb.showerror(title="Error", message="User not logged!")
        return()
    if(CryptoText.str_text != txt_text.get("1.0", tk.END)):
       lbl_status.config(text="Text changed, save it.")
       return()
    txt_text.delete("1.0", tk.END)
    frm_text.pack_forget()
    frm_user.pack()
    CryptoText.bol_user = False
    lbl_status.config(text="Enter the User and Password then click Login,\nor click Create User for a new User.")
    return()

def check_user():
    CryptoText.bol_user = os.path.isfile(CryptoText.str_file)
    return() 

#===========================================================
# User CRUD functions
#===========================================================
def cmd_create():
    mb.askyesno(title="Create User Confirmation", message="Create a new User?")
    set_variables()
    if(CryptoText.bol_user == True):
        mb.showerror(title="Error", message="User already exist!")
        return()
    fernet_generate_key()    
    rsa_generate_keys()
    CryptoText.bol_new_user = True
    cmd_update()
    CryptoText.bol_new_user = False
    frm_text.pack()
    CryptoText.bol_user = True
    lbl_status.config(text="User created")
    return()

def cmd_update():
    set_variables()
    if(CryptoText.bol_new_user != True):
       if(CryptoText.bol_user != True):
           mb.showerror(title="Error", message="User not logged!")
           return()    
    file_write()
    return()

def cmd_delete():
    set_variables()
    if(CryptoText.bol_user != True):
        mb.showerror(title="Error", message="User not logged!")
        return()     
    mb.askyesno(title="Delete User Confirmation", message="All data will be lost.\nDelete current User?")
    os.remove(CryptoText.str_file)
    CryptoText.bol_user = False
    lbl_status.config(text="User deleted")
    return()

#===========================================================
# File control functions
#===========================================================
def file_read():
    with open(CryptoText.str_file, mode="rb") as input_file:
        (publicKey, privateKey) = rsa_recover_keys()
        byt_encrypt = input_file.read()
        CryptoText.str_text = rsa_decrypt(byt_encrypt, privateKey)
        bol_hash = rsa_verify(CryptoText.str_text, publicKey)
        if( bol_hash != True):
           mb.showerror(title="Error", message="File signature is not valid!")
           return()  
        txt_text.insert("1.0", CryptoText.str_text)
        CryptoText.str_text = txt_text.get("1.0", tk.END)
    return()

def file_write():
    with open(CryptoText.str_file, mode="wb") as output_file:
        (publicKey, privateKey) = rsa_recover_keys()
        CryptoText.str_text = txt_text.get("1.0", tk.END)
        byt_signature = rsa_sign(CryptoText.str_text, privateKey)
        byt_encrypt = rsa_encrypt(CryptoText.str_text, publicKey)
        output_file.write(byt_encrypt)
    return()

#===========================================================
# GUI control functions
#===========================================================
def cmd_clear():
    if(CryptoText.bol_user != True):
        mb.showerror(title="Error", message="User not logged!")
        return()  
    lbl_status.config(text="Text cleared, Save before Exit.")
    txt_text.delete("1.0", tk.END)
    return()

def cmd_show():
    if(CryptoText.bol_user != True):
        mb.showerror(title="Error", message="User not logged!")
        return()  
    frm_text.pack()
    lbl_status.config(text="Now you can see the text.")
    return()

def cmd_hide():
    if(CryptoText.bol_user != True):
        mb.showerror(title="Error", message="User not logged!")
        return()  
    frm_text.pack_forget()
    lbl_status.config(text="Now you can not see the text.")
    return()

def cmd_exit():
    if(CryptoText.bol_user != True):
        exit()
    if(CryptoText.str_text == txt_text.get("1.0", tk.END)):
        exit()
    bol_answer = mb.askyesnocancel(title="The text has been changed!", message="Save current text?")
    if(bol_answer == True): 
        cmd_update()
        exit()
    elif(bol_answer == False):
        exit()
    else:
        return()

#===========================================================
# Shuffle - Strings
#===========================================================
def cmd_shuffle(str_value_1, str_value_2):
    int_lenght = len(str_value_2)
    str_shuffle = ""
    int_shuffle = int_lenght - 1
    for chr_loop in str_value_1:
        str_shuffle += chr_loop + str_value_2[int_shuffle:int_shuffle + 1]
        if (int_shuffle > 0):
            int_shuffle -= 1
    return(str_shuffle)

#===========================================================
# RSA - Keys\Encrypt\Decrypt
#===========================================================
def rsa_generate_keys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open("CryptoText/PublicKey" + CryptoText.str_sufix, "wb") as buf_writer:
        byt_encrytp = fernet_encrypt(publicKey.save_pkcs1("PEM"))
        buf_writer.write(byt_encrytp)
    with open("CryptoText/PrivateKey" + CryptoText.str_sufix, "wb") as buf_writer:
        byt_encrytp = fernet_encrypt(privateKey.save_pkcs1("PEM"))
        buf_writer.write(byt_encrytp)
    return()

def rsa_recover_keys():
    with open("CryptoText/PublicKey" + CryptoText.str_sufix, "rb") as buf_reader:
        byt_decrypt = fernet_decrypt(buf_reader.read())
        publicKey = rsa.PublicKey.load_pkcs1(byt_decrypt)
    with open("CryptoText/PrivateKey" + CryptoText.str_sufix, "rb") as buf_reader:
        byt_decrypt = fernet_decrypt(buf_reader.read())
        privateKey = rsa.PrivateKey.load_pkcs1(byt_decrypt)
    return(publicKey, privateKey)

def rsa_encrypt(str_decode:str, publicKey):
    byt_encode = str_decode.encode("utf-8")
    byt_encrypt = rsa.encrypt(byt_encode, publicKey)
    return(byt_encrypt)

def rsa_decrypt(byt_encrypt:bytes, privateKey):
    byt_decrypt = rsa.decrypt(byt_encrypt, privateKey)
    str_decode = byt_decrypt.decode("utf-8")
    return(str_decode)

def rsa_sign(str_decode:str, privateKey):
    byt_encode = str_decode.encode("utf-8")
    byt_signature = rsa.sign(byt_encode, privateKey, "SHA-256")
    byt_encrypt = fernet_encrypt(byt_signature)
    with open("CryptoText/Signature" + CryptoText.str_sufix, "wb") as buf_writer:
        buf_writer.write(byt_encrypt) 
    return(byt_signature)

def rsa_verify(str_decode:str, publicKey):
    with open("CryptoText/Signature" + CryptoText.str_sufix, "rb") as buf_reader:
        byt_encrypt = buf_reader.read()
    byt_signature = fernet_decrypt(byt_encrypt)
    byt_encode = str_decode.encode("utf-8")
    try:
        str_hash = rsa.verify(byt_encode, byt_signature, publicKey)
        bol_return = True
    except:
        bol_return = False
    return (bol_return)

#===========================================================
# String to Base64 to Fernet Key  
#===========================================================
def fernet_generate_key():
    str_md5 = hl.md5(CryptoText.str_pass.encode("utf-8")).hexdigest()
    byt_md5 = str_md5.encode("utf-8")
    byt_salt = str_md5[0:32:2].encode("utf-8")
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
    return()

def fernet_encrypt(byt_encode:bytes):
    byt_encrypt = CryptoText.cls_fernet.encrypt(byt_encode)
    return(byt_encrypt)

def fernet_decrypt(byt_encrypt:bytes):    
    byt_encode = CryptoText.cls_fernet.decrypt(byt_encrypt)
    return(byt_encode)

#===========================================================
# Keyboard and Mouse Events Handle
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
# GUI User Frame
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
ent_pass = tk.Entry(master=frm_user ,text="", show="*")
ent_pass.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

btn_login = tk.Button(master=frm_user, text="Login", command=cmd_login)
btn_login.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
btn_insert = tk.Button(master=frm_user, text="Create User", command=cmd_create)
btn_insert.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
btn_delete = tk.Button(master=frm_user, text="Delete User", command=cmd_delete)
btn_delete.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

#===========================================================
# GUI Text Frame
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
# GUI Control Frame
#===========================================================
frm_ctrl = tk.Frame(master=win_main, width=10, height=10, borderwidth=5)
frm_ctrl.pack(fill=tk.BOTH,  side=tk.BOTTOM, expand=False)
frm_ctrl.rowconfigure([0], minsize=35, weight=1)
frm_ctrl.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=10, weight=1)

btn_clear = tk.Button(master=frm_ctrl, text="Clear", command=cmd_clear)
btn_clear.grid(row=0, column=1, padx=5, pady=5, sticky="sew")
btn_save = tk.Button(master=frm_ctrl, text="Save", command=cmd_update)
btn_save.grid(row=0, column=2, padx=5, pady=5, sticky="sew")
btn_show = tk.Button(master=frm_ctrl, text="Show", command=cmd_show)
btn_show.grid(row=0, column=3, padx=5, pady=5, sticky="sew")
btn_hide = tk.Button(master=frm_ctrl, text="Hide", command=cmd_hide)
btn_hide.grid(row=0, column=4, padx=5, pady=5, sticky="sew")
btn_logout = tk.Button(master=frm_ctrl, text="Logout", command=cmd_logout)
btn_logout.grid(row=0, column=5, padx=5, pady=5, sticky="sew")
btn_exit = tk.Button(master=frm_ctrl, text="Exit", command=cmd_exit)
btn_exit.grid(row=0, column=6, padx=5, pady=5, sticky="sew")

#===========================================================
# GUI Control
#===========================================================
win_main.bind("<Key>", handle_keypress)
win_main.bind("<Button-1>", handle_leftclick)

ent_user.insert(0, "admin")
ent_pass.insert(0, "test")

frm_text.pack_forget()
ent_user.focus()

win_main.mainloop()
#win_main.destroy()

#===========================================================
# That is all folks!
#===========================================================