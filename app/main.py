# Global imports
import os
import json

from flask import Flask, render_template, \
    request, url_for, redirect, session, flash, g, jsonify

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship

APP_SETTINGS="config.DevelopmentConfig"

app = Flask(__name__, template_folder='static/templates')
app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database views definitions
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, default="root")
    is_teacher = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, name, email, role=False):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.role = role

@app.route("/login", methods=["POST", "GET"])
def login():

    
    response = {
        'success': False,
        'msg': ''
    }
    
    # Login authentication
    if request.method == 'POST':
        post_request = json.loads(request.data.decode())
        user = post_request.get('user')
        login_user = request.form.get('user.username', type=str)
        login_password = request.form.get('user.password', type=str)

        user_q = User.query.filter(
            User.username  == str(login_user)).first()

        if login_user != user_q.username or \
            login_password != user_q.password:
            error = 'You shall not pass'
            response['msg'] = error
            return jsonify(response), 504
    else:
        return render_template("login.html")

    response['success'] = True
    response['msg'] = "success"
    return jsonify(response), 200

@app.route("/index", methods=["POST", "GET"])
def login():

    
    response = {
        'success': False,
        'msg': ''
    }
    
    # Login authentication
    if request.method == 'POST':
        post_request = json.loads(request.data.decode())
        user = post_request.get('user')
        login_user = request.form.get('user.username', type=str)
        login_password = request.form.get('user.password', type=str)

        user_q = User.query.filter(
            User.username  == str(login_user)).first()

        if login_user != user_q.username or \
            login_password != user_q.password:

            error = 'You shall not pass'
            response['msg'] = error
            return jsonify(response), 504
    else:
        return render_template("login.html")

    response['success'] = True
    response['msg'] = "success"
    return jsonify(response), 200

if __name__ == "__main__":
     app.run()