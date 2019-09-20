from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12).hex()
from handymia import routes

'''
from flask import Flask, render_template
from handymia.forms import LoginForm
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12).hex()

@app.route('/')
@app.route('/index')
def index():
    welcome = {'message': 'Welcome to HandyMia'}
    return render_template("main.html", title='Home', welcome=welcome)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
'''