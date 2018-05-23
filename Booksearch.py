#打开文档
#c存三本书放到txt，放在pickle里边
#while循环，被文档一条一条的读出来
    #把没一条都给一个dict
        #判断dict[书名=我们要的]
            #判断dict[是否被借出]
               #如果没有被借出，就把他输出给写入到一个TXT函数里边
            #else 进行下一次判断
        #else进行下一次判断
#关闭所有文件
#把刚才的文档导出来
#放入一个GUI界面里边进行选择
#确认选择
#退出
import os
import sys
import pickle
book1={
'ISNB':'swk1112', '书名':"毛泽东传1" ,'是否借出':0,'借出时间':20180511,
}
book2={
'ISNB':'swk1113', '书名':"毛泽东传2" ,'是否借出':1,'借出时间':20180511,
}
book3={
'ISNB':'swk1114', '书名':"毛泽东传1" ,'是否借出':0,'借出时间':20180511,
}

pickle_file=open('book.pkl','wb')
pickle.dump(book1,pickle_file)
pickle.dump(book2,pickle_file)
pickle.dump(book3,pickle_file)
pickle_file.close()
pickle_file=open('book.pkl','rb')
a=pickle_file.seek(0,os.SEEK_END)
b=pickle_file.seek(0,os.SEEK_SET)
while pickle_file.tell() != a:
    line = pickle.load(pickle_file)
    dictk = line
    if (dictk['书名'] == "毛泽东传1"):
            if (dictk['是否借出'] == 0):
                pickle_file1 = open('E:\\my_list.txt', 'ab')
                pickle.dump(dictk, pickle_file1)
                pickle_file1.close()
            else:
                print("借出")#line = pickle.load(pickle_file)
    else:
           print("没找到") #line = pickle.load(pickle_file)
    print("next")
pickle_file2 = open('E:\\my_list.txt', 'rb')
a1 = pickle_file2.seek(0, os.SEEK_END)
b1 = pickle_file2.seek(0, os.SEEK_SET)
while pickle_file2.tell() != a1:
    my_list2 = pickle.load(pickle_file2)
    print(my_list2)
    #如果没有搜索到的要的，请重新输入，退出
    #如果搜索到了

pickle_file2 .close()
    #删除，退出
file = 'E:\\my_list.txt'
if os.path.exists(file):
    os.remove(file)
    print('yes')
else:
    print ('no such file:%s' % file)
