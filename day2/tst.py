import copy
person = ["name",["salary",100]]


p1 = person[:]
p2 = person[:]
p1[0] = "alex"
p2[0] = "fengjie"
p1[1][1]=50
print(p1)
print(p2)