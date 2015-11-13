# -*- coding: utf-8 -*-

import sqlite3
import time,datetime
import os
#global var
#数据库文件绝句路径
DB_FILE_PATH = "mydiary.db"
#表名称
TABLE_NAME = 'mydiary'
#是否打印sql
SHOW_SQL = True

def get_conn(path):
    '''获取到数据库的连接对象，参数为数据库文件的绝对路径
    如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
    路径下的数据库文件的连接对象；否则，返回内存中的数据接
    连接对象'''
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        print(u'硬盘上面:[{}]'.format(path))
        return conn
    else:
        print(u'创建mydiary.db')
        return conn
        
def get_cursor(conn):
    '''该方法是获取数据库的游标对象，参数为数据库的连接对象
    如果数据库的连接对象不为None，则返回数据库连接对象所创
    建的游标对象；否则返回一个游标对象，该对象是内存中数据
    库连接对象所创建的游标对象'''
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()


###############################################################
####            创建|删除表操作     START
###############################################################
def drop_table(conn, table):
    '''如果表存在,则删除表，如果表中存在数据的时候，使用该
    方法的时候要慎用！'''
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        if SHOW_SQL:
            print(u'执行sql:[{}]'.format(sql))
        cu = get_cursor(conn)
        cu.execute(sql)
        conn.commit()
        print(u'删除数据库表[{}]成功!'.format(table))
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def create_table(conn, sql):
    '''创建数据库表：student'''
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print(u'执行sql:[{}]'.format(sql))
        cu.execute(sql)
        conn.commit()
        print(u'创建数据库表[mydiary]成功!')
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

###############################################################
####            创建|删除表操作     END
###############################################################

def close_all(conn, cu):
    '''关闭数据库游标对象和数据库连接对象'''
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()


###############################################################
####            数据库操作CRUD     START
###############################################################

def save(conn, sql, data):
    '''插入数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print(u'执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql,d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def fetchall(conn, sql):
    '''查询所有数据'''
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        allnotes = []
        if SHOW_SQL:
            print(u'执行sql:[{}]'.format(sql))
        cu.execute(sql)
        r = cu.fetchall()
        for i in r: 
            allnotes.append('%s  %s' % (r['TIME'], r['DATA']))
        return allnotes
    else:
        print('the [{}] is empty or equal None!'.format(sql)) 
        return ['None DATA On Server']

def fetchone(conn, sql, data):
    '''查询一条数据'''
    if sql is not None and sql != '':
        if data is not None:
            #Do this instead
            d = (data,) 
            cu = get_cursor(conn)
            if SHOW_SQL:
                print(u'执行sql:[{}],参数:[{}]'.format(sql, data))
            cu.execute(sql, d)
            r = cu.fetchall()
            if len(r) > 0:
                for e in range(len(r)):
                    print(r[e])
        else:
            print('the [{}] equal None!'.format(data))
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def update(conn, sql, data):
    '''更新数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print(u'执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print(u'the [{}] is empty or equal None!'.format(sql))

def delete(conn, sql, data):
    '''删除数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print(u'执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
###############################################################
####            数据库操作CRUD     END
###############################################################


###############################################################
####            数据库创建、写与读
###############################################################
def create_table_test():
    '''创建数据库表测试'''
    conn = get_conn(DB_FILE_PATH)
    print(u'创建数据库表测试...')
    create_table_sql = '''CREATE TABLE IF NOT EXISTS mydiary(
                          Id INTEGER PRIMARY KEY, 
                          TIME TEXT, 
                          DATA TEXT
                        )'''

    create_table(conn, create_table_sql)
    

def save_test(DATA_WEB):
    TIME = time.strftime("%YY%mM%dD%H:%M:%S")
    '''保存数据测试...'''
    data = (TIME,DATA_WEB)
    save_sql = '''INSERT INTO mydiary VALUES(?, ?),data'''
    conn = get_conn(DB_FILE_PATH)
    save(conn, save_sql, data)
    print(u'保存数据测试...')

def fetchall_test():
    '''查询所有数据...'''
    print(u'查询所有数据...')
    fetchall_sql = '''SELECT * FROM mydiary'''
    conn = get_conn(DB_FILE_PATH)
    fetchall(conn, fetchall_sql)

def main():
    create_table_test()
    save_test("123")
    fetchall_test()

if __name__ == '__main__':
    main()