#特性：无顺序，去重。查询速度快，比列表快，但比列表占用内存多


info = {
    'stu101':"mary",
    'stu102':"cane",
    'stu103':"like"
}
#print(info["stu101"])
#info["stu101"] = "武藤兰"
#print(info)
#info["stu104"] = "长经开"
#del info[stu101]
#info.pop()
#info.get(''):#chazhao
#stu101 in info#判断stu101是否存在info中
#info.values
#info.key
#info.setdefault()
#info.update()#合并字典，相同替换，不相同合并
#info.items()#把一个字典转换成列表
#dict.fromkeys([])#初始化一个字典
print(info.popitem())
for i in info:
    print(i,info[i])#最好用这个
#for k,v in info.items():
 #   print(k,v)



