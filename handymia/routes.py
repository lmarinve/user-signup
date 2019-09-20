from flask import render_template
from handymia import app
from handymia.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    welcome = {'message': 'Welcome to HandyMia'}
    return render_template("main.html", title='Home', welcome=welcome)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)
'''
from flask import render_template
from handymia import app
#from handymia.handymia import LoginForm


@app.route('/')
@app.route('/index')
def index():
    welcome = {'message': 'Welcome to HandyMia'}
    return render_template("main.html", title='Home', welcome=welcome)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)
'''
