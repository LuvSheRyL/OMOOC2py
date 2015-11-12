# -*- coding: utf-8 -*-
from bottle import route, run, template,get,post,request,error,FormsDict
from my_diary import append_text,get_text 
import diary_sqlsever


@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hi {{name}}, how are you?', name=name)


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
        
@get('/diary')
def diary_sql_show():
    diary_sql_text = diary_sqlsever.fetchall_test()
    return template('diary_write.tpl',diary_textarea=diary_sql_text)
        
        
run(host='localhost', port=8080,debug=True,reloader=True)