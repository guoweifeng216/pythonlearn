#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/11/12 16:27
@filename:Bigger_Price
"""

def bigger_price(num,list):
    list_1 = sorted(list, key=lambda list : list['price'], reverse=True)
    return (list_1[:num])




bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
])