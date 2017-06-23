name = input("name:")
age = int(input("age:"))
print(type(age),type(str(age)))#string
job = input("job:")
salary = input("salary:")
info = '''
-------info of %s------
Name:%s
Age:%d
Job:%s
Salary:%s

'''% (name,name,age,job,salary)
print(info)

info2 = '''
-------info2 of {name}------
Name:{name}
Age:{age}
Job:{job}
Salary:{salary}

'''.format(
          name=name,
          age=age,
          job=job,
          salary=salary
)
print(info2)


info3 = '''
-------info3 of {0}------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}

'''.format(name,age,job,salary)
print(info3)