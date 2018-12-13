#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/11 13:47
@filename:digital_convert
"""
import string

def checkio(number, num_type):
    flag = True
    result = 0
    if (num_type >= 10) & (num_type < 36):
        num_tmp = chr(num_type + 55)
        for alh in number:
            if alh >= num_tmp:
                result = -1
                flag = False
        if flag:
            result = int(number, num_type)
    elif num_type == 36:
        result = int(number, num_type)
    else:
        for alh in number:
            if alh >= str(num_type):
                result = -1
                flag = False
        if flag:
            result = int(number, num_type)
    return result
checkio("AF", 16)
checkio("101", 2)
checkio("101", 5)
checkio("Z", 36)
checkio("AB", 10)
checkio("113", 2)