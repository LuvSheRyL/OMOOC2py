## 公网版日记本

需求

+ 在上周开发基础上, 完成 极简交互式笔记的 PaaS 版本
+ 需求如下:
+ 将上周应用网站发布为公网稳定服务
+ 可以通过固定域名访问系统:
+ 每次运行时合理的打印出过往的所有笔记
+ 一次接收输入一行笔记
+ 在服务端保存为文件
+ 同时兼容 3w 的 Net 版本的命令行界面进行交互
+ 可以通过本地命令行工具监察/管理网站:
+ 获得当前笔记数量/访问数量等等基础数据
+ 可以获得所有笔记备份的归档下载

需求拆解：

+ 环境搭建
 
 + [PAAS](https://en.wikipedia.org/wiki/Platform_as_a_service),新浪SAE
     + [本地环境搭建](http://www.sinacloud.com/doc/sae/python/tools.html)
            1. pip安装`$ pip install sae-python-dev`
            2. 或者git clone 安装
            
            `$ git clone https://github.com/sinacloud/sae-python-dev-guide.git`

            `$ cd sae-python-dev-guide/dev_server`

            `$ python setup.py instal`
     
      + 在项目目录saeapp\1\下新建两个文件
        ，（\1\表示版本文件夹）
          +  config.yaml 用于配置个人信息
          
                `name: mydiary` 
                `version: 1`

                *注意name:后面需要空格。。否则dev_server.py执行报错。*




          + index.wsgi
          
          + 官方代码：
          
                from bottle import Bottle, run

                import sae

                app = Bottle()

                @app.route('/')
                def hello():
                    return "Hello, world! - Bottle"

                application = sae.create_wsgi_app(app)

      + 切换至项目目录下，运行`dev_server.py` ，
效果如下：
![](http://i5.tietuku.com/fe6a92fac4711ed4.jpg)


 + [KVDB](http://www.sinacloud.com/doc/sae/python/tools.html?ticket=7c904af8cec89f3130a2b2a819f234692b75759c#kvdb)

    + KVDB默认数据存在内存中，dev_server.py进程结束时，数据会全部丢失，如果需要保存数据， 请使用如下命令行启动dev_server.py。
    + `dev_server.py --kvdb-file=/path/to/kvdb/local/file`
    + `$ dev_server.py --kvdb-file=kvdb.db`


+ [远程代码部署](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html#git)
     
     目前SAE上的应用支持通过SVN和Git来部署代码。
     Git仓库地址	https://git.sinacloud.com/YOUR_APP_NAME
     SVN仓库地址	https://svn.sinacloud.com/YOUR_APP_NAME

     用户名 SAE安全邮箱

     密码 SAE安全密码

> 注解
> 
> 用户名和密码为安全邮箱和安全密码，不是微博账号和微博密码！如已启用微盾动态密码，则密码应该是“安全密码”+“微盾动态密码”

    git init

    vim .git/config

        修改远程仓库地址：url =   https://git.sinacloud.com/YOUR_APP_NAME
    git add --all
    git commit -m "V1.0"
    git push sae master:1 （创建分支，并部署。）
