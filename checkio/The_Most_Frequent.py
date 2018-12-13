#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/13 17:02
@filename:The_Most_Frequent
"""
def checkio(strings_list):
    dict_num = {}
    for i in strings_list:
        dict_num[i] = strings_list.count(i)
    # print(sorted(dict_num.items(), key=lambda x: x[1], reverse=True)[0][0])
    return sorted(dict_num.items(), key=lambda x: x[1], reverse=True)[0][0]


checkio(['a','a','a','a','b','b','c','c','c','c','c'])