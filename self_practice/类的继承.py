#!/usr/bin/env python
# -*- coding:utf-8 -*-
class SchoolNumber(object):
    member=0
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.enroll()
    def enroll(self):
         """"注册"""
         print "just enrolled a new school number"
         SchoolNumber.member +=1

    def tell(self):
         print "--------info:%s"%self.name
         for k,v in self.__dict__.items():
             print "\t %s %s"%(k,v)

         print "--------end-------"


    # def __del__(self):
    #     print "开除了%s"%self.name
    #     SchoolNumber.member-=1




class Teacher(SchoolNumber):
    """"讲师"""
    def __init__(self,name,age,sex,salary,course):
        SchoolNumber.__init__(self,name,age,sex)
        self.salary=salary
        self.course=course
    def teaching(self):

        print "Teacher %s is teaching %s"%(self.name,self.course)

class Student(SchoolNumber):
    def __init__(self,name,age,sex,course,tuition):
        SchoolNumber.__init__(self,name,age,sex)
        self.course=course
        self.tuition=tuition

    def pay_tuition(self,amount):

        print "student %s has just paied %s"%(self.name,amount)
        self.amount=amount

t1=Teacher("wusir",28,"male",3000,"python")
s1=Student("haitao",38,"male","pys15",30000)
s2=Student("lichuang",24,"male","pys15",30000)


print t1.member
t1.tell()
del s2