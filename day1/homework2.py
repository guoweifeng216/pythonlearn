import codecs
_username = "weifeng"
_password = "abc123"
#username = input("username:")
#password = input("password:")

cnt=0
while cnt < 3:
    username = input("username:")
    password = input("password:")
    
    with codecs.open("log.txt","a+") as  f:
         f.write(username+'\n')
    if _username ==username and _password == password:
        print("welcome user {name} login..".format(name=username))
        break
    else:
        print("invalid username or password")
    cnt+=1
    if cnt==3:
        print("The user have locked")

