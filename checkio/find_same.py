def checkio(list1):
    len_list=len(list1)
    len0=len(list1[0])
    len1 = len(list1[1])
    len2 = len(list1[2])
    list2=list1
    list3=zip(*list1)
    print list3
    if len0==3 and len1==3 and len2==3 and len_list==3:
        for word in zip(*list1):
            if word[0]==word[1]==word[2] and word[0]!='.':
                print word[0]
l1=[[1,2,3],[1,2,6],[7,2,9]]
checkio([[1,2,3],[1,1,6],[7,2,1]])
# for i in zip(*l1):
#     print i
#     print(i[0])
#     print(i[1])
#     print(i[2])