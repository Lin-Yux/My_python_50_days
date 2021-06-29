## day_16
## 面向对象编程进阶

## 可见性和属性装饰器
# 在很多面向对象编程语言中，对象的属性通常会被设置为私有（private）或受保护（protected）的成员，简单的说就是不允许直接访问这些属性；
# 对象的方法通常都是公开的（public），因为公开的方法是对象能够接受的消息，也是对象暴露给外界的调用接口，这就是所谓的访问可见性。
# 在Python中，可以通过给对象属性名添加前缀下划线的方式来说明属性的访问可见性：
# 例如，可以用`__name`（两个下划线）表示一个私有属性，`_name`（一个下划线）表示一个受保护属性。
class Student:
    def __init__(self,name,age):
        self.__name=name
        self._age=age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.') ## 在类的定义过程中，对象的方法可以通过self.__name调用私有属性

stu = Student('王大锤', 20)
stu.study('Python程序设计')
print(stu.__name) ## AttributeError: 'Student' object has no attribute '__name'
print(stu._age) ## 20

# 以`__`开头的属性`__name`是私有的，在类的外面无法直接访问，但是类里面的`study`方法中可以通过`self.__name`访问该属性。

# Python并没有从语法上严格保证私有属性的私密性，它只是给私有的属性和方法换了一个名字来阻挠对它们的访问，
# 事实上如果你知道更换名字的规则仍然可以访问到它们，我们可以对上面的代码稍作修改就可以访问到私有的。
print(stu._Student__name) ## 我们通过   对象._类名__私有属性 这样的方式就可以访问到私有属性

## 装饰器
# Python中可以通过`property`装饰器为“私有”属性提供读取和修改的方法。
# 装饰器通常会放在类、函数或方法的声明之前，通过一个`@`符号表示将装饰器应用于类、函数或方法。
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property ## 属性访问器(getter方法)，如果调用了.name，就会调用这个方法，返回self.__name这个私有属性
    def name(self):
        return self.__name

    @property ## 同上，属性访问器  
    def age(self):
        return self.__age
    
    @name.setter ## 属性修改器(setter方法)，修改__name属性
    def name(self,name):
        # 如果name参数不为空就赋值给对象的__name属性
        # 否则将__name属性赋值为'无名氏'，有两种写法
        # self.__name = name if name else '无名氏'
        self.__name = name or "无名" ## 注意这里要赋给私有属性
    
stu = Student('王大锤', 20)
print(stu.name, stu.age)    ## 王大锤 20，这里就能够访问我们之前的私有属性了，因为我们用装饰器做了一个方法来调用

stu.name = '' ## 修改私有属性
print(stu.name)    ## 无名氏

stu.age = 30 ## AttributeError: can't set attribute，不能修改私有属性

## note：在实际项目开发中，我们并不经常使用私有属性，属性装饰器的使用也比较少，上面仅供了解。

## 动态属性
# Python是一门动态语言，Ruby,Javascript都是动态语言。c,cpp是静态语言。
# Python中，我们可以动态为对象添加属性，这是Python作为动态类型语言的一个特点。
# 需要提醒大家的是，对象的方法其实本质上也是对象的属性，如果给对象发送一个无法接收的消息，引发的异常仍然是`AttributeError`。（attribute,属性）
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

stu = Student('王大锤', 20)
# 为Student对象动态添加sex属性
stu.sex = '男'
print(stu.sex) ## 男

# 如果不希望使用对象时动态的为对象添加属性，可以使用Python的`__slots__`方法。
# 对于`Student`类来说，可以在类中指定`__slots__ = ('name', 'age')`，这样`Student`类的对象只能有`name`和`age`属性。
# 如果想动态添加其他属性将会引发异常。

