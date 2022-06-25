# -*- coding:utf-8 -*-


# 单例模式装饰器
def single(cls):
    instance = {}

    def func(*args, **kwargs):
        if cls in instance:
            return instance[cls]
        else:
            instance[cls] = cls(*args, **kwargs)
            return instance[cls]
        return func


@single     # Test = single(Test)
class Test:
    pass


t1 = Test()
