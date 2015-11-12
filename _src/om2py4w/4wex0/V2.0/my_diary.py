# coding=utf-8
# author: Alan Lai
# email: techwplai@gmail.com
# version: 1.0
import os
import time


def append_text(text):
    f = open('mydiary.txt', 'a')
    message = '{}:\n{}\n'.format(time.strftime("%YY%mM%dD %H:%M:%S"), text)
    f.write(message)
    f.close()


def get_text():
    if not os.path.exists('mydiary.txt'):
        append_text('')
    else:
        f = open('mydiary.txt')
        text = f.read()
        f.close()
        return text

if __name__ == '__main__':
    while True:
        text_input = raw_input('Ð´µãÊ²Ã´:\n> ')
        if text_input.lower() in ['quit', 'q', 'exit']:
            break
        append_text(text_input)
        print "you diary:\n", get_text()