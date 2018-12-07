#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/7 16:28
@filename:Secret_Message
"""
import re

def find_message(strings):
    p = re.compile(r'[-,$()#+&*?!]')
    # subs = re.split(p, strings)
    subs = re.sub(p, " ", strings)
    print(subs)
    # str_lsit = subs.split(' ')
    str_lsit = " ".join(subs)
    result_tmp = ' '
    cnt = 0
    if len(strings) > 0:
        for str in str_lsit:
            for i in range(len(str)):
                if str[i].isupper():
                    result_tmp = result_tmp + str[i]
                    cnt += 1
        result = result_tmp
    else:
        result = result_tmp
        status = 'nothing'
    # print(result)
    # return result, status


find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
# find_message("hello world!")
find_message("HELLO WORLD!!!")


