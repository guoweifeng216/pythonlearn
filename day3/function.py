#过程是没有返回值得函数
#函数特性：减少重复代码，程序可扩展，易维护
def sayhi():  # 函数名
    print("Hello, I'm nobody!")
sayhi()  # 调用函数
#形参变量只有在被调用时才分配内存单元，在调用结束时，即刻释放所分配的内存单元。因此，形参只在函数内部有效。函数调用结束返回主调用函数后则不能再使用该形参变量
#实参可以是常量、变量、表达式、函数等，无论实参是何种类型的量，在进行函数调用时，它们都必须有确定的值，以便把这些值传送给形参。因此应预先用赋值，输入等办法使参数获得确定值
def calc(x, y):#x,y形参变量
    res = x ** y
    return res  # 返回函数执行结果


c = calc(a, b) ＃结果赋值给c变量，a,b实参
print(c)
#关键参数 正常情况下，给函数传参数要按顺序，不想按顺序就可以用关键参数，只需指定参数名即可，但记住一个要求就是，关键参数必须放在位置参数之后。
#非固定参数
def stu_register(name, age, *args):  # *args 会把多传入的参数变成一个元组形式
    print(name, age, args)
# stu_register("Alex", 22)
# 输出
# Alex 22 () #后面这个()就是args,只是因为没传值,所以为空
stu_register("Jack", 32, "CN", "Python")
# 输出
# Jack 32 ('CN', 'Python')
还可以有一个 ** kwargs
def stu_register(name, age, *args, **kwargs):  # *kwargs 会把多传入的参数变成一个dict形式
    print(name, age, args, kwargs)
stu_register("Alex", 22)
# 输出
# Alex 22 () {}#后面这个{}就是kwargs,只是因为没传值,所以为空
stu_register("Jack", 32, "CN", "Python", sex="Male", province="ShanDong")
# 输出
# Jack 32 ('CN', 'Python') {'province': 'ShanDong', 'sex': 'Male'}

#匿名函数
calc = lambda n:n**n
print(calc(10))
res = map(lambda x:x**2,[1,5,7,4,8])#map实现遍历list
for i in res:
    print(i)
#高阶函数 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)
res = add(3, -6, abs)
print(res)

