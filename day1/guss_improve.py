cnt = 0
while cnt < 3:
    age_of_oldboy= int(input("please enter age:"))
    _age_of_oldboy = 34
    if age_of_oldboy == _age_of_oldboy:
         print("yes,you are get it")
         break
    elif  age_of_oldboy > _age_of_oldboy:
        print("you may guss bigger...")
    else:
        print("you may guss smaller...")
    cnt += 1
    print(cnt)
    if cnt ==3:
        continue_cinfim = input("do you want to keep gussing..?")
        if continue_cinfim != "n":
            cnt=0

