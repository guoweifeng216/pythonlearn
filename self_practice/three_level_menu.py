menu = {
    "浙江":{
                "杭州":{
                        "上城区":["西溪路","浙大"],
                        "下城区":["潮王路","工大"]
                        },
                 "宁波":{
                         "北仑区":["高楼","大厦"],
                         "创业区":["轮船","大海"]
                        }
                },
    "安徽":{
            "合肥":{},
            "六安":{},
            "安庆":{}
    },
    "江苏":{
        "南京":{},
        "无锡":{},
        "苏州":{}
    }
}
exit_flag = True
while exit_flag:
    for i in menu:
        print(i)
    choice = input("please choice province:")
    if choice in menu:
        while exit_flag:
            for j in menu[choice]:
                print(j)
            choice1 = input("please choice city:")
            if choice1 in menu[choice]:
                while exit_flag:
                    for k in menu[choice][choice1]:
                        print(k)
                    choice2 = input("please choice count:")
                    if choice2 in menu[choice][choice1]:
                        for h in menu[choice][choice1][choice2]:
                            print(h)
                        choice3 = input("last class，please enter b continue or q quit:")
                        if choice3 =='b':
                            pass
                        elif choice3 =='q':
                            exit_flag= False
                    if choice2 == 'b':
                        break
                    elif choice2 == 'q':
                        exit_flag = False
            if choice1 == 'b':
                break
            elif choice1 == 'q':
                exit_flag = False