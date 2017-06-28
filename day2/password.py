import getpass
_username = "weifeng"
_password = "abc123"
#username = input("username:")
#password = input("password:")
username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")
print(username,password)
if _username ==username and _password == password:
    print("welcome user {name} login..".format(name=username))
else:
    print("invalid username or password")