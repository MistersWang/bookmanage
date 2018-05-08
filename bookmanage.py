import time
import  pickle
import os

def Login():

def Menumanages():
    print(" ===================>>>Welcome<<<======================")
    print("     1、查询馆藏                 2、借阅图书         ")
    print("     3、归还图书                 4、借阅列表         ")
    print("     5、个人借阅                 6、增加图书        ")
    print("     7、删除图书                 8、更改图书         ")
    print("     9、增加学生                10、删除学生         ")
    print("    11、增加管理员              12、删除管理员         ")
    print("    13、修改学生密码            14、修改管理员密码      ")
    print("    15、退出                       ")
    print("===============>>>copyright (c) 2018<<<================")
def Menustudents():
    print(" ===================>>>Welcome<<<======================")
    print("     1、查询馆藏                 2、借阅图书         ")
    print("     3、归还图书                 4、个人借阅         ")
    print("     5、修改密码                 6、 退出     ")
    print("===============>>>copyright (c) 2018<<<================")
def B_addbook():
    book = {}
    bor = 'no'
    bortime = 'none'
    print("*****在第一次输入以字母‘q’退出添加*****")
    Book_isn = input("请输入书的ISN编号：")
    while 1:
        if (Book_isn == 'q') or (Book_isn == 'Q'):
            print("退出添加中....")
            time.sleep(2)
            exit()
        else:
            Book_name = input("请输入书的名字：")
            Book_pub = input("请输入出版社名称：")
            Book_price = input("请输入书价格：")
            now = int(round(time.time() * 1000))
            times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
            book = {"ISN：": Book_isn, "书名：": Book_name, "出版社：": Book_pub, "价格：": Book_price + "￥", \
                    "入库时间：": times, "是否借出：": bor, "借出时间：": bortime}
            # print(book)
            f = open("D:\\bookadd.pkl", "wb")
            pickle.dump(book, f)
            f.close()
            # f=open("D:\\bookadd.pkl","rb")
            #         # book2=pickle.load(f)
            #         # print(book2)
            print("ISN：%s  书名：%s  出版社：%s  价格：%s￥  入库时间：%s  是否借出：%s  借出时间：%s  " \
                  % (Book_isn, Book_name, Book_pub, Book_price, times, bor, bortime))
            print("入库成功！！！")
            Book_isn = input("请输入书的ISN编号：")
def B_delbook():

def B_modbook():

def B_listbook():

def B_listbrobook():

def M_addmanage():

def M_delmanage():

def M_modmanage():

def M_listmanage():

def S_addstudent()

def S_delstudent():

def S_modstudent():

def S_liststudent():



# 主函数
Login()

B_addbook()


B_delbook()


B_modbook()


B_listbook()


B_listbrobook()


M_addmanage()


M_delmanage()


M_modmanage()


M_listmanage()


S_addstudent()


S_delstudent()

S_modstudent()


S_liststudent()
