## day_30
## Python中的并发编程
# 现如今，我们使用的计算机早已是多CPU或多核的计算机，为此我们使用的操作系统基本都是支持“多任务”的操作系统，
# 这样的操作系统使得我们我们可以同时运行多个程序，也可以将一个程序分解为若干个相对独立的子任务，让多个子任务“齐头并进”的执行，从而缩短程序的执行时间。
# 因此，当下不管用什么编程语言进行开发，实现让一个程序同时执行多个任务已经成为程序员的标配技能。为此，我们需要先了解两个重要的概念：多进程和多线程。

## 线程和进程
# 我们通过操作系统运行一个程序会创建出一个或多个进程，进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动。简单的说，进程是操作系统分配存储空间的基本单位，每个进程都有自己的地址空间、数据栈以及其他用于跟踪进程执行的辅助数据；操作系统管理所有进程的执行，为它们合理的分配资源。一个进程可以通过fork或spawn的方式创建新的进程来执行其他的任务，不过新的进程也有自己独立的内存空间，因此两个进程如果要共享数据，必须通过进程间通信机制（IPC）来实现，具体的方式包括管道、信号、套接字等。
#
# 一个进程还可以拥有多个并发的执行线索，简单的说就是拥有多个可以获得CPU调度的执行单元，这就是所谓的线程。
# 由于线程在同一个进程下，它们可以共享相同的上下文，因此相对于进程而言，线程间的信息共享和通信更加容易。
# 当然在单核CPU系统中，多个线程不可能同时执行，因为在某个时刻只有一个线程能够获得CPU，多个线程通过共享了CPU执行时间的方式来达到并发的效果。
# 在程序中使用多线程技术通常都会带来不言而喻的好处，最主要的体现在提升程序的性能和改善用户体验，今天我们使用的软件几乎都用到了多线程技术，
# 这一点可以利用系统自带的进程监控工具（如macOS中的“活动监视器”、Windows中的“任务管理器”）来证实。

## 并发和并行
# 另外两个概念：并发（concurrency）和并行（parallel）。
# 并发是指同一时刻只能有一条指令执行，但是多个线程对应的指令被快速轮换地执行。
# 比如一个处理器，它先执行线程 A 的指令一段时间，再执行线程 B 的指令一段时间，再切回到线程 A 执行一段时间。
# 由于处理器执行指令的速度和切换的速度非常非常快，人完全感知不到计算机在这个过程中有多个线程切换上下文执行的操作，这就使得宏观上看起来多个线程在同时运行，
# 但微观上其实只有一个线程在执行。
#
# 并行是指同一时刻，有多条指令在多个处理器上同时执行，并行必须要依赖于多个处理器。不论是从宏观上还是微观上，多个线程都是在同一时刻一起执行的。
# 在我们的课程中，其实并不用严格区分并发和并行两个词，所以我们把Python中的多线程、多进程以及异步I/O都视为实现并发编程的手段，但实际上前面两者也可以实现并行编程。

## 总结：并行和并发都是宏观上的多线程，但是并发是依赖多个线程的指令轮转在CPU上完成，而并行是多个CPU同时处理多个线程的指令。


## 多线程编程
# Python标准库中`threading`模块的`Thread`类可以帮助我们非常轻松的实现多线程编程。
# 直接使用`Thread`类的构造器就可以创建线程对象，而线程对象的`start()`方法可以启动一个线程。
# 线程启动后会执行`target`参数指定的函数，当然前提是获得CPU的调度；如果`target`指定的线程要执行的目标函数有参数，需要通过`args`参数为其进行指定。
#
# 除了上面的创建线程的方式外，还可以通过继承`Thread`类并重写`run()`方法的方式来自定义线程。

# note：如果程序中有非常耗时的执行单元，而这些耗时的执行单元之间又没有逻辑上的因果关系，即B单元的执行不依赖于A单元的执行结果，
# 那么A和B两个单元就可以放到两个不同的线程中，让他们并发的执行。这样做的好处除了减少程序执行的等待时间，还可以带来更好的用户体验，
# 因为一个单元的阻塞不会造成程序的“假死”，因为程序中还有其他的单元是可以运转的。

## 多进程和多线程的比较
# 由于GIL问题，CPython中的多线程是不能很好发挥多核优势的，如果想要发挥多核优势，可以考虑使用多进程。对于多进程的程序，每个进程都有属于自己的GIL，
# 所以多进程不会受GIL的影响，能够很好的发挥多核CPU的优势。对于爬虫这类I/O密集型任务来说，多线程和多进程影响差别并不大。
# 对于计算密集型任务来说，多进程相比多线程，在效率上会有成倍的提升。

"""
time python3 example22.py
real    0m11.512s
user    0m39.319s
sys     0m0.169s
使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
"""
import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5

def is_prime(n):
    """判断素数"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    """主函数"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()

## 总结：多线程vs.多进程
# 对于Python开发者来说，以下情况需要考虑使用多线程：
# 1. 程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
# 2. 程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。
#
# 那么在遇到下列情况时，应该考虑使用多进程：
# 1. 程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
# 2. 程序的输入可以并行的分成块，并且可以将运算结果合并。
# 3. 程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。