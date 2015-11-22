# -*- coding: utf-8 -*-
#ref : https://wp-lai.gitbooks.io/learn-python/content/1sTry/sae.html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bottle import route, run, template,get,post,request,Bottle,debug
import requests

import sae
import sae.kvdb
import time


count = 0

kv = sae.kvdb.Client()

#写数据库
def input_db(date_db):
    count = count + 1
    server_time = time.ctime()
    key = 'key' + str(count)
    value = {'time':ctime,'content':date_db}
    kv.set(key,value)

#读数据库
def output_db():
    tmp = [item[1] for item in list(kv.get_by_prefix('key'))]
    results = sorted(tmp, key = lambda x:x['time'], reverse=True)
    return results
    
'''
@error(404)
def error404(error):
    return '网页跑丢了。。稍等'
'''
app = Bottle()


@app.route('/') 
def diary_w():
    local_diary_txt = output_db()
    return template('diary_diary.tpl',diary_textarea=local_diary_txt)

    

@app.route('/',method='POST')
def do_diary_w():
    web_diary_text = request.forms.get('diary_text')
    input_db(web_diary_text)
    web_diary_text_db = output_db()
    return template('diary_diary.tpl',diary_textarea=web_diary_text_db)
    
    
application = sae.create_wsgi_app(app)



