# -*- coding:utf-8 -*-

# with open('test.txt','w+',encoding='utf8') as file:
#     # file 文件操作句柄
#     file.write('你好哇')


class MyOpen(object):
    # 文件操作的上下文管理器
    def __init__(self,file_path,method,encoding='utf8'):
        self.file_path = file_path
        self.method = method
        self.encoding = encoding

    def __enter__(self):
        self.f = open(self.file_path,self.method,encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with MyOpen('test.txt','r') as file:
    # print(file)
    content = file.read()
    print(content)

with MyOpen('test.txt','w') as file:
    print(file)
    
    

