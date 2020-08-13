import time


def consumer(name):
    print("%s 准备学习啦!" % name)
    while True:
        lesson = yield

        print("开始[%s]了,[%s]老师来讲课了!" % (lesson, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("同学们开始上课 了!")
    for i in range(10):
        time.sleep(1)
        print("到了两个同学!")
        c.send(i)
        c2.send(i)
producer("测试")
#send()和next()的区别就在于send可传递参数给yield表达式，这时候传递的参数就会作为yield表达式的值，而yield的参数是返回给调用者的值，也就是说send可以强行修改上一个yield表达式值。
#第一次调用时候必须先next（）或send（）,否则会报错，send后之所以为None是因为这时候没有上一个yield，所以也可以认为next（）等同于send(None)