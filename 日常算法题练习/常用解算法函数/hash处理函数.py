# collections在python官方文档中的解释是High-performance container datatypes，直接的中文翻译解释高性能容量数据类型。
# 统计词频
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
result = {}
for color in colors:
    if result.get(color) == None:
        result[color] = 1
    else:
        result[color] += 1
print(result)

from collections import Counter

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print(dict(c))
