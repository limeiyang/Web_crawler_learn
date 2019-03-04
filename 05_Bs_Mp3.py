
# 【1】===导入包
import urllib.request;
from bs4 import BeautifulSoup;
import os
# 【2】===创建目标网址
url = "https://www.i4.cn/ring_22_0_1.html";
# 做读取本地数据
file_path = "C:\/Users\/Administrator\/Desktop\/WHGC2019年2月25日\/07_Beautiful_爱思助手MP3\/Case01\/03_爱思助手_mp3.html"
data = "";
# 检查文件是否存在
if os.path.exists(file_path):
    # 1.读取本地数据
    html = open(file_path,"rb",1);
    data = html.read();
    print("本地文件存在。。。")
    html.close();
    pass
else:
    print("文件不存在-进行网络访问，并本地存储")
    # 【3】===网络访问---是否访问成功
    html = urllib.request.urlopen(url);
    if html.getcode() == 200:
        # 【4】===读取数据
        data = html.read();
        # 【5】===保存到本地
        file = open("03_爱思助手_mp3.html", "wb", 1);
        file.write(data)
        file.close();
        print("数据访问成功，并存储同级目录")
        pass
    else:
        print("访问失败。。。。");
        pass
    html.close();

    pass

# ============解析数据===============
def Get_mp3_data(data):
    # 1.生成soup对象
    soup = BeautifulSoup(data,"html.parser");
    # 2.获取所有音乐的div标签内容
    divs_mp3 = soup.find_all("div",attrs={"class":"list ring_list"});
    print("音乐数目：",len(divs_mp3))
    # 3.遍历出所有的音乐div
    i = 1;
    for div_mp3_item in divs_mp3:
        print("第%d条音乐：%s"%(i,"********************************"));
        # 1.获取音乐名称：
        mp3_title = div_mp3_item.find("div",attrs={"class":"title"}).string;
        print("第%d首音乐名称：%s"%(i,mp3_title));
        # 2.获取下载量：
        mp3_downcount = div_mp3_item.find("div",attrs={"class":"downcount"}).string;
        print("第%d首音乐下载量：%s"%(i,mp3_downcount));
        # 3.时间
        mp3_longtime = div_mp3_item.find("div",attrs={"class":"longtime"}).string;
        print("第%d首音乐时长：%s"%(i,mp3_longtime));
        # 3.下载地址
        mp3_url = div_mp3_item.find("div",attrs={"class":"btn audio_play"})["data-mp3"];
        print("第%d首地址：%s"%(i,mp3_url));
        # 存储到本地：
        print("--"*50);
        str_01 = "%s\n第%d首:[名称]:%s   [下载量]:%s   [时长]:%s   [下载地址]:%s\n"%("--"*100,i,mp3_title,mp3_downcount,mp3_longtime,mp3_url);
        file_mp3_mulu = open("爱思助手mp3目录4.txt","a",1,encoding="utf-8");
        file_mp3_mulu.write(str_01);
        # 下载：
        urllib.request.urlretrieve(mp3_url,"mp4/%s.mp3"%mp3_title);
        print("第%d首音乐下载完成。。"%i)



        i+=1;
        pass




    pass
# 函数调用
Get_mp3_data(data);