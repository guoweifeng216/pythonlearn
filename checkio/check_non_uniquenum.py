
# def checkio(inter_num):
    # list=[]
    # for i in inter_num:
    #     count_num=inter_num.count(i)
    #     if count_num!=1:
    #         list.append(i)
    # return list

#other methd
def checkio(data):
    return [i for i in data if data.count(i) > 1]


print checkio([10,9,10,8,7,7])