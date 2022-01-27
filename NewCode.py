from flask import Flask,request,jsonify
import random
import requests
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)
url = "http://numbersapi.com/"
@app.route("/getfact",methods=['POST'])
def getFact():
    req = request.get_json()
    intent = req.get("queryResult").get("intent").get("displayName")
    number = req.get("queryResult").get("parameters").get("number")
    qtype = req.get("queryResult").get("parameters").get("type")
    number2 = req.get("queryResult").get("parameters").get("number2")

    print(req)
    print(intent)
    print(number)
    print(qtype)
    if intent == "numbers":
        if qtype == "random":
            qtype = random.choice(["trivia","year","math"])
        qurl = url + str(int(number)) + "/" + qtype + "?json"
        res = requests.get(qurl).json()["text"]
        print("-----")
        print(res)
        print("-----")
        print(qurl)
        return jsonify({"fulfillmentText":res}) #prinnt on dialofflow
    if intent == "addition":
        addition = number + number2;
        print(addition)
        return jsonify({"fulfillmentText":addition});
    elif intent == "multiply":
        multiply = number * number2;
        print(multiply)
        return jsonify({"fulfillmentText":multiply});
    elif intent == "substraction":
        substraction = number - number2;
        print(substraction)
        return jsonify({"fulfillmentText":substraction});
    elif intent == "division":
        try:
            division = number / number2;
        except: 
            return jsonify({"fulfillmentText":"Ohh Your cant divide it by Zero"}); 
        return jsonify({"fulfillmentText":division});
    elif intent == "joke":
        jsonRespone = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&type=single').json()
        return jsonify({"fulfillmentText":jsonRespone['joke']});
    print(intent,number,qtype)
    print(req)  #print on server side
    return jsonify({"fulfillmentText":"Flask server hit"}) #return on client side
