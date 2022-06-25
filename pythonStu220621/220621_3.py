# -*- coding:utf-8 -*-


class Test(object):
    # 继承object
    def __call__(self, *args, **kwargs):
        print('对象触发了call方法')


test = Test()
test()