from flask import Flask, request
import os
from datetime import datetime
import hashlib

app= Flask(__name__)


@app.route("/home", methods=["POST"])
def home():
    content= request.form
    # print(content)
    text= content["text"]
    if text.isalpha()==True:

        return "welcome"

    else:
        return "Bye"

# <----------------------------------------------------------->

@app.route("/user", methods=["POST"])
def user():
    content= request.json

    text= content["Name"]
    if text=="Abhi":

        return {"Response Message":"welcome Boss"},200

    else:
        return {"Response Message":"Who are you mad fellow?"}

# <------------------------------------------------------------------------>

def save_img(text, image):
    # if not os.path.exists("C:/Users/21701/Downloads"+"/"+text):
    #     os.mkdir("C:/Users/21701/Downloads"+"/"+text)
    # img1_file= open("C:/Users/21701/Downloads"+"/"+text+"/"+text+".jpg", "wb")
    img=image.read()
    img1_file= open("C:/Users/21701/Downloads"+"/"+text+".jpg", "wb")
    img1_file.write(img)

    return "Succesfully saved the image"

@app.route("/img", methods=["POST"])
def img():
    imagefile = request.files
    textfile = request.form
    text= textfile["text"]
    image= imagefile["image"]
    save_img(text, image)
    my_date = datetime.now()
    ts = my_date.isoformat().split(".")[0]
    return {'TS':ts,'Response msg': "Image saved"}

# <-------------------------------------------------------------------------->


@app.route("/time", methods=["POST"])
def time():
    content= request.form

    my_date = datetime.now()
    txn = my_date.strftime('%Y%m%d%H%M%S')
    ts = my_date.isoformat().split(".")[0]
    accesskey = content["accesskey"]
    # accesskey = "${{ACCESSKEY}}"
    sha256_hash = hashlib.sha256()
    a_string = accesskey + str(ts) + str(txn)
    encoded_string = a_string.encode()
    byte_array = bytearray(encoded_string)
    sha256_hash.update(byte_array)
    hash = sha256_hash.hexdigest()
    # content= request.json


    return {"ts":ts,"txn":txn,"hash":hash}


if __name__== "__main__":
    app.run()
