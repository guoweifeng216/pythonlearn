def checkio(data):
    T1=False
    T2=False
    T3=False
    for char in data:
        if char.isdigit():
            T1=True
        if char.isupper():
            T2=True
        if char.islower():
            T3=True
    T=T1&T2&T3
    if T and len(data)>=10 and len(data)<64:
         result=True
    else:
         result=False
    return result

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")