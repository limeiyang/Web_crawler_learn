
# 【1】===导入包
import requests;
from bs4 import BeautifulSoup;
import os
biqukan_url = "https://www.biqukan.com/%s/";


# 【8】===请求小数的目录
def Get_xiaoshuo_mulu(xiaoshuo_url,xiaoshuo_name,header):
    # 1.开始请求网络数据
    requests_01 = requests.get(url=xiaoshuo_url,data=header);
    # 2.判断是否请求成功
    print("请求码：",requests_01.status_code);
    if requests_01.status_code == 200:
        # 3.设置编码
        print("当前网站的编码格式：",requests_01.encoding);
        requests_01.encoding = "gbk";
        # 4.获取网站内容  data = html.read();
        xiaoshuo_data = requests_01.text;
        # print(xiaoshuo_data)
        # 5.保存到本地- 分文件夹
        file_path = "C:\/Users\/Administrator\/Desktop\/WHGC2019年2月25日\/08_Requests_笔趣看小说下载助手\/笔趣看小说下载\/%s\/"%xiaoshuo_name;
        # 判断路径是否存在
        if not os.path.exists(file_path):
            print("文件不存在，进行创建")
            os.makedirs(file_path);
            pass
        file = open(file_path+"%s.html"%xiaoshuo_name,"w",1);
        file.write(xiaoshuo_data);
        file.close();



        pass
    else:
        print("网络访问失败，请求码：%d，请检查网址是否正确"%requests_01.status_code);
        pass

    pass

# 【2】===调用Python文件执行入口
if __name__ == "__main__":
    print("程序开机中...")
    # 【3】软件介绍和说明
    print("==========欢迎使用Python小说爬虫V1.0版==========");
    print("==========本程序数据源来至：https://www.biqukan.com");
    print("==========使用说明==========");
    # 【4】获取小说地址
    xiaoshuo_code = input("==========请输入小说编号(格式：38_38964)==========\n").replace(" ","");
    xiaoshuo_url = biqukan_url%xiaoshuo_code;
    print("小说下载地址为：",xiaoshuo_url);
    # 【5】小说名称
    xiaoshuo_name = input("==========请输入小说名称==========\n").replace(" ","");
    print("小说名称为：",xiaoshuo_name);
    # 【6】模拟硬件设备访问-创建用户代理
    """
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36
    """
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"};
    # 【7】请求网络
    # 去除字符串中的空格
    Get_xiaoshuo_mulu(xiaoshuo_url,xiaoshuo_name,header);

    pass
