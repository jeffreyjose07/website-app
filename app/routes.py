from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jose'}
    return '''
<html>
    <head>
        <title>Home Page - My web site</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''