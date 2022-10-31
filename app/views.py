# _*_ encoding: utf-8 _*_
# @Author    : fly
# @Time      : 2022/10/30 0:46
# @Email     :
# @File      : views.py.py
# @License   : Do What The F*ck You Want To Public License
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''