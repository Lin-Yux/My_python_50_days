## 模块和函数
## *Martin Fowler*曾经说过：“**代码有很多种坏味道，重复是最坏的一种！**”
'''
函数的定义：
数学上的函数通常形如`y = f(x)`或者`z = g(x, y)`这样的形式，在`y = f(x)`中，`f`是函数的名字，`x`是函数的自变量，`y`是函数的因变量；
而在`z = g(x, y)`中，`g`是函数名，`x`和`y`是函数的自变量，`z`是函数的因变量。
Python中的函数跟这个结构是一致的，每个函数都有自己的名字、自变量和因变量。我们通常把Python中函数的自变量称为函数的参数，而因变量称为函数的返回值。

函数的命名规则和语法：
在Python中可以使用`def`关键字来定义函数，和变量一样每个函数也应该有一个漂亮的名字，
命名规则跟变量的命名规则是一致的（赶紧想一想我们之前讲过的变量的命名规则）。
在函数名后面的圆括号中可以放置传递给函数的参数，就是我们刚才说到的函数的自变量，
而函数执行完成后我们会通过`return`关键字来返回函数的执行结果，就是我们刚才说的函数的因变量。
一个函数要执行的代码块（要做的事情）也是通过缩进的方式来表示的，跟之前分支和循环结构的代码块是一样的。
大家不要忘了`def`那一行的最后面还有一个`:`，之前提醒过大家，那是在英文输入法状态下输入的冒号。

重构的概念：
我们可以通过函数对上面的代码进行重构。**所谓重构，是在不影响代码执行结果的前提下对代码的结构进行调整。**重构之后的代码如下所示。
'''
##eg：给定一个正整数和自变量的个数，求出有多少组正整数解，即，x1+x2+x3+x4=8，求x1,x2,x3,x4有多少组
## 隔板法：八个苹果，三块隔板，n=C(7,3)(7个空隙选3个放隔板)，排列组合的定义和公式：https://baike.baidu.com/item/%E6%8E%92%E5%88%97%E7%BB%84%E5%90%88/706498?fr=aladdin#2_1
## C(n,m)=n!/((n-m)!*m!)，我们注意到这里其实可以通过写一个阶乘的函数来实现重复调用

'''
def f_n(num):   ## 定义一个求阶乘的函数，def 函数名（形参）：
    ## 函数也是通过缩进来控制是不是一个整体,最后通过一个return返回
    cal=1
    for i in range(1,num+1):
        cal=cal*i ## for-in循环后面也要:（冒号）不要忘了
    return cal

n=int(input("请输入正整数："))
m=int(input("请输入自变量个数："))
if(n<m):
    print("ERROR")
if(m==n):
    print(1)
else:
    n=n-1
    resule=f_n(n)/f_n(n-m)/f_n(m) ## 这里输出会成小鼠，因为python里的"/"就是正常的浮点数除法了，如果想要控制为整数可以用//来实现
    ## resule=f_n(n)//f_n(n-m)//f_n(m)
    print(f"C({n},{m})={resule}")
'''

'''
·函数中没有return语句，就默认返回代表空值的`None`
·定义函数时，函数也可以没有自变量，但是函数名后面的圆括号是必须有的
·Python中还允许函数的参数拥有默认值（就是在调用函数的时候如果没有指定实际参数，那么就会启用默认值）
'''
## eg1：上面那个摇色子游戏
'''
import random
def roll_dice(n=2): ## 调用roll_dice()时，如果没有指定实际参数，而是直接调用函数，那么就默认2是实际参数
    ## 这里实现的是摇n个色子获得点数的功能
    sum=0
    for i in range(1,n+1):
        sum=sum+random.randint(1,6)
    return(sum)

print(roll_dice(3)) ## 这时候是指定了实际参数为3，即三个色子获得一个点数
'''

'''
## eg2：参数的传递
def add(a=0,b=0,c=0):
    ## 默认参数a=0,b=0,c=0
    return(a+b+c)
print(add()) ## 返回0，调用了a,b,c为0的默认值
print(add(1)) ## 返回1，调用了a=1,b=0,c=0
print(add(1,3)) ## 返回4，调用了a=1,b=3,c=0
print(add(c=1,b=1,a=2)) ## 当传递的实际参数不按照形式参数来的时候，可以通过形参=实参值来实现乱序调用
'''

# note:带默认值的参数必须放在不带默认值的参数之后，否则将产生`SyntaxError`错误，
# 错误消息是：`non-default argument follows default argument`，翻译成中文的意思是“没有默认值的参数放在了带默认值的参数后面”。
# 我没有试出来


## eg3：可变参数
## 可变参数指的是在调用函数时，可以向函数传入0个或任意多个参数
'''
def add_2(*args): ## 这里如果args是个数组的话好像挺不错，这时候实现add()就无所谓传入几个参数了
    sum=0 ## 上面这个args是一个数组，*这个在C是数组首地址，这里具体是什么后面再复习一下
    for i in args:
        sum=sum+i
    return(sum)

print(add_2(1,2,3))
print(add_2(1,9))
print(add_2())
'''

## eg4：模块中的函数
## 如果在同一个.py文件里面，定义了两个名称相同的函数，就会报错
## 如果我们在不同的模块里面，比如说module1.py里面定义一个foo()函数，module2.py里面定义另一个foo()函数
## 我们用import module1 import moduel2，然后再module1.foo()（2类似），进行分别调用就不会冲突
'''
import day_7_1
import day_7_2
day_7_1.foo()
day_7_2.foo()
'''
## 还有就是import的时候可以用as来起别名，比如说import numpy as nu
## 或者可以不导入模块，只导入模块中的某个函数，比如说 from day_7_1 import foo ，后面也可以as来起别名

## python的标准库，就类似C的studio.h，但是Python是直接内置了，不需要再额外import
## 包括一些常见的数学运算函数，如：abs(),sum(),min(),oct()(返回八进制字符串),type()等

