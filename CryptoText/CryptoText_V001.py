import base64
import hashlib as hl
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

user = "admin"
password = "password"
message = "Secret message!"
# salt = os.urandom(16)
salt = user[0:4:2].encode('utf-8')
print("Salt: ", salt)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=524288)

key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
frn = Fernet(key)
token = frn.encrypt(message.encode('utf-8'))
print("Token Encrypt: ", token)
scmsg = frn.decrypt(token)
print("Scmsg Decrypt: ", scmsg.decode('utf-8'))

#===========================================================

pwd = password 

key = Fernet.generate_key()
fnk = Fernet(key)
print("Fernet key: ", key)

md5_string = hl.md5(pwd.encode('utf-8')).hexdigest()
print("MD5: ", md5_string)
b_md5 = md5_string.encode('utf-8')

myKey = base64.urlsafe_b64encode(b_md5)
fnk = Fernet(myKey)

epw = fnk.encrypt(pwd.encode('utf-8'))
epw = b'gAAAAABkRM7xiko0hJHwPlx2ggkvn8didomFUf2UkAp7-Jwo_WH4PYmQebCP0IeckorMK9lRuB1OJBznu-UfxYMN0mpF4g9Uzw=='

print("Original string: ", pwd)
print("Encrypted string: ", epw)

dpw = fnk.decrypt(epw).decode('utf-8')
 
print("Decrypted string: ", dpw)

str_user = "admin"
str_pass = "password"
str_mess = "Secret message!"

def key_mdfn():
#===========================================================
# string to MD5 to bytes encode utf-8
#===========================================================
    str_md5 = hl.md5(str_pass.encode('utf-8')).hexdigest()
    print("MD5: ", str_md5)
    byt_md5 = str_md5.encode('utf-8')
#===========================================================
# MD5 to Base64 to Fernet Key
#===========================================================
    byt_key = base64.urlsafe_b64encode(byt_md5)
    cls_fernet = Fernet(byt_key)
    print("Fernet key: ", cls_fernet)
    return(cls_fernet)

def key_mdfn(cls_fernet, str_decode):
    byt_encode = str_decode.encode('utf-8')
    byt_encrypt = cls_fernet.encrypt(byt_encode)
    print("Decoded string: ", str_pass)
    print("Encoded no-Encrypted string: ", byt_encode)
    print("Encrypted string: ", byt_encrypt)
    return(byt_encode)

def key_mdfn(cls_fernet, byt_encrypt):
    byt_decrypt = cls_fernet.decrypt(byt_encrypt)
    str_decode = byt_decrypt.decode('utf-8')
    print("Encrypted string: ", byt_encrypt)
    print("Encoded yes-Decrypted string: ", byt_decrypt)
    print("Decoded string: ", str_decode)
    return(str_decode)