#----------------------------------------------------------#
#           Program: Plagiarism 2025/08/30                 #
#               All rights reserved 2025                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Description:                                             # 
# Test of Plagiarism                                       #
#----------------------------------------------------------#

from flask import Flask
from flask import request
from flask import render_template
import random

app = Flask(__name__)

web_page = """
<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Enter the texts to be compared</h1>
    <form action="." method="POST">
        <input type="text" name="text1">
        <input type="text" name="text2">
        <input type="submit" name="my-form" value="Check !">
    </form>
</body>
</html>
"""

plg_yes = "<h1>Plagiarism Detected !</h1>"
plg_not = "<h1>No Plagiarism Detected !</h1>"

@app.route('/')
def my_form():
    # return render_template("my-form.html") # This should be the name of your HTML file
    return web_page # This should be the name of your HTML file

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    plagiarismPercent = random.randrange(1,100)
    if plagiarismPercent > 50 :
        return plg_yes
    else :
        return plg_not

if __name__ == '__main__':
    app.run()
