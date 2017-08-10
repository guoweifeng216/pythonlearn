#_*_coding:utf-8_*_
import os

def sql_parse(sql):
    print ('sql str is %s'%sql)
    parse_func={
        'insert':insert_parse,
        'delete':delete_parse,
        'update':update_parse,
        'select':select_parse,
    }
    sql_l=sql.split(' ')
    func=sql_l[0]
    res=''
    if func in parse_func:
        res=parse_func[func](sql_l)
    return res

def insert_parse(sql_l):
    # insert into db1.emp values 鲁海宝,35,13910015353,测试,2005-06-27
    sql_dic={
        'func':insert, #函数名
        'insert':[],   #insert选项,留出扩展
        'into':[],     #表名
        'values':[],   #值
    }
    return handle_parse(sql_l,sql_dic)

def delete_parse(sql_l):
    # delete from db1.emp where id=1

    sql_dic={
        'func':delete,
        'delete':[], #delete选项,留出扩展
        'from':[],   #表名
        'where':[],  #filter条件
    }
    return handle_parse(sql_l,sql_dic)

def update_parse(sql_l):
    # update db1.emp set id=2 where name='alex'
    sql_dic={
        'func':update,
        'update':[], #update选项,留出扩展
        'set':[],    #修改的值
        'where':[],  #filter条件
    }
    return handle_parse(sql_l,sql_dic)

def select_parse(sql_l):
    # select * from db1.emp where not id= 1 and name = 'alex' or name= 'sb' limit 3
    print('sql str is %s' % sql_l)
    sql_dic={
        'func':select,
        'select':[], #查询字段
        'from':[],   #表
        'where':[],  #filter条件
        'limit':[],  #limit条件
    }

    return handle_parse(sql_l,sql_dic)

def handle_parse(sql_l,sql_dic):
    tag=False
    for item in sql_l:
        if tag and item in sql_dic:
            tag=False
        if not tag and item in sql_dic:
            tag=True
            key=item
            continue
        if tag:
            sql_dic[key].append(item)
    # print('before \033[33;1m%s\033[0m' %sql_dic)
    if sql_dic.get('where'):
        sql_dic['where']=where_parse(sql_dic.get('where'))

    # print('after \033[33;1m%s\033[0m' %sql_dic)
    return sql_dic

def where_parse(where_l):
    res=[]
    key=['and','or','not']
    char=''
    for i in where_l:
        if len(i) == 0:continue
        if i in key:
            if len(char) != 0:
                char=three_parse(char) #将每一个小的过滤条件如,name>=1转换成['name','>=','1']
                res.append(char)
            res.append(i)
            char=''
        else:
          char+=i
    else:
        char=three_parse(char)
        res.append(char)
    return res

def three_parse(exp_str):
    # print('three_opt before is \033[34;1m%s\033[0m' %exp_str)
    key=['>','=','<']
    res=[]
    char=''
    opt=''
    tag=False
    for i in exp_str:
        if i in key:
            tag=True
            if len(char) !=0:
                res.append(char)
                char=''
            opt+=i
        if not tag:
            char+=i
        if tag and i not in key:
            tag=False
            res.append(opt)
            opt=''
            char+=i
    else:
        res.append(char)
    # print('res is %s ' %res)
    #新增like功能
    if len(res) == 1:#['namelike_ale5']
        res=res[0].split('like')
        res.insert(1,'like')
    return res


#第二部分:sql执行
def sql_action(sql_dic):
    return sql_dic.get('func')(sql_dic)

def insert(sql_dic):
    print('insert %s' %sql_dic)
    db,table=sql_dic.get('into')[0].split('.')
    with open('%s/%s' %(db,table),'ab+') as fh:
        offs = -100
        while True:
            fh.seek(offs,2)
            lines = fh.readlines()
            if len(lines)>1:
                last = lines[-1]
                break
            offs *= 2
        last=last.decode(encoding='utf-8')
        last_id=int(last.split(',')[0])
        new_id=last_id+1
        #insert into db1.emp values 张国辉,30,18500841678,运维,2007-8-1
        record=sql_dic.get('values')[0].split(',')
        record.insert(0,str(new_id))
        record_str=','.join(record)+'\n'
        fh.write(bytes(record_str,encoding='utf-8'))
        fh.flush()
    return [['insert successful']]

