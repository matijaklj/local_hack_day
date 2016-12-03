# Global imports
import os

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

@app.route("/", methods=["POST", "GET"])
def login():
    # Login authentication
    if request.method == 'POST':
        
        login_user = request.form.get('data.username', type=str)
        login_password = request.form.get('data.password', type=str)

        user = User.query.filter(
            User.username  == str(login_user)).first()

        if login_user != user.username or \
            login_password != user.password:
                error = 'You shall not pass'
        else:
            # Sesion
            rp = { 
                'connected': False,
                'ip': None,
                'action': 'connect'
            }
            session['rp'] = rp
            session['logged_in'] = True
            session['logged_user'] = user.username
            session['first_log'] = False
    return render_template

if __name__ == "__main__":
     app.run()