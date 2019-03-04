
# 当使用Beautiful soup的时候，一定要保证第三方文件已经导入成功
# 1.导入包-网络访问，数据解析
import urllib.request;
from bs4 import BeautifulSoup;
# 2.测试网站
url = "https://www.i4.cn/ring_1_0_1.html";
# 3.验证用户包
import ssl;
# 用户验证的变量 - 其中一种写法-Linux或Mac上使用
# ssl._create_default_https_context = ssl._create_unverified_context;
# 4.访问网络--验收是否成功
html = urllib.request.urlopen(url);
if html.getcode() == 200:
    # 5.读取访问到的数据
    data = html.read();
    # 6.数据存储到本地
    file = open("01_爱思助手_音乐.html","wb",1);
    file.write(data);
    file.close();
    print("爱思助手-数据加载成功")
    pass
else:
    print("网络加载失败，返回码:",html.getcode());
    pass
# 7.关闭网络访问数据
html.close();

print("===========解析数据==================");
# 获取一个soup对象；---负责解析当前的网站内容
# soup = BeautifulSoup(open("01_爱思助手_音乐.html"))
# 第一个参数：网站数据，第二个参数：解析器的选择
soup = BeautifulSoup(data,"html.parser");
# 1.通过标签获取网站内容
title = soup.title;
print("获取到标签内容：",title)
# 2.获取标签中文本内容
print(title.string);
# 3.获取该数据的标签名称
print("标签名称为：",title.name);
# 4.查询父容器的名称
name_01 = title.parent.name;
print("父容器内容：",name_01)
# 5.目标获取link中包含的网址
# 只会查询到第一对应标签
link = soup.link;
print("link标签：",link)
# 6获取href对应的网址
print(link["href"]);
# 7查询出所有的link标签内容
links = soup.find_all("link");
print(links);
print(len(links))
# 遍历所有的数据：
for lins_01 in links:
    print("==================")
    print(lins_01);
    # 对应的网址；
    print(lins_01["href"])
    pass
# 8.通过条件查询 - 只能查询的第一个
# <div class="list" data-value="3">教程</div>
div_01 = soup.find_all("div",attrs={"class":"options"});
print(div_01);
print(div_01[0]);
# 获取5个div标签
divs = div_01[0].find_all("div",attrs={"class":"list"});
print(divs)
print(len(divs))
# 通过for循环遍历
for div_item in divs:
    print(div_item.string);
    pass













