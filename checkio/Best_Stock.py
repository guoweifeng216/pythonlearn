#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/11/12 14:38
@filename:Best_Stock
"""

def best_stock(dict):
    for key, value in dict.items():
        if value == max(dict.values()):
            print(key)
            return key
best_stock({'CAC': 10.0,'ATX': 390.2,'WIG': 1.2})