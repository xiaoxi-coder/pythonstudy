# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# 格式化文件  ALt+shift+enter
# help文档 python/Doc下文件内包含所有函数，直接搜索即可，eg：string, build-in function,random，data structure，re，list...
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random  # 随机数
import re  # 正则表达式

# 自定义函数
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# 字符串 字符串操作”字符串名.操作函数名(---)“
def demo_string():
    print_hi('PyCharm')
    print('hello world')

    stra = 'hello world'
    print(stra.capitalize())
    strb = 'new'
    print(1, stra.find('llo'))
    print(2, stra.rsplit('d'))
    print(3, stra + strb)


# 操作符 ：运算，真值，位
def demo_operation():
    print(1, 1 + 1, 2 / 4, 3 * 3, 5 - 2)
    print(2, True, not True)  # 1-True，0-False
    print(3, 1 < 2, 5 > 2)  # 比较运算符
    print(4, 2 << 3, 16 >> 3)  # 移位，左移三位:10-》10000;右移：10000-》10
    print(5, 5 | 3, 5 & 3, 5 ^ 3)  # 位运算 或：101|011=111=7; 与:101&011=1; 异或101^011=110;


# 内置函数
def demo_buildinfunction():
    x = 2  # 变量不区分变量类型
    y = 3.3
    print(x, type(x), y, type(y))  # 打印变量类型
    print(1, max(2, 1), min(5, 3))
    print(3, len('xxx'), len([1, 2, 3]))  # 字符长度
    print(4, range(1, 10, 3))  # ==c语言中 1:3:10
    print(5, dir(list))  # 打印函数名（cmd中dir打印当前文件下子文件名
    print(6, eval('x + 3'))  # 直接计算并打印
    print(7, chr(97), ord('a'))  # 字符与数字转换
    print(8, divmod(11, 3))  # 除数取余


# 控制流：if-else ；while；for；continue，break，pass；
def demo_controlflow():
    # if-else
    score = 65
    if score > 99:
        print(1, 'A')
    elif score > 60:
        print(2, 'B')
    else:
        print(3, 'C')

    # while
    while score < 100:
        print(score)
        score += 10
    score = 65

    # for:continue,break,pass
    for i in range(1, 10, 2):
        if i == 0:
            pass  # 空置，表示目前空操作，留待以后可能有别的操作
        if i < 5:
            continue  # 跳过此后的所有操作，继续执行循环
        print(4, i)
        if i == 7:
            break  # 结束循环


# data structure-数据结构
# list-列表 ；tuple-元祖 ；dictionary-字典 ；set-集合 ；

#   tuple
#   tuplea=（1,2,3）
#   tuple和list区别：tuple只读，不能进行后缀增减的操作，但list可以（list.append;list.extend;
#                   tuple定义用小括号（），list用中括号[];
#         和set区别：set为集合，可以增减，用set(());

#   list
def demo_list():  # list.函数名()；
    lista = [1, 2, 3]  # ==c语言vector
    print(1, lista)
    listb = [1, 'a', 1.1, 'c']  # 列表里可以包含任何形式的对象
    lista.extend(listb)  # 扩展，将listb缀在lista后，并替代lista
    print(2, lista, lista[1], len(lista))  # 访问列表，打印list长度
    print(3, 'a' in listb)  # 查找：问’a'是否在listb中？
    listb.insert(0, 'www')  # 插入： 在第0位置插入‘www'
    print(4, listb)
    listb.pop(1)  # 弹出：将第1位置上的元素去除
    print(5, listb)
    listb.reverse()  # 列表反向
    print(6, listb)
    listb.sort()  # 正向排序
    print(7, listb)
    listb.sort(reverse=True)  # 逆向排序
    print(8, listb)
    print(9, listb * 2)  # 打印多遍


#   dictionary
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}  # items={key:value}
    print(dicta)
    print(1, dicta.keys(), dicta.values())
    # print(2, dicta.has_key(1), dicta.has_key('3'))
    for key, value in dicta.items():  # 打印字典
        print('key-value:', key, value)  # 自动排序

    dictb = {'+': add, '-': sub}  # key = 字符； value = 函数
    print(3, dictb['+'](1, 2))  # [*]内表key，如数组a[*]表示数组a的第*位,此处表示执行key=’+‘时的value，即add操作
    print(4, dictb.get('-')(15, 3))  # get(*)表指针==[*]

    dictb['*'] = 'x'  # 增加新
    print(dictb)

    dicta.pop(1)  # 删除：删除key==1的item
    print(5, dicta)
    del dicta[2]  # 同上删除
    print(6, dicta)


#   set 集合
def demo_set():
    seta = set((1, 2, 3))  # 不加set就变成tuple
    listb = [1, 2, 3]
    tupleb = (1, 2, 3)
    setb = set(listb)
    # setb = set(tupleb)  # 结合
    print(seta, setb)
    print(1, seta.intersection(setb), seta & setb)  # 交集两种表达
    print(2, seta.union(setb), seta | setb)  # 并集两种表达
    print(3, seta - setb)  # seta减去seta与setb的交集，即seta-seta&setb
    seta.add('x')  # 增加元素，不限类型
    print(4, seta, len(seta))


