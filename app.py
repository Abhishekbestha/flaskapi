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




if __name__== "__main__":
    app.run()
