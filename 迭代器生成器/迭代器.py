li = iter([11, 22, 33, 44, 55])  # 首先获得Iterator对象:

print(next(li))
print(next(li))
print(next(li))
print(next(li))
print(next(li))
try:
    print(next(li))
except StopIteration as e:
    print("生成器返回值：", e.value)
'''说明迭代器是没有返回值的'''
# while True:
#     try:
#         x = next(g)
#         print('generator: ',x)
#     except StopIteration as e:
#         print("生成器返回值：",e.value)
#         break