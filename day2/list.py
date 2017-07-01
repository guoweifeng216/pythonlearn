import copy
#names = "zhanngyang weifeng linfeng lingli"
names = ["zhangyang","weifeng",["weifeng","xiaomei"],"linfeng","lingli"]
#names.append("haidong")#放在最后添加
#names.insert(1,"dahai")#插在1前
#names[2]="salary"#替换
#names.remove("haidong")#直接指定
#del names[1]#根据下标删除
#names.pop()#删除最后一个
#print(names)
#print(names[0],names[1])
#print(names[1:2])#切片
#print(names[-2:-1])#切片
#print(names[-2:])
#查找
#print(names.index("weifeng"))
#print(names[names.index("weifeng")])
#统计
#print(names.count("weifeng"))
#q清除
#print(names.clear())
#f反转
#names.reverse()
#print(names)
#排序
#names.sort()
#print(names)
#k扩展
#names2=[1,2]
#names.extend((names2))
#print(names)
#复制
#浅复制一层
#深复制
names3 = copy.deepcopy(names)
names3 = names.copy()
print(names)
print(names3)
#names[1] = "祥鹏"
#names[2][0] = "威风"
print(names)
print(names3)
names[1] ="wshi"
names[2][0] ="mary"
print(names)
print(names3)
for i in names:
    print(i)
#跳着切
print(names[::2])
#列表可以嵌套任何类型
