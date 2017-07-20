
shopping = [
    ('Iphone',5800),
    ('mac pro',9800),
    ('bike',800),
    ('watch',10600),
    ('coffee',31),
    ('alex',120)
]
# def info():
#     tem_info={}
#     with open('info.txt','r',encoding='utf-8') as f:
#         line = f.readline()
#         info_list = line.rstrip().split('')
#         tem_info[info_list[0]] = info_list[1]
#         line = f.readline()
#     return tem_info
shopping_list = []
user_name = input("please enter username:")
password = input("please enter password:")
# user_info = info()
# for k,v in user_info.items():
salary = input("input your salary:")
if salary.isdigit():
   salary = int(salary)
   while True:
        #for item in shopping:
            #print (shopping.index(item),item)#
        for index,item in enumerate(shopping):#
            print(index,item)
        user_choice = input("选择什么？")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice <len(shopping) and user_choice>=0:
                p_item = shopping[user_choice]
                if p_item[1]<=salary:
                    shopping_list.append(p_item)
                    salary -=p_item[1]
                    print("Added  %s into shoping cart,your current \033[31;1m%s\033[0m"%(p_item,salary))#\033[31;1m%s\033[0m红色 \033[32;1m%s\033[0m绿色
                else:
                    print("\033[41;1m你的余额只剩[%s],买不了\033[0m"% salary)
            else:
                print("product code [%s] is not exist"%user_choice)
        elif user_choice=="q":
                print("------shopping list----")
                for p in shopping_list:
                    print(p)
                print("you current balance:",salary)
                exit()
             #print("exit...")