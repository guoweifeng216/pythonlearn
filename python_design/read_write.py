#1
# fout=open('Greeting.txt','w')
# fout.write('hello\n')
# fout.write('world\n')
# fout.close()
# fin=open("Greeting1.txt",'r')
# print fin.readline().rstrip()
# for line in fin:
#     test=fin.readline().rstrip()
# fin.close()
# print test
#2
fout=open('Greeting1.txt','w')
fout.write('hello\n')
fout.write('world\n')
fout.close()
fin=open("Greeting1.txt",'r')
test=fin.readline().rstrip()
fin.close()
print test
#3
list1=['Hello\n','World\n']
fout=open('Greeting3.txt','w')
fout.writelines(list1)
fout.close()
fin=open("Greeting3.txt",'r')
test=fin.read()
fin.close()
# print test.rstrip()
#4
list1=['Hello\n','World\n']
fout=open('Greeting3.txt','a')
fout.writelines(list1)
fout.close()
fin=open("Greeting3.txt",'r')
test=fin.read().rstrip()
fin.close()
# print test
print ([x**2 for x in range(-2,3)])
print (sorted({x**2 for x in range(-2,3)}))