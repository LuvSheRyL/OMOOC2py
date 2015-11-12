# WEB端记事本

### 功能
+ 在上周开发基础上, 完成 极简交互式笔记的Web版本
+ 通过网页访问系统:
+ 每次运行时合理的打印出过往的所有笔记
+ 一次接收输入一行笔记
+ 在服务端保存为文件
+ 同时兼容 3w 的 Net 版本的命令行界面进行交

### 要求
+ Web 应用架构理解
+ RESTful 风格理解
+ Bottle 框架使用
+ (Jinja2 模板使用)
+ MyDailyWeb 私人记事本内网页面版


----------

### MVP（Minimum viable product）最小可执行产品

+ 专注
+ 极致
+ 不断的迭代更新和改进
+ 体验做到完美



### 用于CLI的html解析

官方Beautifulsoup4 库：[https://pypi.python.org/pypi/beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4)

[BeautifulSoup/bs4中文文档](http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)


下载后，安装 `pip install beautifulsoup4-4.4.1-py2-none-any.whl`

安装Requests `$ pip install requests`

----------

### V1.0 WEB/CLI （txt格式保存）
 + utf8中文支持
 + 

效果图：

![](http://i12.tietuku.com/3feeeec558a14dec.jpg)

客户端代码是参考：[sunoonlee](https://github.com/sunoonlee/OMOOC2py/tree/master/_src/om2py4w/4wex0)

在他的基础上修正了
 
 + 客户端中文输出，网页读取历史，服务器崩溃问题
   + 原因是gbk,utf-8 转换问题所致
 
 + 灵活运用`.decode('utf-8').encode('gbk') `#utf-8-->gbk 输出 可解决

`INPUT_gbk = raw_input('输入： '.decode('utf-8').encode('gbk')).strip()`
`INPUT = INPUT_gbk.decode('gbk').encode('utf-8')`

----------

### V2.0 数据库的应用
根据教程提示，这里考虑sqlite关系型数据库

安装地址：[http://www.sqlite.org/download.html](http://www.sqlite.org/download.html)

1. 建里数据库CMD环境下：`C:\Users\robo_one\OMOOC2py\_src\om2py4w\4wex0>sqlite3 mydiary.db`
2. 在sqlite>后输入`sqlite> sqlite3 mydiary.db;` 注意分号--表示sqlite的确认
3. 创建数据表

![](http://i12.tietuku.com/7d5402b627cc6661.jpg)

    sqlite> .tables
    sqlite> CREATE TABLE mydiary(
       ...> Id integer PRIMARY KEY,
      ...> TIME text NOT NULL,
     ...> DATA text DEFAULT 'MYDIARY');
    sqlite> .tables
    mydiary
    sqlite>




----------

### 快速开发Web 美化（未完成）

**一切必须用背景图片才能实现的视觉效果都是耍流氓**

[Bootstrap ](http://getbootstrap.com/getting-started/)

[Bootstrap中文](http://v3.bootcss.com/)

安装`$ npm install bootstrap` 或者[点击下载v3.3.5](https://codeload.github.com/twbs/bootstrap/zip/v3.3.5)



----------
### 参考文档

> [wiki/HTML](https://en.wikipedia.org/wiki/HTML)
> 
> [Web service](https://en.wikipedia.org/wiki/Web_service?cm_mc_uid=28826105043914467360895&cm_mc_sid_50200000=1446736089)
> 
> [REST Wiki](https://en.wikipedia.org/wiki/Representational_state_transfer)
> 
> [REST中文简介](http://www.cnblogs.com/shanyou/archive/2012/05/12/2496959.html)
> 
> [REST案例框架实现](http://blog.csdn.net/maoxiang/article/details/4551434)
> 
> [官方Python WSGI核心](https://www.python.org/dev/peps/pep-0333/)
> 
> [Python你必须知道的十个库](http://www.open-open.com/news/view/ba474d)
>
>[12 个最好的 Python 框架用于快速开发](http://www.open-open.com/news/view/774e1f)
>
> [10个用于Web开发的最好 Python 框架](http://www.open-open.com/news/view/f2eefa)
>
> [Bottle官方文档](http://bottlepy.org/docs/dev/)
>
> [Bottle 教程: Todo-List Application](http://bottlepy.org/docs/dev/tutorial_app.html#using-bottle-for-a-web-based-todo-list)
> 
> [Grunt打造前端自动化工作流](http://tgideas.qq.com/webplat/info/news_version3/804/808/811/m579/201307/216460.shtml)
>> [Gruntjs官方](http://www.gruntjs.net/getting-started)
> 
>[大妈Simple-TODO Bottle 实现版](https://bitbucket.org/ZoomQuiet/bottle-simple-todo/wiki/Home) 
>
> [cURL for Win CMD](http://www.2cto.com/os/201205/131164.html)
> 
> [curl常用命令](http://www.cnblogs.com/gbyukg/p/3326825.html)

>[Html-meta应用](http://www.cnblogs.com/eastsuntdh/articles/561021.html)

>[车百科网开发手记、代码](http://blog.quickbest.net/a/242)
>
>[《零基础学python》（第二版）](https://github.com/qiwsir/StarterLearningPython)