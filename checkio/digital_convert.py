#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/11 13:47
@filename:digital_convert
"""
import string

def digital_convert(number, num_type):
    print(int(number, num_type))
    # print(oct(number[len(number) - 1]))
    if (num_type >= 10) & (num_type < 36):
        num_tmp = chr(num_type + 55)
        print(num_tmp)
    if num_tmp in number:
        print("********")
    else:
        # result = int(number, num_type)
        print("******")
    # print(num_type)







digital_convert("Z", 36)