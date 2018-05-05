# codng:utf-8
# print("hello word")
# print("hello\nword") # 换行输出
# print("hello\\word") # 转义输出具有\符号
# print(r"hello word") # r就是raw原型输出
# #   -    连接符  --
# a = "name"
# print("my name is "+ a ) # 字符串相加
# b = "sf"
# c = 153
# print(a + str(c)) # 将int类型转为字符串str类型相加
# print("ni hao: %s %s"%(b,c)) # 多个参数化相加，%符号右侧使用括号，括号内多个参数使用英文逗号分隔
#
# a = input("请输入你的名字:") # a为自己输入的信息
# print(a) # 将自己输入的信息打印出来
#
# '''  多行注释用三个单引号或双引号开头和结束
# sdfsdfksldjf
# sdfjksdf
# '''

# 数据转换
# w = "hello"
# r = "word"
# w,r = r,w  # 转换格式
# print(w)
# print(r)

# int类型信息，为整型，没有带小数点
# a = 22222222
# print(type(a))
#
#
#
# # float浮点数类型信息
# b = 12.33
# print(type(b))
#
#
# # str字符串类型
# c = "sd552fsf三分少" # 使用单引号或者双引号包围
# print(type(c))
#
#
# # list列表类型，使用中括号包围
# d = [1,4,58,5,5,8,"dsf",12.22,[2,"sdf"]] # 队列
# print(type(d))
#
#
# # tuple元组类型，小括号包围，内容不可更改
# e = (1,2,3,5,"ds","第三方")
# print(type(e))
#
#
# # dict字典类型，大括号包围，用冒号相等对应("key":"value")，多个值用英文逗号分开
# f = {"a":"3","b":"4","c":5}
# print(type(f))
#
#
# # bool布尔值类型
# g = True
# h = False
# print(type(g))
# print(type(h))
#
#
# # None类型，什么都没有的意思
# i = None
# print(type(i))
#
#
# j = 4
# k = 5
# if j>k and k > 0:  # 如果两个条件都成立，那么将下面内容打印出来
#     print("dsfsfsdf")
# if j>k or k>0:
#     print("sdfjksdf") # 如果其中一个条件成立，那么将下面内容打印出来
#
# if not k<j:  # 如果条件不成立，那么将下面内容打印出来
#     print("f圣大非省大家逢山开路")
#
# k= "hello word"
# print(k[0:4]) # 正向切片输出
# print(k[::-6])# 反向切片输出
#
#
# # list队列里面取值
# l = [2,3,4,5,6,7,8]
# print(l[0]) # list队列正向取值，左边开始取，首个值表示下标为0，比如2就是下标0啦，一直下去
# print(l[-1]) # list队列反向取值，右边开始取，首个值表示下标为0-1，比如8就是下标-1啦，一直下去
# print(l[-4])
# print(l[2])
#
# # list队列加入数值
# n = [4,34,5]
# n.append(41) # 向队列最后面加入41数值
# print(n)
#
# # list队列删除数值
# m = [1,2,3,4]
# del m[-1] # 同个下标索引删除对象，这里是反向删除
# print(m)
# m.remove(3) # 直接删除队列某个对象
# print(m)
#
# # list队列修改数值
#
# m[0] = 50 # 使用正向索引修改list对象
# print(m)
# m[-1] = 80  # 使用反向索引修改list对象
# print(m)

# list队列弹出数值
# z = [2,3,4,5]
# z.pop()  # 将最后一个弹出
# print(z) # 输出弹出最后一个值的最新队列z
# b = z.pop() # 将最后一个值弹出
# print(b)  # 将最后一个弹出值输出显示


# 统计长度函数
# z = [2,3,4,5]
# print(len(z))

# 排序
# z = [2,2,32,43,5]
# z.sort()
# print(z)
# # 统计输出值出现次数
# print (z.count(2))

# 遍历输出
# a = "hello word"
# for i in a:
#     print("2222")  # "hello word"有多少个字符，那么这里就输出多少行这个字符串
#
# c = [2,3,5,6,7,7,9]
# for i in c:
#     print(i)

# range()函数区间输出，格式是range(起点，终点，步长)
# s = range(10) # 这样是输出区间
# print(s)
# f = list(range(0,10)) # 这样是区间内每个都输出
# print(f)
# d = list(range(5,50,2)) # 这样是区间内，从5开始，每个加2输出
# print(d)
# g = list(range(20,1,-1)) # 这样是区间20～1内，从20开始，每个值减1输出
# print(g)
#
# # 循环输出0～14的值
# for i in list(range(15)):
#     print(i)


# continune和break循环，当值小于/大于某个数值时，continune时跳出本次循环，进入下次循环；当值大于或小于某个数值时，break退出循环

# for i in list(range(15)):
#     if i < 8:
#         continue # 当下循环值小于8的，跳出循环
#     if i > 12:  # 当下循环值大于12时，结束本次循环
#         break
#     else:         # 反之，则输出循环值
#         print(i)

a = "sd"
b = "ij"
c = "21"
e = (a,b,c) # 元组属性
print(list(e)) # list将元组输出转为list队列属性