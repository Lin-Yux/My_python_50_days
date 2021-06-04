## 字符串

## 字符串定义：零个或多个字符组成的有限序列，eg:
s1="hello world!"
s2='hello world!!'
s3='''
hello world!!!
'''
## 之前有个地方理解错误了，三个'开头是字符串，不是注释，注释是三个"
"""
注释
"""
print(s1,s2,s3) ## 逗号隔开默认是用空格来隔开
## 输出
## hello world! hello world!! 
## hello world
## 注意到这里虽然s3被输出了，但是是换行输出的，所以可能默认了中间有个\n换行符
## print()里面有个参数，end=''，表示输出后以什么结尾，缺省的话为'\t'

## 转义字符和原始字符串
## 同C语言，用\（反斜杠）来表示转义。如果想要表示一个特殊字符比如'（单引号）"（双引号）\（反斜杠）就需要应用\来转义
print("test\"") ## test"
print("test\\") ## test\
print("test\'") ## test'

## notice：python有一类特殊定义，就是字符串如果是r或者是R开头，就是被称为原始字符串，字符串中的每个字符都是它本来的含义，没有所谓的转义字符。
## eg：
print("s1\n",r"s2\n")  ## 这里感觉跟前面print(f(……{变量}……｝))有异曲同工之妙

## python还允许\后面跟八进制或者十六进制数来表示字符
print('\141')
print('\141\142\143\x61\x62\x63')

## 字符串运算
## +和*
print("hello"+"world") ## 输出中间是没有空格的
print('!'*3) ## `*`实现字符串的重复

## 比较
print("a"=="a")
s1 = 'a whole new world'
s2 = 'hello world'
print(s1==s2,s1<s2)
a=ord('尤')
b=ord('昀')
c=ord('颖') ## ord()可以输出字符串对应的十六进制数，里面不能放变量，字符串，只能放字符
print(a,b,c)

#notice："=="可以用来判断两个字符串内容(值)是否相等，"is"比较的是两个变量对应的字符串是否在内存中相同的位置（内存地址）
# 用id()可以输出一个变量的地址
s1="1000"
s2="1000" 
s3=s2
print(s1==s2,s2==s3)
print(s1 is s2,s2 is s3)  ## 照理说这里应该输出一个F，一个T，但是输出两个T，
## 原因：python对小整数在内存中直接创建了一份，不会回收，所有创建的小整数变量直接从对象池中引用他即可，
## 但是注意Python仅仅对比较小的整数对象进行缓存（范围为范围[-5, 256]）缓存起来，而并非是所有整数对象。
## 也就说只有在这个[-5,256]范围内创建的变量值使用is比较时候才会成立。
## 但是对于一些解释器比如说pycharm/VScode来说，即使超过这个范围也没事
# ref:https://blog.csdn.net/qq_26442553/article/details/82195061
print(id(s1),id(s2),id(s3))

## in
s1="hello world"
s2="hello"
print(s2 in s1)

## len()，相当于R的length()
s1="hello world"
print(len(s1))

## 索引,[]，可以把一个字符串理解成一个字符数组
# 下标从0开始
s1="hello world"
print(len(s1))
print(s1[4]) ## 正向索引
print(s1[-1]) ## 负向索引，-1是字符串的最后一个
## 如果索引越界，会报错

## 切片
# `[i:j:k]`，其中`i`是开始索引，索引对应的字符可以取到；
# `j`是结束索引，索引对应的字符不能取到；
# `k`是步长，默认值为`1`，表示从前向后获取相邻字符的连续切片，所以`:k`部分可以省略

# `k > 0`时表示正向切片（从前向后获取字符），
# 如果没有给出`i`和`j`的值，则`i`的默认值是`0`，`j`的默认值是`N`；
# 当`k < 0`时表示负向切片（从后向前获取字符），
# 如果没有给出`i`和`j`的值，则`i`的默认值是`-1`，j的默认值是`-N - 1`
s="abc123456"
print(s[2:5:]) ## 左闭右开,即[2,5)，正向索引
print(s[-7:-4:]) ## 左开右闭,(-7,-4]，不用强行去记，因为不管是对于正索引还是负索引，下标都是从0开始的，所以开闭会不一样
print(s[7:4:-1]) ## 左闭右开,(4,7]，逆向切片，所以输出是倒着输出的，所以字符串翻转就很容易，直接[,,-1]就行了
## 还有很多例子，就不一个个尝试了，了解索引下标是从0开始，[i:j:k]可以实现切片,i,j,k分别对应起点，终点，步长（方向）就可以了
"""
s = 'abc123456'

# i=2, j=5, k=1的正向切片操作
print(s[2:5])       # c12

# i=-7, j=-4, k=1的正向切片操作
print(s[-7:-4])     # c12

# i=2, j=9, k=1的正向切片操作
print(s[2:])        # c123456

# i=-7, j=9, k=1的正向切片操作
print(s[-7:])       # c123456

# i=2, j=9, k=2的正向切片操作
print(s[2::2])      # c246

# i=-7, j=9, k=2的正向切片操作
print(s[-7::2])     # c246

# i=0, j=9, k=2的正向切片操作
print(s[::2])       # ac246

# i=1, j=-1, k=2的正向切片操作
print(s[1:-1:2])    # b135

# i=7, j=1, k=-1的负向切片操作
print(s[7:1:-1])    # 54321c

# i=-2, j=-8, k=-1的负向切片操作
print(s[-2:-8:-1])  # 54321c

# i=7, j=-10, k=-1的负向切片操作
print(s[7::-1])     # 54321cba

# i=-1, j=1, k=-1的负向切片操作
print(s[:1:-1])     # 654321c

# i=0, j=9, k=1的正向切片
print(s[:])         # abc123456

# i=0, j=9, k=2的正向切片
print(s[::2])       # ac246

# i=-1, j=-10, k=-1的负向切片
print(s[::-1])      # 654321cba

# i=-1, j=-10, k=-2的负向切片
print(s[::-2])      # 642ca
"""

