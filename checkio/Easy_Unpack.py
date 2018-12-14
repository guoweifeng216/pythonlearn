#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/14 8:42
@filename:Easy_Unpack
"""
import random
def checkio(tuple_num):
    list_tmp = []
    list_tmp.append(tuple_num[0])
    list_tmp.append(tuple_num[2])
    list_tmp.append(random.sample(list(tuple_num)[2:], 1)[0])
    return (tuple(list_tmp))
checkio((1, 2, 3, 4))