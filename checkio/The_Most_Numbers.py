#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/11/13 9:17
@filename:The_Most_Numbers
"""


def checkio(*args):
    if len(args) > 0:
        max_value = max(args)
        min_value = min(args)
        result = max_value - min_value
    else:
        result = 0
    return result


def almost_equal(checked, correct, significant_digits):
    precision = 0.1 ** significant_digits
    print(correct - precision < checked < correct + precision)
    return correct - precision < checked < correct + precision


assert almost_equal(checkio(1,-2,3,4.0),6,3)
