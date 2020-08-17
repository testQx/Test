import re

'''re.match函数
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。'''
print(re.match('www', 'www.runoob.com').span())
# span函数指返回一个元组
print("*" * 30)
'''re.search方法
re.search 扫描整个字符串并返回第一个成功的匹配。'''
print(re.search('www', 'www.www.com').span())
print("*" * 30)
'''我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。'''

'''re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。'''
line = "Cats are smarter than dogs";

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")
matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> searchObj.group() : ", matchObj.group())
else:
    print("No match!!")
print("*" * 30)

'''re.sub用于替换字符串中的匹配项
re.sub(pattern, repl, string, count=0)
repl : 替换的字符串，也可为一个函数,count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配'''

'''re.compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用'''
pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print(m)
print("*" * 30)
'''findall
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。'''
pattern = re.compile(r'\d+')  # 查找数字
print(pattern.findall('runoob 123 google 456'))
print("*" * 30)
'''re.split
split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下
re.split(pattern, string[, maxsplit=0, flags=0])
maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。'''
print(re.split('\W+', 'runoob, runoob, runoob.',maxsplit=2))
print("*" * 30)
'''常用正则表达式
rub[ye]	匹配 "ruby" 或 "rube" ，即[]指匹配[]中的任意一个字母/数字等
[a-zA-Z0-9]	匹配任何字母及数字
'''
