
# 【1】导包
import requests;
from bs4 import BeautifulSoup;
from openpyxl import Workbook;
import os


# 【4】查询每一个种类的书籍数据
def Get_book_content(book_class_item,douban_book_url,header):

    print("开始访问网络：爬取【%s】数据"%book_class_item);
    # 1.创建一个数组-用于保存访问到的数据
    book_class_content = [];
    # 2.每类数据网址拼接
    # https://www.douban.com/tag/财经/book?start=0
    # ==================================================================
    douban_book_url = douban_book_url+book_class_item+"/book?start=0";
    print("下载地址：",douban_book_url);
    # 3.请求网络
    requests_01 = requests.get(douban_book_url,data = header);
    # 4.判断网络
    if requests_01.status_code == 200:
        # 5.修改编码格式
        # print(requests_01.encoding);
        # requests_01.encoding = "utf-8"
        # 6.获取网址源码
        # data = requests_01.text;
        data =requests_01.content.decode("utf-8");
        # 7.数据存储
        file_path = "C:\/Users\/Administrator\/Desktop\/WHGC2019年2月25日\/09_豆瓣图书汇总\/豆瓣图书数据汇总\/%s\/"%book_class_item
        if not os.path.exists(file_path):
            os.makedirs(file_path);
            pass
        file = open(file_path+"%s.html"%book_class_item,"w",1,encoding="utf-8");
        file.write(data);
        file.close();

        pass
    else:
        print("网络访问失败。查不到:%s"%book_class_item);
        pass




    # ==================================================================

    pass

# 【3】爬取数据之前的分类处理
def Do_spider(book_class_list,douban_book_url,header):
    # 1.创建一个数组用于存放书籍数据
    book_data_lists = [];
    # 2.遍历所有数据种类-并创建完整url地址
    for book_class_item in book_class_list:
        print("==============================================================")
        print("数据种类：",book_class_item);
        # 3.开始爬取数据
        book_item_data = Get_book_content(book_class_item,douban_book_url,header);



        pass

    pass


# 【2】Python文件的执行入口
if __name__ == "__main__":
    print("==================豆瓣图书汇总======================");
    # 1.创建数组：用于存放数据的种类
    book_class_list = ["财经","爬虫","小说","历史","演讲","刘帅涛"];
    # 2.豆瓣图书网络地址
    # https://www.douban.com/tag/财经/book?start=0
    douban_book_url = "https://www.douban.com/tag/";
    # 3.用户代理
    """
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
    user-agent:Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4
    """
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    # 4.做分工处理
    Do_spider(book_class_list=book_class_list,douban_book_url=douban_book_url,header=header);


    pass
























