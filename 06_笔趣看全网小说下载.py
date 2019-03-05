
# 【1】===导入包
import requests;
from bs4 import BeautifulSoup;
import os
import time;
biqukan_url = "https://www.biqukan.com/%s/";
# 【9】获取每一个章节内容
def Get_xiaoshuo_mulu_context(a_context_url,a_context,header):
    # 1.网络访问
    requests_02 = requests.get(a_context_url,data = header);
    # 2.判断网络
    if requests_02.status_code == 200:
        # 3.设置编码格式
        requests_02.encoding = "gbk"
        # 4.获取网站内容
        context_data =requests_02.text;
        # 5.解析数据
        soup_01 = BeautifulSoup(context_data,"html.parser");
        # 6.获取包含小说的div
        div_content = soup_01.find("div",attrs={"id":"content"});
        # 7.获取div中的文本信息
        content_text = div_content.get_text();
        # print(content_text);
        file = open("%s.txt"%a_context,"w",1,encoding="utf-8");
        file.write(str(content_text).replace("\xa0",""));
        file.close()
        pass
    else:
        print("网络异常，加载失败");
        pass




    pass


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
        # 6判断路径是否存在
        if not os.path.exists(file_path):
            print("文件不存在，进行创建");
            os.makedirs(file_path);
            pass
        file = open(file_path+"%s.html"%xiaoshuo_name,"w",1,encoding="gbk");
        file.write(xiaoshuo_data);
        file.close();
        # 7.数据解析处理
        soup =BeautifulSoup(xiaoshuo_data,"html.parser");
        div_listmain = soup.find("div",attrs={"class":"listmain"});
        # print(div_listmain)
        # 8.获取dl标签内容
        dl_01 = div_listmain.dl;
        # print(dl_01);
        # 9.创建一个变量用于记录下载状态
        start_dowm = False;
        # 10.遍历整个dl中内容
        i = 1;

        for tab_dd in dl_01:
            # print("第%d行：%s" % (i, tab_dd));

            if tab_dd == "\n":
                # 不做任何操作
                pass
            elif tab_dd.string == "《%s》正文卷"%xiaoshuo_name:
                start_dowm = True;
                pass
            elif start_dowm:
                print("=======================")
                print("第%d行：%s" % (i, tab_dd));
                # 获取章节的名称：
                a_context = tab_dd.a.string;
                print(a_context);
                # https://www.biqukan.com/38_38964/14621793.html
                a_context_url ="https://www.biqukan.com"+ tab_dd.a["href"];
                print(a_context_url)
                # 11.调用函数获取每一个章节的内容:单位是秒
                time.sleep(0.5)
                Get_xiaoshuo_mulu_context(a_context_url,a_context,header);



                pass
            else:
                # print("第%d行是最新章节，不做操作：%s," % (i, tab_dd));
                pass


            i+=1;
            pass




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
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"};
    # 【7】请求网络
    # 去除字符串中的空格
    Get_xiaoshuo_mulu(xiaoshuo_url,xiaoshuo_name,header);

    pass
