#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/11/12 9:55
@filename:Second Index
"""


def second_index(strings, char):
    if strings.count(char) < 2:
        return None
    count = 0
    char_count = 0
    str_list = list(strings)
    for each_char in str_list:
        count += 1
        if each_char == char:
            char_count += 1
            if char_count == strings.count(char):
                return count - 1

second_index("hiiiiii", 'i')