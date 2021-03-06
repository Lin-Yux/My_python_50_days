## day_15
## 面向对象编程入门

# 简介：
# ①面向对象编程是一种非常流行的编程范式（programming paradigm），所谓编程范式就是程序设计的方法学，也就是程序员对程序的认知和理解。
# “程序是指令的集合”，运行程序时，程序中的语句会变成一条或多条指令，然后由CPU（中央处理器）去执行。
# 为了简化程序的设计，我们把相对独立且经常重复使用的代码放置到函数中，在需要使用这些代码的时候调用函数即可。
# 如果一个函数的功能过于复杂和臃肿，我们又可以进一步将函数进一步拆分为多个子函数来降低系统的复杂性。

# ②面向对象编程的世界里，程序中的数据和操作数据的函数是一个逻辑上的整体，我们称之为对象，对象可以接收消息，解决问题的方法就是创建对象并向对象发出各种各样的消息

# ③**面向对象编程**：
# 把一组数据和处理数据的方法组成**对象**，
# 把行为相同的对象归纳为**类**，
# 通过**封装**隐藏对象的内部细节，
# 通过**继承**实现类的特化和泛化，
# 通过**多态**实现基于对象类型的动态分派。
# 关键词：**对象**（object）、**类**（class）、**封装**（encapsulation）、**继承**（inheritance）、**多态**（polymorphism）

# ④类和对象：
# 在面向对象编程中，**类是一个抽象的概念，对象是一个具体的概念**。
# 我们把同一类对象的共同特征抽取出来就是一个类，比如我们经常说的人类，这是一个抽象概念，
# 而我们每个人就是人类的这个抽象概念下的具体的实实在在的存在，也就是一个对象。简而言之，类是对象的蓝图和模板，对象是类的实例。

# 面向对象编程的世界中，**一切皆为对象**，**对象都有属性和行为**，**每个对象都是独一无二的**，而且**对象一定属于某个类**。
# 对象的属性是对象的静态特征，对象的行为是对象的动态特征。按照上面的说法，如果我们把拥有共同特征的对象的属性和行为都抽取出来，就可以定义出一个类。

## 定义类
# 在Python中，可以使用`class`关键字加上类名来定义类，通过缩进我们可以确定类的代码块，就如同定义函数那样。
# 在类的代码块中，我们需要写一些函数，我们说过类是一个抽象概念，那么这些函数就是我们对一类对象共同的动态特征的提取。
# 写在类里面的函数我们通常称之为**方法**，方法就是对象的行为，也就是对象可以接收的消息。
# 方法的第一个参数通常都是`self`，它代表了接收这个消息的对象本身。
class Student: 
    def study(self,course_name):
        print(f"学生正在学习：{course_name}")
        
    def play(self):
        print("学生正在玩游戏")

## 创建和使用对象
# 用构造器语法来创建对象
stu_1 = Student() ## 类名() 就是构造器语法，用来创建某一个类的对象
stu_2 = Student()

print(stu_1) ## print对象就会显示出这个对象的类和十六进制内存逻辑地址
print(stu_2)
stu_3 = stu_2 ## 没有创建一个新的对象，只是让两个变量指向同一个地址

# 调用对象的方法
## 通过“类.方法”调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
Student.study(stu_1,"Python")
## 通过“对象.方法”调用方法，点前面的对象就是接收消息的对象，只需要传入第二个参数
stu_1.study("python")

Student.play(stu_2)
stu_2.play()

## 初始化方法
# 刚才我们创建的学生对象只有行为没有属性，如果要给学生对象定义属性，我们可以修改`Student`类，为其添加一个名为`__init__`的方法。
# 在我们调用`Student`类的构造器创建对象时，首先会在内存中获得保存学生对象所需的内存空间，
# 然后通过自动执行`__init__`方法，完成对内存的初始化操作，也就是把数据放到内存空间中。
# 所以我们可以通过给`Student`类添加`__init__`方法的方式为学生对象指定属性，同时完成对属性赋初始值的操作，`__init__`方法通常也被称为初始化方法。

class Student:
    def __init__(self,name,age): ## 定义初始化方法，让一些属性可以赋到类上
        self.name = name
        self.age = age 

    def study(self,course_name):
        print(f"学生正在学习：{course_name}")
    
    def play(self):
        print("学生正在玩游戏")

stu_1=Student() ## TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
## note:由于创建类时会自动执行__init__方法，因此我们在用构造器构造时，要注意参数的个数要符合__init__方法的参数个数
stu_1=Student('王大锤', 15)
print(stu_1)

