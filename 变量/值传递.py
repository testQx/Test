def f(a, num=0,String="",list=[],tuple=(),set=set(),dict={}):
    b={"num":id(num),"String":id(String),"list":id(list),"tuple":id(tuple),"set":id(set),"dict":id(dict)}
    print(b)
    num=a
    String+=str(a)
    list.append(a)
    tuple=tuple+(a,)
    set.update({a})
    dict.update({"key":a})
    c = {"num": id(num), "String": id(String), "list": id(list), "tuple": id(tuple), "set": id(set), "dict": id(dict)}
    d=["num","String","list","tuple","set","dict"]
    for i in d:
        print(b[f'{i}'])
        print(c[f'{i}'])
        if (b[f'{i}'] == c[f'{i}']):
            print(f'{i}'+"为可变参数，引用传递：被调函数对形参操作为间接寻址，访问影响主调函数的实参；对这个参数实例对象操作，指针指向同一个地址，操作同一个对象")
        else:
            print(f'{i}'+"为不可变参数，值传递：被调函数的形参作局部变量，不影响主调函数的实参；原不可变对象无法改变值，重新开辟新对象的存储地址来操作")
    return c
print(f(1))
# print(f(2))