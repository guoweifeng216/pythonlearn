#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/10 14:19
@filename:Continue_Three_Words
"""

def checkio(strings):
    string_tmp = ''.join(strings.split(' '))
    if not string_tmp.isdigit():
        if len(strings) > 2:
            strings_list = strings.split(' ')
            for i in range(len(strings_list)-2):
                if strings_list[i].isalpha():
                    if strings_list[i+1].isalpha():
                        if strings_list[i+2].isalpha():
                            result = True
                            break
                        else:
                            result = False

                    else:
                        result = False
                        continue

                else:
                    result = False
                    continue
        else:
            result = False
    else:
        result = False
    return result

print(checkio("Hello World hello"))
print(checkio("ba bla bla bla"))
print(checkio("He is 123 man"))
print(checkio("1 2 3 4"))
print(checkio("HI"))
print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))