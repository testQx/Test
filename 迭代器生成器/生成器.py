info = [55, 44, 222, 33, 14, 55, 64, 37, 28, 19]
b = []
for index,i in enumerate(info):
    #emumerate函数用于将一个可遍历的数据对象组合成一个索引序列，同时列出数据和数据下标
    print(index,",",i,end="|")
    info[index] +=1
print('\n',info)
print("*"*30)

info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = map(lambda x:x*10,info)
for i in a:
    print(i,end=" ")
print('\n',"*"*30)

info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [i*99 for i in range(10)]
print(a)
print("*"*30)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
a = fib(10)
print(a.__next__())
for i in fib(6):
    print(i,end=" ")
print('\n',"*"*30)

#想通过生成器获取返回值，则必须抓捕"StopIteration"错误，返回值在StopIteration的value中
def fib(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b =b,a+b
        n = n+1
    return 'done'
g = fib(6)
#此时的g为一个迭代器
print(g)
while True:
    try:
        x = next(g)
        print('generator: ',x)
    except StopIteration as e:
        print("生成器返回值：",e.value)
        break

