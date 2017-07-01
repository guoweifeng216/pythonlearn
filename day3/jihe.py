list_1 = [1,4,6,8,3,2,8]
list_2 = [1,3,5,7,9,7]
list_1 = set(list_1)
print(list_1)#jige
list_2 = set([2,3,2,7,4,6,3,8])
print(list_1,list_2)
print(list_1.intersection(list_2))#交集
print(list_1.union(list_2))#并集
#差集 in list_1 but no in list_2
print(list_1.difference(list_2))
#ziji
print(list_1.issubset(list_2))
print(list_1.issuperset(list_2))#父集
#对称差集
print(list_1.symmetric_difference(list_2))
list_3 = set([3,4,5])
list_4 =set([6,7,8])

print(list_3.isdisjoint(list_4))#判断是否有交集

print(list_1&list_2)
print(list_1|list_2)
print(list_1-list_2)

list_1.add(99)
list_1.update([777,999])
print(list_1)
print(list_1.discard(777))#list_1.remove()会报错