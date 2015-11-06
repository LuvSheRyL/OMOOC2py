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


