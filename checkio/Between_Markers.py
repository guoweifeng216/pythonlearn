#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/11/12 10:47
@filename:Between_Markers
"""


def between_markers(strings, char1, char2):
    if char1 in strings:
        if char2 in strings:
            if len(strings[:strings.find(char1)]) > len(strings[:strings.find(char2)]):
                print("******")
                return ""
            else:
                print(strings[strings.find(char1)+len(char1):strings.find(char2)])
                return strings[strings.find(char1)+len(char1):strings.find(char2)]
        else:
            print(strings[strings.find(char1)+len(char1):])
            return strings[strings.find(char1)+len(char1):]
    elif char2 in strings:
            print(strings[:strings.find(char2)])
            return strings[:strings.find(char2)]
    else:
        print(strings)
        return strings



between_markers("def<errrr>", '<', '>')
between_markers("def<errrr>", '<', ' ')
between_markers("deferrrr>wwww<", '<', '>')
between_markers("def<errrr>ggg", ' ', '>')
between_markers("def<errrr>", ' ', ' ')
between_markers("<head><title>My new site</title></head>","<title>", "</title>")
between_markers('No[/b] hi', '[b]', '[/b]')
between_markers('No [b]hi', '[b]', '[/b]')
between_markers('No hi', '[b]', '[/b]')
between_markers('No <hi>', '>', '<')