from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.model):
    pass


class User(db.model):
    pass

@app.before_request

def require_login():
    pass


@app.route("/blog")
def blog():
    pass

@app.route("/login", methods=['GET', 'POST'])
def login():
    pass

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    pass

@app.route("/newpost", methods=['GET', 'POST'])
def newpost():
    pass

@app.route("/logout")
def logout():
    pass

app.run()