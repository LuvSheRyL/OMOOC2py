#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ref：https://github.com/sunoonlee/OMOOC2py/tree/master/_src/om2py4w/4wex0
import requests
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

def main():
    print '''
    My diary
    --r/read 历史
    --q/quit 退出
    '''.decode('utf-8').encode('gbk') #utf-8-->gbk 输出

    while True:
        INPUT_gbk = raw_input('输入： '.decode('utf-8').encode('gbk')).strip()
        INPUT = INPUT_gbk.decode('gbk').encode('utf-8')
        inp = INPUT.lower()
        if inp in ['quit','q']:
            break
        elif inp in ['r','read']:
            print listnotes()
        else:
            addnote(INPUT)

def addnote(note):
    requests.post('http://localhost:8080/write', data = {'diary_text':note})

def listnotes():
    r = requests.get('http://localhost:8080/read')
    #text_gbk = r.text
    soup = BeautifulSoup(r.text,'html.parser') #使用pyhton内置parser库解析
    lis = soup.find_all('textarea')
    notes = ''
    for i in lis:
        notes += i.get_text()+'\n'
    return notes

if __name__ == '__main__':
    main()