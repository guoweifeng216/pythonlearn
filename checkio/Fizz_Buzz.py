#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/11/12 17:20
@filename:Fizz_Buzz
"""


def frizz_buzz(num):
    if (num % 3 == 0) & (num % 5 == 0):
        print("**")
        return ("Fizz Buzz")
    elif num % 3 ==0:
        return ("Fizz")
    elif num % 5 == 0:
        return ("Buzz")
    else:
        return str(num)

frizz_buzz(15)