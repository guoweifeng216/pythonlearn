#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/12/7 16:28
@filename:Secret_Message
"""


def find_message(strings):
    import re
    p = re.compile(r'[-,.$()#+&*?!]')
    subs = re.sub(p, " ", strings)
    list_string = subs.split(" ")
    result = ''
    cnt_big_alphabet = 0
    list_tmp = []
    alphabet_cnt = 0
    if len(strings) > 0:
        for strs in list_string:
            if len(strs) > 0:
                list_tmp.append(strs)
            else:
                continue
        for i in range(len(list_tmp)):
            if list_tmp[i].capitalize():
                alphabet_cnt += len(list_tmp[i])
                for alphabet in list_tmp[i]:
                    if alphabet.isupper():
                        result = result + alphabet
                        cnt_big_alphabet += 1

        if alphabet_cnt == cnt_big_alphabet:
            status = "Capitals"
        else:
            status = result.lower()

    else:
        result = result
        status = "nothing"

    return result, status


find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
find_message("hello world!")
find_message("HELLO WORD!!!")


