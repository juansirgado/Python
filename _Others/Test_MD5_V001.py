import os
import hashlib as hl
from pathlib import Path

txt_user = "juan.sirgado@hotmail.com"
md5_string = hl.md5(txt_user.encode('utf-8')).hexdigest()
print(md5_string)

txt_filename = "file_" + md5_string + ".json"
txt_output = "Test 123 ...; "

#txt_edit.delete("1.0", tk.END)
filepath = str(Path.home())
filename = filepath + "\\CryptoText\\" + txt_filename
print("Filename: ", filename)

print("File exist? ", os.path.isfile(filename))

with open(filename, mode="r", encoding="utf-8") as input_file:
    txt_input = input_file.read()
#    txt_edit.delete("0.0", tk.END)
#    txt_edit.insert("0.0", text)
print("Input: ", txt_input)

with open(filename, mode="w", encoding="utf-8") as output_file:
#    txt_output = txt_text.get("0.0", tk.END)
    output_file.write(txt_output)
print("Output: ", txt_output)

print("End program;")