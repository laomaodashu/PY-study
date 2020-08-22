'''
print('你好') #字符串
print('WTF')
print(2333)
print(2.3333)
print(True)
print(666)
print("haha"+"xixi")

print('哈哈')
print('哈哈'*100)
print('嘿嘿',2333,2.333)
print(1+2)
print(((1+2)*100-9.9)/2)
print(2<3)

name = '张三'
print(name)
'''


# a = float(input('请输入：'))
# b = float(input('请输入：'))
# print('input获取的内容：',int(a+b))


# c = type(2333)
# print(c)

# print(type(True))
# print(type([]))

# a = str('2333')
# print(type(a))

# a = '我操'
# print(len(a))


# a = input('请输入内容一：')
# b = input('请输入内容二：')
# print('您输入的第一段内容是:',a)
# print('您输入的第一段内容的字符长度为：',len(a))
# print('您输入的第一段内容是:',b)
# print('您输入的第一段内容的字符长度为：',len(b))
# print('您输入的两段内容的字符长度之和为：',len(a+b))

# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)
# print(a)
# print(a[-2])
# print(a[0:4])
# print(a[4:7])
# print(a[9:])
# print(a[:4])
# # print(a.index('嘻嘻'))
# # print(a.count('哈哈'))

# # b = (a,'哈哈哈','嘻嘻嘻')
# # # print(b[0][3])

# a = [1,2,3,4,"哈哈","嘻嘻",True,False]
# print(a)
# print(a[4])
# a.append('append1')
# a.append('append2')
# a.insert(0,'insert')
# b = a.pop(4)
# c = a.pop(1)
# print(a)
# print(b)
# print(b+c)
# # a.clear()
# xx = ['你好','不好']
# a.extend(xx)
# print(a)
# print(a+xx)
# a.remove('嘻嘻')
# print(a)

# a = {"name":"张三",9:'哈哈','age':25}
# print(a['name'])
# print(a['age'])
# a['High'] = '183cm'
# print(a)
# a['name'] = '李四'
# print(a)

# b = a.get('name')
# print(b)
# b = a.pop('name')
# print(b)
# print(a)
# a.update(name=1111)
# print(a)
# del a['name']
# print(a)
# del a[9]
# print(a)

name = input('请输入您的姓名：')
age = input('请输入您的年龄：')
sex = input('请输入您的性别：')
print(' ')
print('*****我是华丽的分割线*****')
print(' ')
print('您的姓名是：',name)
print('您的年龄是：',age)
print('您的性别是：',sex)
zidian1 = {'姓名':name,'年龄':age,'性别':sex}
print(' ')
print('*****我是华丽的分割线*****')
print(' ')
print(zidian1)