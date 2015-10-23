
### [Win安装ipython&Notebook配置](http://jingyan.baidu.com/article/8cdccae9698758315413cdfe.html)
+ 下载ez_setup.py 到某一个目录(如:C:\Python27\get-pip.py),  [下载地址](http://www.pip-installer.org/en/latest/installing.html#install-or-upgrade-setuptools  )
+ 运行`C:\Python27>python.exe get-pip.py`
+ 升级到最新版本命令`python -m pip install -U pip`
+ 安装完成反馈如下信息
	`
		Installing collected packages: pip, wheel

		Found existing installation: pip 7.0.1
		Uninstalling pip-7.0.1:
    	Successfully uninstalled pip-7.0.1
		Successfully installed pip-7.1.2 wheel-0.26.0
	
+ 在系统环境变量中添加`C:\Python27;C:\Python27\Scripts`，重启
 + 下载pyreadline包，并且双击后安装就可以了！[下载链接](https://pypi.python.org/pypi/pyreadline/2.1)
 + 下载 [ipython ](http://archive.ipython.org/release/)，实测4.0目前兼容性不太稳定，建议选择3.X版本
 + 下载完成以后，解压到c盘根目录，即可
 + 然后在cmd中安装ipython即可，命令为：`python setupegg.py install`
 + 设置ipython的环境变量，ipython的可执行文件在`C:\Python27\Scripts`中
 + 搞定![](http://i13.tietuku.com/04c2aeec1e029dd1.jpg)
+ **安装Notebook方法1** 
	+ 尝试Notebook [ipython4.0以上需要安装这个notebook](https://github.com/jupyter/notebook), 
	+ Notebook安装好之后，还需要下载一些其它咚咚
    0. [distribute 安装](https://pypi.python.org/pypi/distribute/0.7.3)
	1. [下载安装 pyzmq](https://github.com/zeromq/pyzmq),解压缩后在当前目录运行python setupegg.py install 即可安装
     	c:>easy_install.exe pyzmq
	2. [下载安装 jinja2](https://github.com/mitsuhiko/jinja2),      c:>easy_install.exe jinja2
    3. [下载安装 tornado](http://www.tornadoweb.org/en/stable/)
      c:>easy_install.exe tornado 
    4. 添加数学公式MathJax
    	`from IPython.external.mathjax import install_mathjax`
		`install_mathjax()`



+ **安装Notebook方法2**：`pip install notebook`安装
   
 好了，使用下面命令就可以把Notebook起来：
      c:>ipython notebook

```
## 运行界面

![](http://i13.tietuku.com/44c8781012397f30.jpg)