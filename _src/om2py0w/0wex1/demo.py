# _*_ coding: utf-8 _*_
# magic comment



print u"2015年10月25日"
a = u'a 2015年10月25日'
b = 'b 二〇一五年十月二十五日'

print a
a_utf_8 = a.encode('GBK')
b_gbk = b.encode('GBK')
print a_utf_8
print b_gbk