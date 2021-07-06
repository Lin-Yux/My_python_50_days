## day_21
## 文件读写和异常处理
# 实际开发中需要对数据进行持久化，就是将数据从无法长久保存数据的存储介质（通常是内存）转移到可以长久保存数据的存储介质（通常是硬盘）中。
# 实现数据持久化最直接简单的方式就是通过文件系统将数据保存到文件中。
#
# 计算机的文件系统是一种存储和组织计算机数据的方法，它使得对数据的访问和查找变得容易，
# 文件系统使用文件和树形目录的抽象逻辑概念代替了硬盘、光盘、闪存等物理设备的数据块概念，
# 用户使用文件系统来保存数据时，不必关心数据实际保存在硬盘的哪个数据块上，只需要记住这个文件的路径和文件名。
# 在写入新数据之前，用户不必关心硬盘上的哪个数据块没有被使用，硬盘上的存储空间管理（分配和释放）功能由文件系统自动完成，用户只需要记住数据被写入到了哪个文件中。

## 打开和关闭文件
# Python内置的`open`函数来打开文件，在使用`open`函数时，我们可以通过函数的参数指定文件名、操作模式和字符编码等信息，就可以对文件进行读写操作了。
# 这里所说的操作模式是指要打开什么样的文件（字符文件或二进制文件）以及做什么样的操作（读、写或追加），具体如下表所示。
# | 操作模式 | 具体含义                         |
# | -------- | -------------------------------- |
# | `'r'`    | 读取 （默认）                    |
# | `'w'`    | 写入（会先截断之前的内容）       |
# | `'x'`    | 写入，如果文件已经存在会产生异常 |
# | `'a'`    | 追加，将内容写入到已有文件的末尾 |
# | `'b'`    | 二进制模式                       |
# | `'t'`    | 文本模式（默认）                 |
# | `'+'`    | 更新（既可以读又可以写）         |

# 使用`open`函数时，如果打开的文件是字符文件（文本文件），可以通过`encoding`参数来指定读写文件使用的字符编码。
# 如果对字符编码和字符集这些概念不了解，可以看看[《字符集和字符编码》](https://www.cnblogs.com/skynet/archive/2011/05/03/2035105.html)
# 如果没有指定该参数，则使用系统默认的编码作为读写文件的编码。

## 获取当前系统默认的编码
import sys
print(sys.getdefaultencoding()) ## utf-8

# 使用`open`函数打开文件成功后会返回一个文件对象，通过这个对象，我们就可以实现对文件的读写操作；
# 如果打开文件失败，`open`函数会引发异常。
# 如果要关闭打开的文件，可以使用文件对象的`close`方法，这样可以在结束文件操作时释放掉这个文件。

## 读写文本文件
# 用`open`函数打开文本文件时，需要指定文件名并将文件的操作模式设置为`'r'`，如果不指定，默认值也是`'r'`；
# 如果需要指定字符编码，可以传入`encoding`参数，如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码。
# 保证保存文件时使用的编码方式与`encoding`参数指定的编码方式是一致的。

## 直接读取整个文本文件
file = open('E:\Python-Core-50-Courses\致橡树.txt', 'r', encoding='utf-8') ## 同R,python读取文件依然要带路径，Windows下最好用'\\'来划分路径和文件名
print(file.read())
file.close()

## 逐行读取文件
# 使用`for-in`循环逐行读取
import time

file = open('E:\Python-Core-50-Courses\致橡树.txt', 'r', encoding='utf-8')
for line in file:
    print(line, end='')
    time.sleep(0.5) ## 每输出一行都暂停0.5秒
file.close()

# `readlines`方法将文件按行读取到一个列表容器
file = open('E:\Python-Core-50-Courses\致橡树.txt', 'r', encoding='utf-8')
lines = file.readlines() ## 返回一个list对象
for line in lines:
    print(line, end='')
    time.sleep(0.5)
file.close()

