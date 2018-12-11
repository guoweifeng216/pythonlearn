#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/11 9:26
@filename:Index_Power
"""
def checkio(list, num):
    if len(list) < num:
        result = -1
    else:
        result = list[num] ** num

    return result

checkio([1, 2, 3, 4], 2)
checkio([1, 3, 10, 100], 3)
checkio([0, 1], 0)
checkio([1, 2], 3)