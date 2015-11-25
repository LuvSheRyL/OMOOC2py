#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ref：https://github.com/sunoonlee/OMOOC2py/tree/master/_src/om2py4w/4wex0
import requests
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

# 帮助信息
HELP = '''\
输入 ?/h/H 打印帮助信息
输入 q/quit/exit 退出日记本
输入 r/read 读取日记内容
输入 tag:<tag> 设置tag信息
输入 DELETE 删除日记信息
'''.decode('utf-8')

def main():
    print HELP
    tag = ''
    while True:
        print "\n"
        print 'tag:', tag
        INPUT_gbk = raw_input('输入： '.decode('utf-8').encode('gbk')).strip()
        INPUT = INPUT_gbk.decode('gbk').encode('utf-8')
        data = INPUT

        if data.startswith('tag:'):
            tag = data[4:]
            print "Tag change to: ", tag
        elif data in ['h', 'H', '?']:
            print HELP
        elif data in ['q', 'quit', 'exit']:
            print u"bye, 亲~"
            break
        elif data in ['r', 'read']:
            read_tag(tag)
        elif data == 'DELETE':
            print "you should really think about it!"
            print "Do you really want to delete all data?(y/n)"
            delete = raw_input(">")
            if delete.lower() == 'y':
                delete_diary()
            else:
                print "Glad you didn't choose to delete"
                continue
        else:
            addnote(data,tag)

def addnote(note,tags=''):
    requests.post('http://localhost:8080/', data={'content': note,'tags':tags})
    
def read_diary():
    r = requests.get('http://localhost:8080/')
    soup = BeautifulSoup(r.text,'html.parser')
    for item in soup.find_all('p',class_='content'):
        print item.get_text()
        
def read_tag(tag):
    if tag:
        r = requests.get('http://localhost:8080/tags/{}'.format(tag))
        soup = BeautifulSoup(r.text,'html.parser')
        for item in soup.find_all('p',class_='content'):
            print item.get_text()
    else:
        read_diary()


def delete_diary():
    r = requests.delete('http://localhost:8080/')
    print "all data deleted"


if __name__ == '__main__':
    main()