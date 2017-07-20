#打开文件
f =open('db2' , 'r+', encoding="utf-8")#如果打卡模式无B，则read，按照字符读取，有b，则read按字节
# f = open('db1''w')#只写，先清空原文件
#f = open('db2','x')#存在报错，不存在，创建并写内容
# f = open('db3','a')#追加
#f.truncate()#截断，指针后的全部清空
data = f.read(1)
print(f.tell())#当前指针所在位置
print(data)
#f.seek(0)#调整指针的位置
f.write("66")
for line in f:
    print(line)

f.close()