stu_1.study("Python")
stu_1.play() ## 用VS这种IDE有一个好处就是你把光标放到括号内，它就会告诉你要传几个参数

## 打印对象
## 魔术方法：__(两个下划线，dunder)开头和结尾的方法
## 如果我们在print(class)的时候不希望看到内存地址而是希望看到其他的信息，我们可以通过定义__repr__方法来完成
class Student:
    def __init__(self,name,age): ## 定义初始化方法，让一些属性可以赋到类上
        self.name = name
        self.age = age 

    def study(self,course_name):
        print(f"学生正在学习：{course_name}")
    
    def play(self):
        print("学生正在玩游戏")

    def __repr__(self):
        return(f"姓名是{self.name}，年龄是{self.age}") ## self就是指这个对象本身，本质上也是属于这个class，所以可以用.来调用属性和方法

stu_1=Student('王大锤', 15)
print(stu_1)

## 面向对象编程的三大支柱
# 面向对象编程有三大支柱：封装、继承和多态。先说一下什么是封装。我自己对封装的理解是：隐藏一切可以隐藏的实现细节，只向外界暴露简单的调用接口。
# 我们在类中定义的对象方法其实就是一种封装，这种封装可以让我们在创建对象之后，
# 只需要给对象发送一个消息就可以执行方法中的代码，也就是说我们在只知道方法的名字和参数（方法的外部视图）
# 不知道方法内部实现细节（方法的内部视图）的情况下就完成了对方法的使用。

# 举一个例子，假如要控制一个机器人帮我倒杯水：
# 如果不使用面向对象编程，不做任何的封装，那么就需要向这个机器人发出一系列的指令，如站起来、向左转、向前走5步、拿起面前的水杯、向后转、向前走10步、弯腰、放下水杯、按下出水按钮、等待10秒、松开出水按钮、拿起水杯、向右转、向前走5步、放下水杯等，才能完成这个简单的操作。
# 按照面向对象编程的思想，我们可以将倒水的操作封装到机器人的一个方法中，当需要机器人帮我们倒水的时候，只需要向机器人对象发出倒水的消息就可以了。

# 在很多场景下，面向对象编程其实就是一个三步走的问题。第一步定义类，第二步创建对象，第三步给对象发消息。
# 有的时候我们是不需要第一步的，因为我们想用的类可能已经存在了。Python内置的`list`、`set`、`dict`其实都不是函数而是类
# 如果要创建列表、集合、字典对象，我们就不用自定义类了。
# 有的类并不是Python标准库中直接提供的，它可能来自于第三方的代码。
# 在某些特殊的场景中，我们会用到名为“内置对象”的对象，所谓“内置对象”就是说上面三步走的第一步和第二步都不需要了，
# 因为类已经存在而且对象已然创建过了，直接向对象发消息就可以了，这也就是我们常说的“开箱即用”。

## eg1：定义一个类描述数字时钟。
import time
## 创建clock类
class clock:
    def __init__(self,hour=0,minite=0,second=0):
        self.hour=hour
        self.minite=minite
        self.second=second
    
    def runtime(self):
        self.second+=1
        if(self.second==60):
            self.minite+=1
            self.second=0
            if(self.minite==60):
                self.minite=0
                self.hour+=1

    def __repr__(self):
        return (f"现在时间是:{self.hour}:{self.minite}:{self.second}")

## 创建clock_1为clock类的一个对象
clock_1=clock(23,58,58)

while(True):
    ## 输出现在的时间
    print(clock_1)
    ## 休眠一秒
    time.sleep(1)
    ## 走字一次
    clock_1.runtime()

## eg2：定义一个类描述一个点，要求提供计算到另一个点距离的方法。
import math
## 定义point类
class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def get_dis(self,point):
        x_x=self.x-point.x
        y_y=self.y-point.y
        z_z=self.z-point.z

        ddis=x_x*x_x+y_y*y_y+z_z*z_z
        ddis=abs(ddis**(1/2))
        return ddis


point_1=point(1,1,1)
point_2=point(2,2,2)

dis=point_1.get_dis(point_2)

print(dis)

        
## 简单总结：面向对象编程是一种非常流行的编程范式，除此之外还有**指令式编程**、**函数式编程**等编程范式。
# 由于现实世界是由对象构成的，而对象是可以接收消息的实体，所以**面向对象编程更符合人类正常的思维习惯**。
# 类是抽象的，对象是具体的，有了类就能创建对象，有了对象就可以接收消息，这就是面向对象编程的基础。

## 推荐漫画书：《面向对象分析与设计》