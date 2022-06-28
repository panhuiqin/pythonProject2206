# -*- coding:utf-8 -*-


# 单例模式装饰器
def single(cls):
    # 为了避免类属性被对象/类直接调用篡改值，该变量定义为私有属性，__开头(类/对象无法直接调用)
    __instance = {}

    def func(*args, **kwargs):
        if cls in __instance:
            return __instance[cls]
        else:
            __instance[cls] = cls(*args, **kwargs)
            return __instance[cls]
        return func


@single     # Test = single(Test)
class Test:
    pass


t1 = Test()
