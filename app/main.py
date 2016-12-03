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
        self.name = name
        self.email = email
        self.password = password
        self.role = role

@app.route("/login", methods=["POST", "GET"])
def login():
    response = {
        'success': False,
        'message': ''
    }
    
    # Login authentication
    if request.method == 'POST':
        post_request = json.loads(request.data.decode())
        user = post_request.get('data')
        login_user = user.get("username")
        login_password = user.get("password")

        # make query to db
        user_q = User.query.filter(
            User.username  == str(login_user)).first()

        if user_q:
            if login_user != user_q.username or \
                login_password != user_q.password:
    
                error = 'You shall not pass'
                response['message'] = error
            else:
                response['message'] = "OK"
                response['success'] = True
        else:
            response['message'] = 'User does not exist'

        # Load index
        return render_template("index.html")

    # Get request, load login
    return render_template("login.html")

@app.route("/index", methods=["POST", "GET"])
def index():

    response = {
        'success': False,
        'message': ''
    }
    
    # Login authentication
    if request.method == 'POST':
        post_request = json.loads(request.data.decode())
        user = post_request.get('data')
        login_user = user.get("username")
        login_password = user.get("password")

        # make query to db
        user_q = User.query.filter(
            User.username  == str(login_user)).first()

        if user_q:
            if login_user != user_q.username or \
                login_password != user_q.password:
    
                error = 'You shall not pass'
                response['message'] = error
            else:
                response['message'] = "OK"
                response['success'] = True
                return jsonify(response), 200
        else:
            response['message'] = 'User does not exist'

    return jsonify(response), 200

if __name__ == "__main__":
     app.run()