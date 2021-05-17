import os
from flask import Flask,render_template, request,json, jsonify
import jwt
import requests

app = Flask(__name__)

users = [
    {
        "token": "admin",
        "user_info": {
            "username": "admin",
            "first_name": "admin",
            "last_name": "admin",
            "email": "admin@fab.org",
        },
    },
    {
        "token": "admin2",
        "user_info": {
            "username": "admin2",
            "first_name": "admin2",
            "last_name": "admin2",
            "email": "admin2@fab.org",
        },
    },
    {
        "token": "karen",
        "user_info": {
            "username": "karen",
            "first_name": "karen",
            "last_name": "karen",
            "email": "karen@fab.org",
        },
    },
    {
        "token": "karen2",
        "user_info": {
            "username": "karen2",
            "first_name": "karen2",
            "last_name": "karen2",
            "email": "karen2@fab.org",
        },
    },
    {
        "token": "alpha1",
        "user_info": {
            "username": "alpha1",
            "first_name": "alpha1",
            "last_name": "alpha1",
            "email": "alpha1@fab.org",
        },
    },
    {
        "token": "gamma1",
        "user_info": {
            "username": "gamma1",
            "first_name": "gamma1",
            "last_name": "gamma1",
            "email": "gamma1@fab.org",
        },
    },
    {
        "token": "alpha2",
        "user_info": {
            "username": "alpha2",
            "first_name": "alpha2",
            "last_name": "alpha2",
            "email": "alpha2@fab.org",
        },
    },
    {
        "token": "gamma2",
        "user_info": {
            "username": "gamma2",
            "first_name": "gamma2",
            "last_name": "gamma2",
            "email": "gamma2@fab.org",
        },
    },
    {
        "token": "admin3",
        "user_info": {
            "username": "admin3",
            "first_name": "admin3",
            "last_name": "admin3",
            "email": "admin3@fab.org",
        },
    },
]


@app.route("/user/info", methods=["GET"])
def get_user_info():
    token = request.args.get("token")

    if token is not None:
        search = list(filter(lambda person: person["token"] == token, users))
        if search != []:
            user_info = search[0]["user_info"]
            print(user_info)
            return jsonify(user_info)

    return jsonify(None)


@app.route('/login')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    encoded_jwt = jwt.encode({"some": str(user)}, "secret", algorithm="HS256")
    rp = requests.get(url='http://127.0.0.1:5000/dashboard')
    return rp.text
    #return json.dumps({'status':'OK','user':user,'pass':password, 'encoded_jwt': encoded_jwt});


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')


if __name__=="__main__":
    app.run()