# 面向对象
#   对象：利用类封装的数据结构实例，包括类变量和实例变量，及方法
#   类：用来描述具有相同属性和方法的对象的集合。
#   方法：类中定义的函数
#   具体实现：封装——继承——多态（方法重写）
class User:  # 封装：定义了一个类变量名为User的类（class）；eg：类型
    type = 'USER'  # 基本属性

    # __weight = 0 # 私有属性，类外部无法直接访问

    # 成员函数（方法）；init初始函数；self表类的实例，表当前对象地址，可以替换成别的单词；self.class指向类
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):  # 默认输出：打印
        return 'im ' + self.name + ' ' + str(self.uid)


class Admin(User):  # 继承：派生类Admin继承了基类User的字段和方法，即Admin属于User这一类，类似于dog属于animal
    type = 'ADMIN'  # （管理员）

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)  # 首先调用了基类User的构造函数（方法
        self.group = group  # 多态：此外在User的基础上添加或改写内容（方法

    def __repr__(self):  # 覆写基类的方法
        return 'im ' + self.name + ' ' + str(self.uid) + ' ' + self.group  # 输出也改变


def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 101, 'g1')
    else:
        raise ValueError('error')


# 异常处理 try
# 首先，执行try子句（在关键字try和关键字except之间的语句）
# 如果没有异常发生，忽略except子句，try子句执行后结束。
# 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
# 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
# finally始终都会执行
def demo_exception():
    try:
        print(2 / 1)
        print(2 / 0)  # 异常
        raise Exception('Raise Error', 'NowCoder')  # raise 抛出一个指定的异常
    except Exception as e:  # e表示error类型：ValueError，NameError，TypeError...
        print('error:', e)
    # except可列举error类型，分别处理
    # 此处可以用else语句
    finally:  # 清理行为
        print('clean up')


# 随机数/正则表达式
'''
随机数           正则表达式
random.random   \d\D-digital； \s\S-space； \w\W-word；大写表示非（非数字，非空格，非字母）
random.seed     +-匹配一次及以上,*-匹配零次及以上,?-匹配零次或一次
random.randint  |-或,^-非
random.choice   0
random.sample   \\
'''


def demo_random():
    # 随机数实际上是伪随机数，随机数的产生实际上有一定公式，且下一个随机数由上一个随机数产生
    # eg:
    # random.seed(1) # 去掉此行注释，指定seed后，即指定第一个随机数，此后每次运行程序，第1,2,3次的随机数不发生改变
    # eg:上机考试每个学生的题目从题库中随机抽取，原理就是系统派发给每个学生的seed不同，因此每个学生的试卷实际上只要记得seed值，即可知道试卷内容
    print(1, random.random())  # 0-1浮点数
    print(2, random.random()*100)  # 0-100浮点数
    print(3, random.randint(0,100))  # 0-100整数
    print(4,random.choice(range(0,100))) # 0-100随机抽一个
    print(5,random.sample(range(0,100),4)) # 抽样：0-100随机抽4个
    a = [1,2,3,4,5]
    random.shuffle(a)  # 随机打乱
    print(6,a) # 0-100随机抽一个


def demo_re():

    str = 'abc123def12gh15'
    p1 = re.compile('\d+') # pattern 模式：打印数字（连续的数字算作一个数）; +表示匹配一个以上
    print(1,p1.findall(str))
    p2 = re.compile('\d') # pattern 模式：打印数字（匹配单个数字）
    print(2,p2.findall(str))

    # eg：登录邮箱时要求登入邮箱的格式满足什么要求可以用正则表达式来实现
    str = 'a@163.com; b@gmail.com; c@qq.com; dc@163.com'
    p3 = re.compile('[\w]+@[163|qq]+.com') # 打印163邮箱地址；[163|qq]+表示可以匹配163，也可以匹配qq，即打印两类邮箱的地址
    print(3,p3.findall(str))                  # \w表示word

    str ='<html><h>title</h><body>xxxxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')   #找出title：可以发现title非<开头，
    print(4,p4.findall(str))
    p5 = re.compile('<h>([^<]+)</h>''<body>([^<]+)</body>')   #仅打印title和xxxxx
    print(5,p5.findall(str))

    # 想要爬一个网页内的某些特定的属性,比如某网页内的发表时间
    str = 'jsh2016-07-11heifh'
    p6 = re.compile('\d\d\d\d-\d\d-\d\d')
    print(6,p6.findall(str))
    p7 = re.compile('\d{4}-\d{2}-\d{2}')
    print(7,p7.findall(str))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':  # ==main{ }

    # demo_string()

    # demo_operation()

    # demo_buildinfunction()

    # demo_controlflow()

    # demo_list()

    # demo_dict()

    # demo_set()

    '''
    user1 = User('u1', 1)  # 类对象实例化
    print(user1)
    admin1 = Admin('a1', 101, 'g1')
    print(admin1)
    print(create_user('USER'))
    '''

    # demo_exception()

    # demo_random()

    demo_re()