def delete(sql_dic):
    db,table=sql_dic.get('from')[0].split('.')
    bak_file=table+'_bak'
    with open("%s/%s" %(db,table),'r',encoding='utf-8') as r_file,\
            open('%s/%s' %(db,bak_file),'w',encoding='utf-8') as w_file:
        del_count=0
        for line in r_file:
            title="id,name,age,phone,dept,enroll_date"
            dic=dict(zip(title.split(','),line.split(',')))
            filter_res=logic_action(dic,sql_dic.get('where'))
            if not filter_res:
                w_file.write(line)
            else:
                del_count+=1
        w_file.flush()
    os.remove("%s/%s" % (db, table))
    os.rename("%s/%s" %(db,bak_file),"%s/%s" %(db,table))
    return [[del_count],['delete successful']]

def update(sql_dic):
    #update db1.emp set id='sb' where name like alex
    db,table=sql_dic.get('update')[0].split('.')
    set=sql_dic.get('set')[0].split(',')
    set_l=[]
    for i in set:
        set_l.append(i.split('='))
    bak_file=table+'_bak'
    with open("%s/%s" %(db,table),'r',encoding='utf-8') as r_file,\
            open('%s/%s' %(db,bak_file),'w',encoding='utf-8') as w_file:
        update_count=0
        for line in r_file:
            title="id,name,age,phone,dept,enroll_date"
            dic=dict(zip(title.split(','),line.split(',')))
            filter_res=logic_action(dic,sql_dic.get('where'))
            if filter_res:
                for i in set_l:
                    k=i[0]
                    v=i[-1].strip("'")
                    print('k v %s %s' %(k,v))
                    dic[k]=v
                print('change dic is %s ' %dic)
                line=[]
                for i in title.split(','):
                    line.append(dic[i])
                update_count+=1
                line=','.join(line)
            w_file.write(line)

        w_file.flush()
    os.remove("%s/%s" % (db, table))
    os.rename("%s/%s" %(db,bak_file),"%s/%s" %(db,table))
    return [[update_count],['update successful']]

def select(sql_dic):
    db,table=sql_dic.get('from')[0].split('.')
    fh=open("%s/%s" %(db,table),'r',encoding='utf-8')

    filter_res=where_action(fh,sql_dic.get('where'))
    # print('filter_res is ====>',filter_res)
    fh.close()

    limit_res=limit_action(filter_res,sql_dic.get('limit'))
    # print('limit_res is ====>',limit_res)

    search_res=search_action(limit_res,sql_dic.get('select'))
    # print('select_res is ====>',search_res)

    return search_res

def where_action(fh,where_l):
    res=[]
    logic_l=['and','or','not']
    title="id,name,age,phone,dept,enroll_date"
    if len(where_l) !=0:
        for line in fh:
            dic=dict(zip(title.split(','),line.split(',')))
            logic_res=logic_action(dic,where_l)
            if logic_res:
                res.append(line.split(','))
    else:
        res=fh.readlines()
    return res

def logic_action(dic,where_l):
    res=[]
    # print('==\033[45;1m%s\033[0m==\033[48;1m%s\033[0m' %(dic,where_l))
    for exp in where_l:
        if type(exp) is list:
            exp_k,opt,exp_v=exp
            if exp[1] == '=':
                opt='%s=' %exp[1]
            if dic[exp_k].isdigit():
                dic_v=int(dic[exp_k])
                exp_v=int(exp_v)
            else:
                dic_v="'%s'" %dic[exp_k]
            if opt != 'like':
                exp=str(eval("%s%s%s" %(dic_v,opt,exp_v)))
            else:
                if exp_v in dic_v:
                    exp='True'
                else:
                    exp='False'
        res.append(exp)
    res=eval(' '.join(res))
    # print('==\033[45;1m%s\033[0m' %(res))
    return res

def limit_action(filter_res,limit_l):
    res=[]
    if len(limit_l) !=0:
        index=int(limit_l[0])
        res=filter_res[0:index]
    else:
        res=filter_res

    return res

def search_action(limit_res,select_l):
    res=[]
    fileds_l=[]
    title="id,name,age,phone,dept,enroll_date"
    if select_l[0] == '*':
        res=limit_res
        fileds_l=title.split(',')
    else:

        for record in limit_res:
            dic=dict(zip(title.split(','),record))
            # print("dic is %s " %dic)
            fileds_l=select_l[0].split(',')
            r_l=[]
            for i in fileds_l:
                r_l.append(dic[i].strip())
            res.append(r_l)

    return [fileds_l,res]



if __name__ == '__main__':
    while True:
        sql=input("sql> ").strip()
        if sql == 'exit':break
        if len(sql) == 0:continue

        sql_dic=sql_parse(sql)

        if len(sql_dic) == 0:continue #输入命令非法
        res=sql_action(sql_dic)

        for i in res[-1]:
            print(i)