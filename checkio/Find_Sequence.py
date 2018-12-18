#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2018/12/17 15:03
@filename:Find_Sequence

"""


def check_find(list_array):

    for i in range(len(list_array)):
        if len(set(list_array[i])) == 1:
            print(list_array[i])
            break
        else:
            list_tmp = []
            for j in range(len(list_array[i])):
                print("***")
                list_tmp.append(list_array[i][j])
            print(list_tmp)
            print("**********")
# check_find([
#         [2, 1, 1, 6, 1],
#         [1, 1, 2, 1, 1],
#         [4, 1, 1, 3, 1],
#         [5, 1, 5, 5, 5]
#     ])
check_find([
        [5, 1, 1, 6, 1],
        [5, 1, 2, 1, 1]
    ])