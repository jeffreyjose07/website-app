from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jose'}
    posts = [
        {
            'author': {'username': 'Jose'},
            'body': 'Beautiful day!'
        },
        {
            'author': {'username': 'Mini'},
            'body': 'Its a rainy day!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
