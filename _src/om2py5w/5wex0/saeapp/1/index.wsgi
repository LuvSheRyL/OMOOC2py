# -*- coding: utf-8 -*-
#ref : https://wp-lai.gitbooks.io/learn-python/content/1sTry/sae.html
from bottle import route, run, template,get,post,request,Bottle,debug
import requests

import sae
import sae.kvdb
import time
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

count = 0

kv = sae.kvdb.Client()

#写数据库
def input_db(date_db):
    count += 1
    server_time = time.ctime()
    key = 'key' + str(count)
    value = {'time':ctime,'content':date_db}
    kv.set(key,value)

#读数据库
def output_db():
    server_db = []
    for i in kv.get_by_prefix('key'):
        server_db.append(i[1])
    return server_db
'''
@error(404)
def error404(error):
    return '网页跑丢了。。稍等'
'''
app = Bottle()


@route('/write') 
def diary_w():
    local_diary_txt = output_db()
    return template('diary_write.tpl',diary_textarea=local_diary_txt)

    

@route('/write',method='POST')
def do_diary_w():
    web_diary_text = request.forms.get('diary_text')
    input_db(web_diary_text)
    web_diary_text_db = output_db()
    return template('diary_write.tpl',diary_textarea=web_diary_text_db)
    
    
application = sae.create_wsgi_app(app)



