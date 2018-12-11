#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/11 10:05
@filename:Digits_Multiplication
"""
def checkio(number):
    result = 1
    if number == 0:
        return number
    else:
        num_tmp = str(number)
        num_list = []
        for digital in num_tmp:
            if int(digital) != 0:
                num_list.append(int(digital))
            else:
                continue
        for num in num_list:
            result = result * num
        print(result)
    return result
checkio(120345)
checkio(999)
checkio(111111)
checkio(100000)