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
    print "Here I am."
    user1 = User("admin", "admin_name", "something@somewhere.com", "lolekbolek", False)
    db.session.add(user1)
    db.session.commit()
    print "User with name: %s | username: %s" % (user1.name, user1.username)
    return render_template("index.html")

if __name__ == "__main__":
     app.run()