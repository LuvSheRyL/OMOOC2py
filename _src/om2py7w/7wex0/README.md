# Qpython 手机移动端日记本


 在之前开发基础上, 完成 极简交互式笔记的 移动应用 版本
 需求如下:
+ 推荐基于 QPython 快速构建:
+ 在手机端每次接收一行的文本(不包含表情/图片/声音/视频...)
+ 使用专用指令,可打印出过往所有笔记
+ 在服务端合理存储/管理
+ 同时兼容:
+ 命令行工具
+ 微信公众号
+ 可以通过本地命令行工具监察/管理 移动应用 运行:
+ 获得当前笔记数量/访问数量等等基础数据
+ 可以获得所有笔记备份的归档下载

补充：

+ 备选的:
+ 如果有余力!-)
+ 请尝试:
+ 如何编译为标准 .apk 进行发布?
+ 如何建立认证功能,防止有人误入?
+ 如果识别weibo用户呢?
+ 即,这是一个私人笔记系统,不接受其它人使用
+ 当然,想作成多人也是相同的技术.
+ 如何建立数据加密?防止有人通过分析网络协议伪造数据提交?


*****

## 环境搭建：

1.  [Qpython](http://qpython.org/) or [http://qpython.com/](http://qpython.com/),[Qpython Wiki](http://wiki.qpython.org/)
 + [国内下载链接](http://openbox.mobilem.360.cn/appfun/detail?id=84676)
 + QEditor's keyboard shortcuts

		Run script F5

		Find text CTRL+F

		Save file CTRL+S

		Open file CTRL+O

		Undo CTRL+Z

		Go to line CTRL+Z

		Left indent CTRL+[

		Right indent CTRL+]

		Run file CTRL+R
 + [Window系统下 使用Virtual box 安装 Android x86 并实现竖屏](https://lzw.me/a/window-virtual-box-android-x86-resolution.html) 
 + [Android-x86虚拟机安装配置全攻略](http://www.oschina.net/question/565065_92851)
 + [虚拟机virtualbox下载](https://www.virtualbox.org/wiki/Downloads)
 + [android-x86 各下载地址（需科学上网）](http://www.android-x86.org/download)
 + [android-x86-5.1-rc1.iso 下载地址镜像](http://nchc.dl.sourceforge.net/project/android-x86/Release%205.1/android-x86-5.1-rc1.iso)
 + ![](http://i12.tietuku.com/1da3c1c0ba8dd917.jpg)
 
 + android-x86常用的快捷键有：

		Alt-F1 = 进入 console 模式
		Alt-F7 = 回到 GUI 模式
		Alt-F9 = 图形界面
		Alt-F10 = 画面旋转 180 度
		Alt-F10 = 画面旋转 180 度
		Alt-F11 = 画面向左旋转 90 度
		Alt-F12 = 画面向右旋转 90 度
		Ctrl-P = 开启Android设定画面
		"Windows 键"相当于 Android 的 Home 按钮。
		"Esc" 相当于 Android 的 Back 按钮
		F2 相当于 Android 的 Menu 按钮
		F3 相当于 Android 的 Search 按钮
		右边的菜单键（win和ctrl中间的键） = Android菜单键

2.  Fabric
	1. 下载`pip install fabric`
		+ Win用户会报错，
		`error: Microsoft Visual C++ 9.0 is required (Unable to find vcvarsall.bat). Get it from http://aka.ms/vcpython27`
		+ 解决办法：[下载最新VC9.0补丁](https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi)
	2. 验证 ` pip show fabric`
	
	3. [Fabric官方教程](http://docs.fabfile.org/en/1.10/)
	4. [参考博客](http://blog.csdn.net/wklken/article/details/8719541)

3.  [安卓模拟器genymotion](http://www.genymotion.net/)