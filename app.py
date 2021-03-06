# import the model after import the db
from models import *

from flask import (
    flash,
    Flask,
    render_template,
    redirect,
    request,
    url_for,
    session
)
from flask_sqlalchemy import SQLAlchemy
# = from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
# import sqlite3

app = Flask(__name__)
app.secret_key = "xdfaskjmkd"
app.database = "sample.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# create the sqlalchemy object
db = SQLAlchemy(app)


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login.')
            return redirect(url_for('login'))
        return wrap


@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if (
            request.form['username'] != 'admin' or
                request.form['password'] != 'admin'
        ):
            error = 'Incorrect Username or Password. Please try again.'
        else:
            session['logged_in'] = True
            flash('You are just logged in')
            return redirect(url_for('home'))
        return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You are just logged out')
    return redirect(url_for('welcome'))


# def connect_db():
#   return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run(debug=True)
