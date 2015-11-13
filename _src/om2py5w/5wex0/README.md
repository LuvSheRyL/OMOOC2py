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

 + [KVDB](http://www.sinacloud.com/doc/sae/python/kvdb.html)
 + 