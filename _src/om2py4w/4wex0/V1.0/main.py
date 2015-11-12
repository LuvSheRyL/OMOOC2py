# -*- coding: utf-8 -*-
from bottle import route, run, template,get,post,request,error,FormsDict
from my_diary import append_text,get_text 



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
    

@route('/write') 
def diary_w():
    local_diary_txt = get_text()
    return template('diary_write.tpl',diary_textarea=local_diary_txt)

@route('/write',method='POST')
def do_diary_w():
    web_diary_text = request.forms.get('diary_text')
    append_text(web_diary_text)
    return template('diary_write.tpl',diary_textarea=web_diary_text)
    
@get('/read')
def diary_w():

        f = open('mydiary.txt')
        content = f.read()
        f.close
        return template('diary_write.tpl',diary_textarea=content)
        
    
run(host='localhost', port=8080,debug=True,reloader=True)