name = "Alex Li"
def change_name(name):
    print("before change:", name)
    name = "金角大王,一个有Tesla的男人"
    print("after change", name)
change_name(name)
print("在外面看看name改了么?", name)
# 全局与局部变量
# 在子程序中定义的变量称为局部变量，在程序的一开始定义的变量称为全局变量。
# 全局变量作用域是整个程序，局部变量作用域是定义该变量的子程序。
# 当全局变量与局部变量同名时：
# 在定义局部变量的子程序内，局部变量起作用；在其它地方全局变量起作用。