## 字符串的循环遍历
# eg1:通过下标
s1="hello world"
for i in range(0,len(s1)): ## range(5)=range(0,5) range是用来生成一个自然数数列，是range类型
    print(s1[i],end='\t')
# eg2:通过字符直接索引，这里就是可以理解Python里面的字符串相当于一个数组了
s2="Hi world"
for i in s2:
    print(i,end='\t')

## 字符串类型自带的处理方法
# 对于一个字符串类型的变量，我们可以用`变量名.方法名()`的方式来调用它的方法
# 方法其实就是跟某个类型的变量绑定的函数（面向对象编程）
# 简单来说，就是对于每一个特定的类型（class），都可以定义一系列的针对它的方法，使用的时候就直接 变量.方法()，这里的方法其实就是函数，所以要记得有()
s1='hello, world!'
print(s1.capitalize()) ## capitalize，首字母大写化
print(s1.title())  ## 每个单词首字母大写，像title一样
print(s1.upper()) ## 所有字母大写，upper
print((s1.upper()).lower()) ## 先大写再小写,lower

## 查找字符串，和前面的in一起，find，index
s = 'hello, world!'
# find方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串中另一个字符串首字符的索引
print(s.find("or")) ## 返回or中前面那个，即'o'的索引
print(s.find('oro')) ## 找不到返回-1

## index和find一模一样
print(s.find('o',2)) ## .find(pattern,从第几个字符开始)
print(s.rfind('o')) ## .rfind()逆向查找，这里意思是找最后一个o，一样可以在里面加一个数字表示从第几个字符开始，不过尽量别这么用，容易错

## 性质判断：startwith endwith 
# 顾名思义，就是判断是不是从某个字母、字符串开头，再配合in也能知道字符串里有没有这个东西
s1 = 'hello, world!'
print(s1.startswith('h'))
print(s1.endswith('d'))

print(s1.isdigit()) ##是不是数字
print(s1.isalpha()) ## alpha() 字母
print(s1.isalnum()) ## 是不是数字字母组成


## 调整字符串格式 center ljust rjust（居中，左对齐，右对齐）
s = 'hello, world'
print(s.center(20,'+')) ## 将s填充成长度为20的字符串，用+来填充，并且居中字符串s
print(s.ljust(20,'-'))
print(s.rjust(20,'*'))

## print()时输出变量所代替的值
#eg1: 利用 %d和%
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
#eg2：python3.6后用前面加f（day_4就有用到）
print(f'{a}*{b}={a*b}') ## 前面加f,里面就可以｛变量｝

## 进一步调整格式，比如说小数的位数，就在print(f"{变量:……}")，即在变量的后面加一个:然后对应进行操作
"""
| 变量值      | 占位符     | 格式化结果      | 说明                   |
| ----------- | ---------- | --------------- | ---------------------- |
| `3.1415926` | `{:.2f}`   | `'3.14'`        | 保留小数点后两位       |
| `3.1415926` | `{:+.2f}`  | `'+3.14'`       | 带符号保留小数点后两位 |
| `-1`        | `{:+.2f}`  | `'-1.00'`       | 带符号保留小数点后两位 |
| `3.1415926` | `{:.0f}`   | `'3'`           | 不带小数               |
| `123`       | `{:0>10d}` | `0000000123`    | 左边补`0`，补够10位    |
| `123`       | `{:x<10d}` | `123xxxxxxx`    | 右边补`x` ，补够10位   |
| `123`       | `{:>10d}`  | `'       123'`  | 左边补空格，补够10位   |
| `123`       | `{:<10d}`  | `'123       '`  | 右边补空格，补够10位   |
| `123456789` | `{:,}`     | `'123,456,789'` | 逗号分隔格式           |
| `0.123`     | `{:.2%}`   | `'12.30%'`      | 百分比格式             |
| `123456789` | `{:.2e}`   | `'1.23e+08'`    | 科学计数法格式         |
"""
a=3.14
b=9.526
c=111
d=123456789
print(f"{a*b:.2f}") ## 控制输出两位小数 {:f}表示是针对浮点数的操纵，{:d}表示是针对整数的操作，注意数据类型
print(f"{c:0<10d}") ## 这只是变换了输出，本质上c的大小其实是不变的
print(f"{d:,}") ## 控制按k m b区分

## 修剪操作 strip（lstrip,rstrip）
# 帮我们获得将原字符串修剪掉左右两端空格之后的字符串，这个感觉还挺有趣的
s="     emailaddress@email  "
print(s)
print(s.strip())
print(s.rstrip())

## 本节课重点：①定义一个类的方法的时候，可以通过 变量.方法（）来引用 ————注意这个方法一定得是针对这个类的
## python的下标也是从0开始