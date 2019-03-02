
# 【1】===urllib库的使用===
import urllib.request;
# python2.x
# import urllib,urllib2;
# 【2】===设定访问的目标网址====
url = "https://www.i4.cn/wper_1_0_0_1.html";
# 【3】====开始网络链接====
html = urllib.request.urlopen(url);
# 【4】===读取访问网络返回的数据====
data = html.read();
# print(data);
# 【5】===存储到本地====
file = open("01_urllib爱思助手.html","wb",1);
# 【6】===写入数据===
file.write(data);
# 【7】===关闭文件和网络===
file.close();
html.close();

# ======================urllib常规用法===================================
# 获取访问网络的网址
print("当前访问网络的网址：%s"%html.geturl());
# 获取网络状态的返回码
print("访问网络的状态码：%d"%html.getcode());
# 中文乱码问题
url01 = "http://tieba.baidu.com/f?ie=utf-8&kw=武汉工程大学red_tag=v1087355643";
# 网址的加密
url02 = urllib.request.quote(url01);
print("加密后的乱码网址：%s"%url02);
# 修正中文网址乱码问题
url03 = urllib.request.unquote(url02);
print("生成的网址：%s"%url03)