## 写入内容
# 如果要向文件中写入内容，可以在打开文件时使用`w`（写入）或者`a`（追加）作为操作模式，前者会截断之前的文本内容写入新的内容，后者是在原来内容的尾部追加新的内容。
file = open('E:\Python-Core-50-Courses\致橡树.txt', 'a', encoding='utf-8')
file.write('\n标题：《致橡树》')
file.write('\n作者：舒婷')
file.write('\n时间：1977年3月')
file.close()

# 利用for-in来写入多行
lines = ['标题：《致橡树》', '作者：舒婷', '时间：1977年3月']
file = open('致橡树.txt', 'a', encoding='utf-8')
for line in lines:
    file.write(f'\n{line}')
file.close()

## 异常处理机制
# 请注意上面的代码，如果`open`函数指定的文件并不存在或者无法打开，那么将引发异常状况导致程序崩溃。
# 为了让代码具有健壮性和容错性，我们使用Python的异常机制对可能在运行时发生状况的代码进行适当的处理。
# Python中和异常相关的关键字有五个，分别是`try`、`except`、`else`、`finally`和`raise`。

file = None
try:
    file = open('致橡树.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
finally:
    if file:
        file.close()

# 在Python中，我们可以将运行时会出现状况的代码放在`try`代码块中，在`try`后面可以跟上一个或多个`except`块来捕获异常并进行相应的处理。
# 例如，在上面的代码中，文件找不到会引发`FileNotFoundError`，指定了未知的编码会引发`LookupError`，
# 而如果读取文件时无法按指定编码方式解码文件会引发`UnicodeDecodeError`，所以我们在`try`后面跟上了三个`except`分别处理这三种不同的异常状况。
# 在`except`后面，我们还可以加上`else`代码块，这是`try` 中的代码没有出现异常时会执行的代码，而且`else`中的代码不会再进行异常捕获，
# 也就是说如果遇到异常状况，程序会因异常而终止并报告异常信息。
# 最后我们使用`finally`代码块来关闭打开的文件，释放掉程序中获取的外部资源。
# 由于`finally`块的代码不论程序正常还是异常都会执行，甚至是调用了`sys`模块的`exit`函数终止Python程序，
# `finally`块中的代码仍然会被执行（因为`exit`函数的本质是引发了`SystemExit`异常），因此我们把`finally`代码块称为“总是执行代码块”，它最适合用来做释放外部资源的操作。

## python内置的异常类型，下面是继承结构图
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning

# 从上面的继承结构可以看出，Python中所有的异常都是`BaseException`的子类型，
# 它有四个直接的子类，分别是：`SystemExit`、`KeyboardInterrupt`、`GeneratorExit`和`Exception`。
# 其中，`SystemExit`表示解释器请求退出，`KeyboardInterrupt`是用户中断程序执行（按下`Ctrl+c`），
# `GeneratorExit`表示生成器发生异常通知退出。
# 值得一提的是`Exception`类，它是常规异常类型的父类型，很多的异常都是直接或间接的继承自`Exception`类。
# 如果Python内置的异常类型不能满足应用程序的需要，我们可以自定义异常类型，而自定义的异常类型也应该直接或间接继承自`Exception`类，
# 当然还可以根据需要重写或添加方法。

# 在Python中，可以使用`raise`关键字来引发异常（抛出异常对象），而调用者可以通过`try...except...`结构来捕获并处理异常。
# 例如在函数中，当函数的执行条件不满足时，可以使用抛出异常的方式来告知调用者问题的所在，
# 而调用者可以通过捕获处理异常来使得代码从异常中恢复，定义异常和抛出异常的代码如下所示。
class InputError(ValueError):
    """自定义异常类型"""
    pass

def fac(num):
    """求阶乘"""
    if type(num) != int or num < 0:
        raise InputError('只能计算非负整数的阶乘！！！')
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

# 调用求阶乘的函数`fac`，通过`try...except...`结构捕获输入错误的异常并打印异常对象（显示异常信息），如果输入正确就计算阶乘并结束程序。
flag=True
while flag:
    num=int(input('n='))
    try:
        print(f"{num}!={fac(num)}")
        flag=False
    except InputError as err:
        print(err)

## 上下文语法
# 对于`open`函数返回的文件对象，还可以使用`with`上下文语法在文件操作完成后自动执行文件对象的`close`方法，这样可以让代码变得更加简单，
# 因为不需要再写`finally`代码块来执行关闭文件释放资源的操作。需要提醒大家的是，
# 并不是所有的对象都可以放在`with`上下文语法中，只有符合**上下文管理器协议**（有`__enter__`和`__exit__`魔术方法）的对象才能使用这种语法，
# Python标准库中的`contextlib`模块也提供了对`with`上下文语法的支持。
try:
    with open('致橡树.txt', 'r', encoding='utf-8') as file: ## 如果with open，之后就不需要再close文件，但是只有有__enter__和__exit__魔术方法的对象才能用这种上下文语法
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
## 不需要finally:
#           file.close()

## 读写二进制文件（图片）
# 读写二进制文件跟读写文本文件的操作类似，但是需要注意，在使用`open`函数打开文件时，如果要进行读操作，操作模式是`'rb'`，如果要进行写操作，操作模式是`'wb'`。
# 还有一点，读写文本文件时，`read`方法的返回值以及`write`方法的参数是`str`对象（字符串），
# 而读写二进制文件时，`read`方法的返回值以及`write`方法的参数是`bytes-like`对象（字节串）。
# 下面的代码实现了将当前路径下名为`guido.jpg`的图片文件复制到`吉多.jpg`文件中的操作。
try:
    with open('E:\\Python-Core-50-Courses\\a.jpg','rb') as file_1:
        data=file_1.read()
    with open('E:\\Python-Core-50-Courses\\b.bmp','wb') as file_2: ## 这里要注意一点，路径和文件名直接要用\\来分隔，具体看Pycharm给的提示。
        file_2.write(data)
except FileNotFoundError:
    print("文件不存在")
except IOError:
    print("文件读写错误")
print("文件读写结束")

## 如果要复制的图片文件很大，一次将文件内容直接读入内存中可能会造成非常大的内存开销，为了减少对内存的占用，
# 可以为`read`方法传入`size`参数来指定每次读取的字节数，通过循环读取和写入的方式来完成上面的操作，代码如下所示。

try:
    with open('E:\\Python-Core-50-Courses\\a.jpg', 'rb') as file1, \
        open('E:\\Python-Core-50-Courses\\b.bmp', 'wb') as file2:
        data = file1.read(512) ## 指定读取的字节数
        while data:
            file2.write(data)
            data = file1.read()
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')

# 总结：通过读写文件的操作，我们可以实现数据持久化。
# 在Python中可以通过`open`函数来获得文件对象，可以通过文件对象的`read`和`write`方法实现文件读写操作。
#
# 程序在运行时可能遭遇无法预料的异常状况，可以使用Python的异常机制来处理这些状况。
# Python的异常机制主要包括`try`、`except`、`else`、`finally`和`raise`这五个核心关键字。
# `try`后面的`except`语句不是必须的，`finally`语句也不是必须的，但是二者必须要有一个；
# `except`语句可以有一个或多个，多个`except`会按照书写的顺序依次匹配指定的异常，如果异常已经处理就不会再进入后续的`except`语句；
# `except`语句中还可以通过元组同时指定多个异常类型进行捕获；`except`语句后面如果不指定异常类型，则默认捕获所有异常；
# 捕获异常后可以使用`raise`再次抛出，但是不建议捕获并抛出同一个异常；不建议在不清楚逻辑的情况下捕获所有异常，这可能会掩盖程序中严重的问题。
# 最后强调一点，不要使用异常机制来处理正常业务逻辑或控制程序流程，简单的说就是不要滥用异常机制。