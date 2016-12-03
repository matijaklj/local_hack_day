import os

from flask import Flask, render_template, \
    request, url_for, redirect, session, flash, g, jsonify

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app import app, db

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