class Student:
    __slots__=("name","age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('王大锤', 20)

stu.sex = '男' ## AttributeError: 'Student' object has no attribute 'sex'，此时我们就不允许在调用对象时动态地增加属性

## 静态方法和类方法
# 之前我们在类中定义的方法都是对象方法，换句话说这些方法都是对象可以接收的消息。
# 除了对象方法之外，类中还可以有静态方法和类方法，这两类方法是发给类的消息，二者并没有实质性的区别。
# 在面向对象编程中，一切皆为对象，定义的类也是一个对象，而静态方法和类方法就是发送给类对象的消息。

# 举一个例子，定义一个三角形类，通过传入三条边的长度来构造三角形，并提供计算周长和面积的方法。
# 计算周长和面积是三角形对象的方法。
# 但在创建三角形对象时，传入的三条边长未必能构造出三角形，为此我们可以先写一个方法来验证给定的三条边长是否可以构成三角形，
# 这种方法很显然就不是对象方法，因为在调用这个方法时三角形对象还没有创建出来。
# 我们可以把这类方法设计为静态方法或类方法，也就是说这类方法不是发送给三角形对象的消息，而是发送给三角形类的消息。


## 个人总结概括：方法是对象调用的，静态方法和类方法是对象还没创建的时候，就可以通过类来调用的方法。
class Triangle:
    def __init__(self,a,b,c): ## 初始化
        self.a=a
        self.b=b
        self.c=c
    
    @staticmethod ## 静态方法staticmethod
    def is_valid_staticmethod(a,b,c):
        return a+b>c and b+c>a and a+c>b
    
    
    @classmethod ## 类方法classmethod
    def is_valid_classmethod(self,a,b,c): ## 这里的self是指类本身，而不是属于这个类的对象
        return a+b>c and b+c>a and a+c>b
    

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

t1=Triangle(1,2,3) ## 创建Triangle对象t1

print(Triangle.is_valid_staticmethod(1,2,3)) ## False，调用静态方法
print(Triangle.is_valid_classmethod(1,2,3)) ## False，调用类方法，这里的参数虽然和上面一样，但是实际上还隐藏了一个参数self指类本身

print(t1.is_valid) ## <function Triangle.is_valid at 0x000001C802F80F70>

# 上面的代码使用`staticmethod`装饰器声明了`is_valid`方法是`Triangle`类的静态方法，如果要声明类方法，可以使用`classmethod`装饰器。
# 可以直接使用`类名.方法名`的方式来调用静态方法和类方法。二者的区别在于：
# 类方法的第一个参数是类对象本身，而静态方法则没有这个参数。

# 简单的总结一下：
# ①对象方法、类方法、静态方法都可以通过`类名.方法名`的方式来调用。
# ②不同之处在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象。
# ③静态方法通常也可以直接写成一个独立的函数，因为它并没有跟特定的对象绑定。

## 继承
# 面向对象的编程语言支持在已有类的基础上创建新类，从而减少重复代码的编写。
# 提供继承信息的类叫做父类（超类、基类），得到继承信息的类叫做子类（派生类、衍生类）。
# 例如，我们定义一个学生类和一个老师类，我们会发现他们有大量的重复代码，而这些重复代码都是老师和学生作为人的公共属性和行为，
# 所以在这种情况下，我们应该先定义人类，再通过继承，从人类派生出老师类和学生类，代码如下所示。
class Person: ## 定义Person这个类
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}正在吃饭.')
    
    def sleep(self):
        print(f'{self.name}正在睡觉.')

class Student(Person): ## 定义Student作为Person的子类
    def __init__(self,name,age):
        super().__init__(name,age) ## super()指父类，调用.__init__(name,age)方法来直接对子类进行初始化
        # super(Student,self).__init__(name,age) 这么写也可以 

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

class Teacher(Person): ## 定义教师类，作为Person的子类
    def __init__(self, name, age,title):
        super().__init__(name, age)
        self.title=title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')

stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
teacher = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
teacher.teach('Python程序设计')
stu1.study('Python程序设计')

# 继承的语法是在定义类的时候，在类名后的圆括号中指定当前类的父类。如果定义一个类的时候没有指定它的父类是谁，那么默认的父类是`object`类。
# `object`类是Python中的顶级类，这也就意味着所有的类都是它的子类，要么直接继承它，要么间接继承它。

# Python语言允许多重继承，也就是说一个类可以有一个或多个父类。
# 在子类的初始化方法中，我们可以通过`super().__init__()`来调用父类初始化方法，`super()`函数是Python内置函数中专门为获取当前对象的父类对象而设计的。
# 从上面的代码可以看出，子类除了可以通过继承得到父类提供的属性和方法外，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力。
# 在实际开发中，我们经常会用子类对象去替换掉一个父类对象，在面向对象编程中很常见，也叫做“里氏替换原则”（Liskov Substitution Principle）。

# 子类继承父类的方法后，还可以对方法进行重写
# 不同的子类可以对父类的同一个方法给出不同的实现版本，这样的方法在程序运行时就会表现出多态行为。（调用相同的方法，做了不同的事情）。
# 多态是面向对象编程中最精髓的部分，当然也是对初学者来说最难以理解和灵活运用的部分。