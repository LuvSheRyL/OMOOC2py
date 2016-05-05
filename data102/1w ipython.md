> 2016-5-5 15:38:40




## 一、Linux操作

[国内镜像源链接汇总](http://www.centoscn.com/yunwei/news/2016/0417/7070.html)

 一、站点版
 （一）、企业站
- 1.搜狐：http://mirrors.sohu.com/
- 2.网易：http://mirrors.163.com/
- 3.阿里云：http://mirrors.aliyun.com/
- 4.腾讯：http://android-mirror.bugly.qq.com:8080/（仅针对APP开发的软件，限流，不推荐）

 （二）、教育站
- 1.上海交通大学：http://ftp.sjtu.edu.cn/html/resources.xml（部分移动运营商出口状况不佳，无法访问）
- 2.华中科技大学：http://mirror.hust.edu.cn/（当前已用容量估计：4.83T）
- 3.清华大学：http://mirrors.tuna.tsinghua.edu.cn/（当前已用容量估计：9.8T）

思考
- 1. 如何查看文件的前100行和最后100行？
- 1. 如何查看文件的第3列？
- 1. 如何统计文件的前100行有多少个单词？

## 二、Python数据工具箱

从底层工具箱开始练手

定位问题
搜集数据：
 + 爬虫
 + 整理
pandas数据整理
数据探索；
数据建模；
 - Scikit-learn
数据展示
 - BOKEH

数据相关模块（线下自学）：
request：网页数据抓取
beautiful soup:解析网页数据
Flask：轻量级Web框架
Sqlite3:轻量级数据接口
Pytspark:spark的Python接口（海量数据）
nltk：自然语言处理
networkx:社会网络分析；
theano:深度学习

计算套件：Anaconda
>如果安装完后，相关包不是最新的？
>例如运行 `conda update numpy`

## 运行环境


ipython,Jupyer notebook


科学计算基础包：numpy
Scipy 丰富了numpy的扩展包；


## 数据可视化

+ Matplotlib
+ Seaborn简单

## 数据分析

+ 汇总统计：pandas


## 机器学习

Scikit-Learn:机器学习库

![scikit learn algorithm cheat sheetf
](http://scikit-learn.org/stable/_static/ml_map.png)

参考：http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

## 三、ipython入门

参考链接：
+ http://ipython.org/documentation.html
+ http://docs.scipy.org/doc/numpy/reference/



* * *

Python进行数据分析练习笔记

>第三章内容



    print "world"

    world
    


    import numpy as np


    ? np


    %quickref

>ipython的快速参考手册

% 是ipython 的魔法函数


    2+10




    12




    _+10




    22




    10+22;


    _




    22




    Out[20]




    22




    _15




    -10




    print("last output", _)

    ('last output', -10)
    


    %magic


    %timeit range(10)

    1000000 loops, best of 3: 354 ns per loop
    


    %%timeit
    range(10)
    range(100)

    The slowest run took 4.08 times longer than the fastest. This could mean that an intermediate result is being cached 
    1000000 loops, best of 3: 1.31 µs per loop
    


    for i in range(5):
        size = i*100
        print('size:',size,end='')
        %timeit range(size)


      File "<ipython-input-47-1ba539eb5013>", line 3
        print('size:',size,end='')
                              ^
    SyntaxError: invalid syntax
    



    %%file test.txt
    This is a test file

    Writing test.txt
    


    !cat test.txt

    This is a test file
    

## 练习：利用Python进行数据分析
    


    import numpy as np
    from numpy.random import randn


    import datetime


    def add_numbers(a,b):
        """
        Add two numbers together
        
        Returns
        
        ______
        
        the_sum ：type of arguments
        """
        return a + b


    add_numbers?


    add_numbers??

>字符配以通配符（*）即可显示所有与该通配符表达式相匹配的名称


    np.*load*?

    np.load
    np.loads
    np.loadtxt
    np.pkgload

## %run 命令

%run 命令可当做`python`命令执行。Python xxxxx.py 
所有文件都可以通过%run命令当做Python程序来执行。%run可以调用.py文件中函数，并执行，其对应的函数变量，将成为当前ipython shell命令环境中的变量。例如：


    def f(x,y,z):
        return (x + y)/z
    a = 5
    b = 6
    c = 7.5
    
    result = f(a, b, c)


    result




    1.4666666666666666



## 魔术命令

魔术命令是以%为前缀的命令。例如通过%timeit检测语句执行时间


    a = np.random.randn(100,100)


    %timeit np.dot(a,a)

##### 常见ipython魔术命令


    %quickref 显示ipython的快速参考
    %magic 显示所有魔术命令的详细文档
    %debug 从最新的异常的底部进入交互调试
    %hist 打印命令的输入历史
    %pdb 在异常发生后自动进入调试器
    %paste 执行剪贴板的Python代码
    %cpaste 打开特殊提示符以便手工粘贴待执行的Python代码
    %reset 删除interactive命令空间中的全部变量、名称
    %page OBJECT 通过分页器打印输入OBJECT
    %run scipt.py 在ipython中执行一个Python脚本文件
    %prun statement 通过cprofile执行statement，并打印分析器的输出结果
    %time statement 报告statement执行时间
    %timeit statement 多次执行statement以计算系统平均执行时间
    %xdel variable 删除变量，并尝试清楚其在ipython中的对象上的一切引用


## 记录输入输出日志

`%logstart`


    %logstart

    Activating auto-logging. Current session state plus future input saved.
    Filename       : ipython_log.py
    Mode           : rotate
    Output logging : False
    Raw input log  : False
    Timestamping   : False
    State          : active
    

## 与系统的命令交互

    !cmd  在系统shell中执行cmd
    output = !cmd args  执行cmd,并将stdout存放在output中
    %bookmark 使用ipython的目录书签系统
    %cd 目录   将系统工作目录更改为对应的目录路径
    %pwd  返回系统的当前工作目录
    %pushd 目录  将当前目录入栈，并转向该目录
    %dirs 返回一个含有当前目录栈的列表
    %dhist 打印目录访问历史
    %env 以dict形式返回系统环境变量
    

## 目录书签系统

`%bookmark db D:/开智/数据班资料/data202`


    %bookmark data202 D:/开智/数据班资料/data202


    cd data202

    (bookmark:data202) -> D:/开智/数据班资料/data202
    D:\开智\数据班资料\data202
    

## 逐行分析函数性能

+ %prun 宏观性能分析
+ %lprun (line_profiler)做微观性能分析；

魔法函数%lprun，可以对一个或者多个函数进行性能分析。例如：

    from numpy.random import randn

    def add_and_sum(x,y):
        added = x + y
        summed = added.sum(axis=1)
        return summed
    def call_function():
        x = randn(1000,1000)
        y = randn(1000,1000)
        return add_and_sum(x,y)
        
比如我想知道`add_and_sum`函数性能，`%prun`会给出如下结果：

``` 
 4 function calls in 0.096 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.076    0.076    0.089    0.089 <ipython-input-3-668833098812>:3(add_and_sum)
        1    0.013    0.013    0.013    0.013 {method 'sum' of 'numpy.ndarray' objects}
        1    0.007    0.007    0.096    0.096 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
```


    from numpy.random import randn
    
    def add_and_sum(x,y):
        added = x + y
        summed = added.sum(axis=1)
        return summed
    def call_function():
        x = randn(1000,1000)
        y = randn(1000,1000)
        return add_and_sum(x,y)


    x = randn(3000,3000)


    y = randn(3000,3000)


    %prun add_and_sum(x,y)






