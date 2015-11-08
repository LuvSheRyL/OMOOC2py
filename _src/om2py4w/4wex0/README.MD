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


----------
### 参考

> [wiki/HTML](https://en.wikipedia.org/wiki/HTML)
> [Web service](https://en.wikipedia.org/wiki/Web_service?cm_mc_uid=28826105043914467360895&cm_mc_sid_50200000=1446736089)
> [REST Wiki](https://en.wikipedia.org/wiki/Representational_state_transfer)
> [REST中文简介](http://www.cnblogs.com/shanyou/archive/2012/05/12/2496959.html)
> [REST案例框架实现](http://blog.csdn.net/maoxiang/article/details/4551434)
> [官方Python WSGI核心](https://www.python.org/dev/peps/pep-0333/)
>[Python你必须知道的十个库](http://www.open-open.com/news/view/ba474d)
>[12 个最好的 Python 框架用于快速开发](http://www.open-open.com/news/view/774e1f)
>[10个用于Web开发的最好 Python 框架](http://www.open-open.com/news/view/f2eefa)
>[Bottle](http://bottlepy.org/docs/dev/)
>[Bottle Tutorial: Todo-List Application](http://bottlepy.org/docs/dev/tutorial_app.html#using-bottle-for-a-web-based-todo-list)


<html>
<body>
<hr>
<form action="diary" method="get">
        <center>
        My diary: <input type="text" name="diary_text" />
        <input type="submit" value="Updata" />
        <br>
        <textarea rows="3" cols="50" readonly>
日记
        </textarea>
        <center>
</form>
</body>
</html>






----------


