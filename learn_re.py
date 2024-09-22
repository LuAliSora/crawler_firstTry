# import re

# print(re.match('www','www.baidu.com').span())
# print(re.match('baidu','www.baidu.com'))

# print(re.search('www','www.baidu.com'))
# print(re.search('baidu','www.baidu.com',flags=re.I))

# print(re.findall(pattern='\d+', string='abafa 124ddwa56'))

# mat=re.compile(r'\d+')#匹配数字

# print(mat.findall('abafa 124ddwa56'))
# print(mat.findall('abafa 124ddwa56',0,7))#匹配从0位开始，到7位结束

# it = re.finditer(r"\d+", "12a32bc43jf3")
# for match in it:
#     print(match.group(),match.group())

# print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.groups())
    

# phone = "2004-959-559 # 这是一个电话号码"

# # 删除注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码 : ", num)

# 移除非数字的内容
# num = re.sub(r'\D', "", phone)
# print("电话号码 : ", num)

# 将匹配的数字乘于 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
 
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))

# p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
# print(p.search('Paris in the the spring').group())

# print(re.match(r'^(\d+?)(0*)$', '102300').groups())


# # 正确的理解思路：如果在第⼀对<>中是什么，按理说在后⾯的那对<>中就应该是什么。通过引⽤分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式。
# ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
# # 因为2对<>中的数据不⼀致，所以没有匹配出来
# test_label = ["<html>hh</html>","<html>hh</htmlbalabala>"]
# for label in test_label:
#     ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", label)
#     if ret:
#         print("%s 这是一对正确的标签" % ret.group())
#     else:
#         print("%s 这是⼀对不正确的标签" % label)

        