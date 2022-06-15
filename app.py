from flask import Flask, request


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
    img1_file= open("https://github.com/Abhishekbestha/flaskapi/tree/main/data"+"/"+text+".jpg", "wb")
    img1_file.write(img)

    return "Succesfully saved the image"

@app.route("/img", methods=["POST"])
def img():
    imagefile = request.files
    textfile = request.form
    text= textfile["text"]
    image= imagefile["image"]
    save_img(text, image)

    return "Image saved Successfully"




if __name__== "__main__":
    app.run()
