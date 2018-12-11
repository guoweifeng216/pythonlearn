#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/11 9:52
@filename:Right_to_Left
"""
def right_to_left(array):
    import re
    list_tmp = list(array)
    strings = ','.join(list_tmp)
    # p = re.compile(r'[right]')区别
    p = re.compile(r'right')
    subs = re.sub(p, "left", strings)
    return subs

right_to_left(("left", "right", "left", "stop"))
right_to_left(("bright aright", "ok"))
right_to_left(("brightness wright",))
right_to_left(("enough", "jokes"))