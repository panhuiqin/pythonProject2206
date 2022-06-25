# -*- coding:utf-8 -*-


# 类实现装饰器
class Decorator:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('装饰器的功能')
        self.func()


@Decorator      # test = Decorator(test) 创建对象
def test():
    print('函数的功能')


test()