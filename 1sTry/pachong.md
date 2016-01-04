# 

[使用 Python 进行线程编程](http://www.ibm.com/developerworks/cn/aix/library/au-threadingpython/)

DEMO1

    import urllib2
    import time

    hosts = ["http://map.baidu.com", "http://sina.com", "http://taobao.com","http://qq.com"]

    start = time.time()
    #grabs urls of hosts and prints first 1024 bytes of page
    for host in hosts:
      url = urllib2.urlopen(host)
      print url.read(1024)

    print u"Elapsed Time: %s" % (time.time() - start)

[Beautiful Soup 4.2.0 文档](http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)