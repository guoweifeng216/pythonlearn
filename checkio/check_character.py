
def check_character(input_string):
    char_dict={}
    string=''
    for char in input_string:
        if str.isalpha(char):
            string=string+char
    string=string.lower()
    for char in string:
        char_dict[char]=string.count(char)
    # print char_dict
    char_dict1=sorted(char_dict.items(), key=lambda x: x[1])#value sort
    char_dict2 = sorted(char_dict.keys())#key sort
    print char_dict1
    if char_dict1[0][1]==char_dict1[len(char_dict1)-1][1]:
        print char_dict2[0]
    else:
        print char_dict1[len(char_dict1)-1][0]

    # print char_dict2
check_character('AAAooo')