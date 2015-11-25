# -*- coding: utf-8 -*-
#ref : https://wp-lai.gitbooks.io/learn-python/content/1sTry/sae.html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bottle import route, run, template,get,post,request,Bottle,debug
import requests
import os
import sae
import sae.kvdb
import time


count = 0

kv = sae.kvdb.Client()

# 将id和访问数储存进KVDB里
if kv.get('globalvar_id'):
    pass
else:
    kv.set('globalvar_id',0)

if kv.get('globalvar_traffic'):
    pass
else:
    kv.set('globalvar_traffic',0)

#写数据库
def input_db(date_db,tags):

    key_id = kv.get('globalvar_id')
    kv.set('globalvar_id', key_id+1)
    server_time = time.ctime()
    key = 'key' + str(key_id)
    tags = tags if tags else ['NULL']
    value = {'time':server_time,'content':date_db,'tags':tags}
    kv.set(key,value)
    for tag in tags:
        if kv.get(tag):
            kv.replace(tag, kv.get(tag)+[key])
        else:
            kv.set(tag, [key])

#读数据库
def output_db():
    tmp = [item[1] for item in list(kv.get_by_prefix('key'))]
    results = sorted(tmp, key = lambda x:x['time'], reverse=True)
    return results

# 读取对应tag的信息
def get_tag_data(tag):
    if kv.get(tag):
        keys = kv.get(tag)
        tmp = kv.get_multi(keys)
        results = [tmp[key] for key in sorted(tmp.keys(), reverse=True)]
        return results
    else:
        return []
'''
@error(404)
def error404(error):
    return '网页跑丢了。。稍等'
'''
app = Bottle()


@app.route('/') 
def diary_w():
    traffic = kv.get('globalvar_traffic')
    kv.set('globalvar_traffic', traffic+1)
    traffic = kv.get('globalvar_traffic')
    web_diary_text_db = output_db()
    note = len(list(kv.getkeys_by_prefix('key')))
    return template('diary_diary',diary_text=web_diary_text_db,traffic=traffic,note = note)

    

@app.route('/',method='POST')
def do_diary_w():
    web_diary_text = request.forms.get('diary_text')
    tags = request.forms.get('tags').replace(',',' ').replace('，',' ').split()
    tags = [tag.lower() for tag in tags]
    input_db(web_diary_text,tags)
    web_diary_text_db = output_db()
    traffic = kv.get('globalvar_traffic')
    note = len(list(kv.getkeys_by_prefix('key')))
    return template('diary_diary',diary_text=web_diary_text_db,traffic=traffic,note = note)
    
@app.route('/tags/<tag>')
def do_tag(tag):
    mydiary = get_tag_data(tag)
    if mydiary:
        return template('tag', diary=mydiary,tag=tag)
    else:
        return "Tag not found<br><a href='/'>返回<a>"
        
application = sae.create_wsgi_app(app)



