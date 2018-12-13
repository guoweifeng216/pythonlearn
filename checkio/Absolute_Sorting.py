#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/13 10:46
@filename:Absolute_Sorting
"""
def checkio(tuple_num):
    tuple_list = []
    abs_tmp = []
    for i in range(len(tuple_num)):
        if tuple_num[i] < 0:
            tuple_list.append(abs(tuple_num[i]))
            abs_tmp.append(abs(tuple_num[i]))
        else:
            tuple_list.append(tuple_num[i])
    abs_list = sorted(tuple(tuple_list))
    for i in range(len(abs_list)):
        if abs_list[i] in abs_tmp:
            abs_list[i] = ~abs_list[i] + 1
    return abs_list

checkio((1, 2, -10, -7))