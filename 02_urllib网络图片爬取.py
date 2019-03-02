
# 【1】===导包===
import urllib.request;
# 导入正则表达式的包
import re
# 【2】===设置目标网址===
url = "https://www.i4.cn/wper_23_0_0_1.html";
# 【3】===检查网络访问状态===
html = urllib.request.urlopen(url);

if html.getcode()==200:
    print("网络访问成功：%d"%html.getcode())
    data = html.read();
    # 【4】===存储到本地===
    file = open("02_urllib爱思助手.html","wb",1);
    file.write(data);
    file.close();

    pass
else:
    print("网络访问失败。。。")
    pass
html.close();
# ================解析网络图片下载============================
# 【5】===创建获取图片的函数===
def Get_data_img(data):
    # 创建一个正则表达式
    r = r'https://d-paper.i4.cn/middle/[^\s]*[.jpg|.JPG]';
    # 创建一个正则表达式的模板
    pat = re.compile(r)
    # 根据正则表达式模板，进行匹配数据
    imgurls = re.findall(pat,str(data));
    # 输出返回数据
    print(imgurls)
    print(len(imgurls))
    # 通过遍历循环下载
    i = 1;
    for urlimg in imgurls:
        print("第%d张图片地址：%s"%(i,urlimg));
        print("开始下载第%d张。。。"%i);
        urllib.request.urlretrieve(urlimg,"爱思助手手机壁纸/图片_%d.jpg"%i);
        print("下载成功\n======================")
        i+=1;
        pass

    pass

# 【6】===函数的调用===
Get_data_img(data);












