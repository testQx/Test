'''startswith()方法语法：

str.startswith(str, beg=0,end=len(string));
用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False
'''
str = "this is string example....wow!!!"
print(str.startswith('this'))

'''str.strip([chars])
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
'''

'''str.split(str="", num=string.count(str))
split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
'''

'''str.replace(old, new, max)
replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次'''


'''转换大小写
s.upper() 全大写  s.lower() 全小写
'''