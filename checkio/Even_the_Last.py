#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/7 16:05
@filename:Even_the_Last
"""

def checkio(array):
    sum_value =0
    if len(array) > 0:
        for i in range(len(array)):
            if i % 2 ==0:
                sum_value += array[i]
        result = sum_value * array[len(array)-1]
    else:
        result = 0
    return result

checkio([0, 1, 2, 3, 4, 5])
checkio([1, 3, 5])
checkio([6])
checkio([])