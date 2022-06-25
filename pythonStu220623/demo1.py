# -*- coding:utf-8 -*-


class MyStr(object):
     # 由此可见是s1触发的魔术方法
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

    def __add__(self, other):
        print('等等等')
        # print(self.data)
        # print(other)
        return self.data + other.data

    def __sub__(self, other):
        return self.data.replace(other.data, '')


s1 = MyStr('11')
s2 = MyStr('22')
s3 = MyStr(s1 + s2)     # s1 + s2 = s1.__add__(s2)
print(s3 - s2)