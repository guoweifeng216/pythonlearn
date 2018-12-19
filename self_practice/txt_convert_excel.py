#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2018/12/19 10:28
@filename:txt_convert_excel

"""
import pandas as pd
import os


def txt_convert_file(dir_path):
    files = []
    for file in os.listdir(dir_path):
        if file.endswith('txt'):
            filename = os.path.join(dir_path, file)
            df = pd.read_table(filename, sep=' ')
            files.append(df)
    data = pd.concat(files)
    data.to_excel(os.path.join(dir_path,'contact.xlx'), index=False)


# print(os.getcwd())
txt_convert_file('E:\github\pythonlearn\self_practice')