#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2018/12/14 16:28
@filename:Is_stressful

"""


def is_stressful(stringd):
    string_list = stringd.split(' ')
    import re
    for str in string_list:
        if len((re.findall('h.*e.*l.*p.*|a.*s.*a.*p.*|u.*r.*g.*e.*n.*t.*', str, flags=re.IGNORECASE))):
            return True
    if stringd.endswith("!!!"):
        result = True
    elif stringd.isupper():
        result = True
    else:
        result = False
    return result


is_stressful("I neeed H---e-------L---------P-----------")
is_stressful("aeeess--aaa---pp--")
is_stressful("u22--r---g---e---n---tuuuuu")
is_stressful("u22--r---g------n---!!!")
is_stressful("He loves peace")