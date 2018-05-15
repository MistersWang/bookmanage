import time
import  pickle
import os

def Login():
    name = input("请输入学号(q退出)：")
    while (name != 'q') and (name != 'Q'):
        passw = input("请输入密码：")
        with open("D:\\python_code\\usersadd.pkl", "rb") as f:
            b = f.seek(0, os.SEEK_END)
            a = f.seek(0, os.SEEK_SET)
            while f.tell() != b:
                mylist = pickle.load(f)
                if mylist["学号："] == name and mylist["密码："] == passw:
                    if mylist["权限："] == "1":
                        Menumanages()
                        return
                    else:
                        Menustudents()
                        return

        print("账号或密码错误，请重新输入！！")
        name = input("请输入学号(q退出)：")
    return
def Menumanages():
    while 1:
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
        num = int(input("请输入对应功能的编号>>>"))
        if num == 1:
            pass
        if num == 2:
            pass
        if num == 3:
            pass
        if num == 4:
            pass
        if num == 5:
            pass
        if num == 6:
            B_addbook()
        if num == 7:
            pass
        if num == 8:
            pass
        if num == 9:
            S_addstudent()
        if num == 10:
            pass
        if num == 11:
            pass
        if num == 12:
            pass
        if num == 13:
            pass
        if num == 14:
            pass
        if num == 15:
            E_exit()

def Menustudents():
    while 1:
        print(" ===================>>>Welcome<<<======================")
        print("     1、查询馆藏                 2、借阅图书         ")
        print("     3、归还图书                 4、个人借阅         ")
        print("     5、修改密码                 6、 退出     ")
        print("===============>>>copyright (c) 2018<<<================")
        num = int(input("请输入对应功能的编号>>>"))
        if num == 1:
            pass
        if num == 2:
            pass
        if num == 3:
            pass
        if num == 4:
            pass
        if num == 5:
            pass
        if num == 6:
            E_exit()


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
            return
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
# def B_delbook():

# def B_modbook():

# def B_listbook():

# def B_listbrobook():

# def M_addmanage():

# def M_delmanage():

# def M_modmanage():

# def M_listmanage():

def S_addstudent():
    users = {}
    # bor='no'
    # applytime='none'
    print("*****在第一次输入以字母‘q’退出添加*****")
    User_num = input("请输入您的学号：")
    while 1:
        if (User_num == 'q') or (User_num == 'Q'):
            print("退出添加中....")
            time.sleep(1)
            return
        else:
            User_passw = input("请输入您的密码：")
            User_power = input("请输入权限：")
            now = int(round(time.time() * 1000))
            times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
            users = {"学号：": User_num, "密码：": User_passw, "权限：": User_power, "申请时间": times, }
            # print(book)
            f = open("D:\\python_code\\usersadd.pkl", "ab")
            pickle.dump(users, f)
            f.close()
            # f=open("D:\\bookadd.pkl","rb")
            #         # book2=pickle.load(f)
            #         # print(book2)
            print("学号：%s  密码：%s  权限：%s  申请时间：%s  " % (User_num, User_passw, User_power, times))
            print("添加成功！！！")
            User_num = input("请输入您的学号：")
# def S_delstudent():

# def S_modstudent():

# def S_liststudent():

def E_exit():
    print("正在退出....")
    time.sleep(1)
    exit()


Login()


