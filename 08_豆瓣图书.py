
# 【1】导包
import requests;
from bs4 import BeautifulSoup;
from openpyxl import Workbook;
import os

# 【7】数据录入
def Play_data_Excle(book_class_list,book_data_lists):
    # 1.创建表格
    wb = Workbook();
    # 2.创建选项卡
    for i in range(0,len(book_class_list)):
        ws_01 = wb.create_sheet(book_class_list[i],i);
        pass
    # 4.根据数据遍历
    j =0;
    for book_class_data in book_data_lists:
        print("===:",book_class_data);
        # 4.1选择选项卡
        ws_02 = wb[book_class_list[j]]
        ws_02.append(["书名","作者及翻译","出版社","时间","价格","评分","图片地址","书籍地址"]);
        for book_item_data in book_class_data:
            print("***:",book_item_data)
            ws_02.append(book_item_data);

            pass
        j+=1;

        pass

    # 3.保存
    wb.save("豆瓣图书汇总.xlsx")
    pass


# 【6】有缓存的情况下
def Get_Local_data():
    print("有本地数据")

    pass

# 【5】请求网络访问数据
def Get_Requests_data():
    print("没有本地数据");

    pass


# 【4】查询每一个种类的书籍数据
def Get_book_content(book_class_item,douban_book_url,header):
    Net_T = False;
    print("开始访问网络：爬取【%s】数据"%book_class_item);
    # 1.创建一个数组-用于保存访问到的数据
    book_class_content = [];
    # 2.每类数据网址拼接
    # https://www.douban.com/tag/财经/book?start=0
    # ==================================================================
    douban_book_url = douban_book_url+book_class_item+"/book?start=0";
    print("下载地址：",douban_book_url);
    # ==============特殊条件-没网=======================
    caijing_path = "C:\/Users\/Administrator\/Desktop\/WHGC2019年2月25日\/09_豆瓣图书汇总\/豆瓣图书数据汇总\/财经\/财经.html"
    if os.path.exists(caijing_path):
        Net_T = True;
        pass

    # ===================================================
    if Net_T:
        # 有数据的情况下
        Get_Local_data();
        pass
    else:
        # 没有数据的情况下
        Get_Requests_data();

        pass

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
        # 8.数据解析
        soup = BeautifulSoup(data,"html.parser");
        # 8-1.获取div class = mod book-list
        div_book_list = soup.find("div",attrs={"class":"mod book-list"});
        # print(div_book_list);
        # 8-2.获取所有书籍的dl []
        tag_dls =div_book_list.find_all("dl");
        print("书籍数目：",len(tag_dls));
        # 8-3遍历循环获取每一本书
        i=1;
        for tag_dl in tag_dls:
            print("%s第%d本书详情："%("\n=============================================\n",i));
            # 1.获取书籍图片地址
            book_img_url = tag_dl.dt.a.img["src"];
            print("第%d本书：%s" % (i, book_img_url));
            # 2.获取书籍名称
            book_name = tag_dl.dd.a.string;
            print("第%d本书：%s" % (i, book_name));
            # 3.获取书籍的详情链接
            book_url = tag_dl.dd.a["href"];
            print("第%d本书：%s" % (i, book_url));
            # 4.获取书籍详情信息
            div_desc = str(tag_dl.dd.find("div",attrs={"class":"desc"}).string).strip();
            print("第%d本书：%s" % (i, div_desc));
            # 5.获取书籍评分
            # 判断div的个数
            div_num = tag_dl.dd.find_all("div");
            span_rating_nums = "0";
            if len(div_num) == 2:
                span_rating_nums = tag_dl.dd.find("span", attrs={"class": "rating_nums"}).string;
                pass
            print("第%d本书：%s" % (i, span_rating_nums));
            # 6.数据拆分处理：
            print("第%d===：%s" % (i, div_desc.split("/")));
            div_content = div_desc.split("/");
            # 吴晓波 / 中信出版社 浙江人民出版社 / 2007-1 / 35.00
            # 拉斯·特维德 / 董裕平 / 中信出版社 / 2012-11 / 69.00元
            # ["作者及翻译","出版社信息","出版时间","价格"]
            # 例如：浙江人民出版社 / 2007-1 / 35.00
            if len(div_content)<4:
                print("由于书籍信息不完整，无法录入")
                div_content =["","","",""];
                pass
            # 6-1.获取价格
            book_jg = div_content[-1];
            book_time = div_content[-2];
            book_add = div_content[-3];
            # 作者及翻译
            book_author = "";
            for j in range(0,len(div_content)-3):
                book_author+=div_content[j]+"/"
                pass
            #
            book_author = book_author[0:len(book_author)-1];
            print("第%d本书：%s" % (i, book_author));
            # 存储的数据格式
            # ["书名","作者及翻译","出版社","时间","价格","评分","图片地址","书籍地址"]
            print(["《"+book_name+"》",book_author,book_time,book_jg,span_rating_nums,book_img_url,book_url])
            book_class_content.append(["《"+str(book_name).strip()+"》"
                                          ,str(book_author).strip()
                                          ,str(book_add).strip()
                                          ,str(book_time).strip()
                                          ,str(book_jg).strip()
                                          ,str(span_rating_nums).strip()
                                          ,str(book_img_url).strip()
                                          ,str(book_url).strip()]);

            i+=1;

            pass

        pass
    else:
        print("网络访问失败。查不到:%s"%book_class_item);
        pass




    # ==================================================================
    return book_class_content;

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
        book_data_lists.append(book_item_data);
        print(book_data_lists);
        # 4.数据的录入
        Play_data_Excle(book_class_list,book_data_lists);





        pass

    pass


# 【2】Python文件的执行入口
if __name__ == "__main__":
    print("==================豆瓣图书汇总======================");
    # 1.创建数组：用于存放数据的种类
    book_class_list = ["财经","爬虫","小说","历史","演讲","刘帅涛"];
    # book_class_list = ["财经"];
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
























