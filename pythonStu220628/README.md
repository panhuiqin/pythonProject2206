1. 实现数据库操作的上下文管理器
demo1.py

2. 面向对象的三大特征是什么 多态是什么
    1）封装、继承、多态
    2）一类事物有多种形态，一个抽象类有多个子类，不同的子类对象调用相同的方法，产生不同的执行结果
    
3. 私有属性怎么定义 不同的定义方式有什么区别
    1）单下划线开头定义
        对外公开，外部可以直接访问
    2）双下划线开头定义
        对外不公开，外部不可以直接访问，为了保护变量对其修改了属性名（原有属性名前加_类名）
4. 属性访问方法
    1）object.__getattr__：对象被访问/查找属性，且属性不存在时触发
    2）object.__getattrbute__：对象被访问/查找属性，第一时间触发
    3）object.__setattr__：设置对象属性时触发
    4）object.__delete__：删除对象属性时触发
        
ORM模型
O（Objects）- 类和对象
R（Relation）- 关系，数据库中的表格
M（Mapping）- 映射

ORM ---  DB
类  ---  数据表
对象 --- 数据行
属性 --- 字段

一. ORM框架的功能
    1）建立模型类和表之间的对应关系，允许我们通过面向对象的方式来操作数据库
    2）根据设计的模型类生成数据库中的表格
    3）通过方便的配置就可以进行数据库的切换
    
二. 数据库的字段类型
    1. mysql常用数据类型
        1）整型：int、bit
        3）小数：decimal
        3）字符串：varchar、char
        4）日期事件：datetime、date、time
        5）枚举值:enum
    2.ORM模型中对应的字段（Django为例）
        1）BooleanField：布尔字段 值为True或False
        2）CharField：字符串，参数max_length表示最大字符个数
        3)IntegerField：整数
        
        
元类
python中的任何新式类以及python3中的任何类都是type元类中的一个实例。函数type()实际上是一个元类，type就是python用来创建所有类的元类
一. 元类和继承的基类
    type：python3中所有的类都是通过type来创建的
    object：python3中所有类的顶级父类都是object
