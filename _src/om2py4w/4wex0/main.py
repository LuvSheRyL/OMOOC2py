# -*- coding: utf-8 -*-
from bottle import route, run, template,get,post,request,error,FormsDict

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hi {{name}}, how are you?', name=name)

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.getunicode('username')
    password = request.forms.getunicode('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

# 添加错误提示
@error(404)
def error404(error):
    return '网页跑丢了。。稍等'
    

@route('/diary') #

def diary():
    return '''

    <hr>
    <form action="diary" method="get">

            
            <br>
            <center>
            <textarea rows="10" cols="50" id="diary_text" readonly>
My diary
            </textarea>
            <center>
            My diary: <input type="text" name="diary_text" />
            <input type="submit" value="Updata" /><br>
    </form>
    '''

    
run(host='localhost', port=8080,debug=True)