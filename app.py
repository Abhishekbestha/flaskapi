from flask import Flask, request
import os
from datetime import datetime
import hashlib
import requests

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
    # accesskey = "Desktop_App"
    sha256_hash = hashlib.sha256()
    a_string = accesskey + str(ts) + str(txn)
    encoded_string = a_string.encode()
    byte_array = bytearray(encoded_string)
    sha256_hash.update(byte_array)
    hash = sha256_hash.hexdigest()
    # content= request.json

    return {"ts":ts,"txn":txn,"hash":hash}

# <-------------------------------------------------------------------------->

@app.route("/covid", methods=["POST"])
def covid():
    if request.method == 'POST':
        global country
        new_country = request.form.get('country')
        country = new_country

    # print(country)
    url = "https://coronavirus-19-api.herokuapp.com/countries/{}"

    # print(url)
    r = requests.get(url.format(country)).json()
    # print(r)
    covid = {
                'country': country.upper(),
                'confirmed': r['cases'],
                'recovered': r['recovered'],
                'critical': r['critical'],
                'deaths': r['deaths'],
                'todayCases': r['todayCases'],
                'todayDeaths': r['todayDeaths'],
                'active': r['active'],
                'totalTests': r['totalTests'],
            }

    # print(covid)

    return covid


# <-------------------------------------------------------------------------->

@app.route("/countries", methods=['POST', 'GET'])
def countries():
    url = "https://countriesnow.space/api/v0.1/countries/states"
    if request.method == 'GET':
        r = requests.get(url)
    else:
        content = request.json
        countries = content["country"]
        # print(countries)
        data = {"country": f"{countries}"}
        r = requests.post(url, data)
    # print(r)
    aresp = r.json()
    return aresp




if __name__== "__main__":
    app.run()
