#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/11/12 15:12
@filename:Popular_Words
"""
def popular_words(strings, list):
    dict = {}
    strings = strings.lower()
    string_list = strings.replace("\n", " ").split(" ")
    for char in list:
        dict[char] = string_list.count(char)
    return dict

popular_words('''When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near'])