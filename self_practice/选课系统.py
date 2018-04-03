import pickle
import uuid,hashlib

def creat_uuid():
    return str(uuid.uuid1())
class BaseMode:
    def save(self):
        pickle.dump(self,open('F:\python\git\pythonlearn\self_practice\db1\%s'%self.identy,'wb'))

    @classmethod
    def get_all_obj_list(cls):
        ret = []
        for file_name in wenjianming:
            obj = pickle.load(open( / home / db /, 'rb'))
            ret.append(obj)
        return ret


class School(BaseMode):
    def __init__(self,name,addr,identy):
        self.identy=identy
        self.name=name
        self.addr=addr


    def __str__(self):
         return self.name

class Teacher(BaseMode):
    pass
class Course(BaseMode):
    pass
class Classes(BaseMode):
    pass

class Student(BaseMode):
    pass


