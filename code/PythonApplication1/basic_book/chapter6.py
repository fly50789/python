# coding=big5
#OO
#�����O
class person():
    #�غc�l
    def __init__(self,name):
        #�۷��O�bclass�̭��W�[�ܼ�
       self.name=name
hunter=person('Allen')
print(hunter.name)

#�~��

class car():
    def __init__(self):
        pass
    def exclaim(self):
        print('i m car')
    
#�~��car        
class yogo(car):
    pass

test1_1=car()
test1_2=yogo()
test1_1.exclaim()
test1_2.exclaim()





class car2():
    def __init__(self):
        pass
    def exclaim(self):
        print('i m 111car')
   
    
    
#�л\car        
class yogo2(car2):
    def exclaim2(self):
        print('i m morethan a111 car')
#�i�H�۩w�q�����O�S����method modular
    def push(self):
        print('pushharder')
test2_1=car2()
test2_2=yogo2()
test2_1.exclaim()
test2_2.exclaim()
test2_2.push()

class person():
      def __init__(self,name):
       self.name=name
class MDperson(person):
     def __init__(self,name):
      self.name=name+'DOCTER'
class JDperson(person):
     def __init__(self,name):
      self.name=name+'GOD'
GOD=JDperson('HAHA')
print(GOD.name)

class person2():
      def __init__(self,name):
       self.name=name
class Eperson(person2):
      def __init__(self,name,email):
#��Super�I�s�����O����k
       super().__init__(name)
       self.email=email
bob=Eperson('bob','123.gmail')
print(bob.name,bob.email)

#property,getter setter 

#��ئۭq�qproperty����k
class Duck():
     def __init__(self,input_name):
         self.hidden_name=input_name
     def get_name(self):
         print('inside the getter')
         return self.hidden_name
     def set_name(self,input_name):
         print('inside the setter')
         self.hidden_name=input_name

     name= property(get_name,set_name)
#�ۭq�qproperty�i�H�w�q�]�w��������欰
fowl=Duck('howard')
print(fowl.name)
fowl.name='fuck'
print(fowl.name)

class Duck2():
     def __init__(self,input_name):
         self.hidden_name=input_name
#�S��˹��l
     @property
     def name(self):
         print('inside the getter')
         return self.hidden_name
     @name.setter
     def name(self,input_name):
         print('inside the setter')
         self.hidden_name=input_name

fowl=Duck2('howsssard')
print(fowl.name)
fowl.name='fuck2'
print(fowl.name)  
print("can use hidden name",fowl.hidden_name)  


#����Q�~���Ψ쪺�W�r�Х[�����u
class Duck2():
     def __init__(self,input_name):
         self.__name=input_name
#�S��˹��l
     @property
     def name(self):
         print('inside the getter')
         return self.__name
     @name.setter
     def name(self,input_name):
         print('inside the setter')
         self.__name=input_name


class A():
    count=0
    def __init__(self):
        A.count+=1
    def exclaim(self):
        print('i m A')
    @classmethod
    def kid(cls):
        print("obj num",cls.count)
EASY=A()
BRE=A()
TEQR=A()
A.kid()
print('easy',EASY.count)
class B():
    @staticmethod
    def test():
        print('static method')
B.test()

#�h�� �i�H���ܦh�ۦP��k�W��

class Multi1():
      def a(self,name1):
        return name1+'3'
class Multi2():
      def a(self,name1):
        return name1+'2'
class Multi3():
      def a(self,name1):
        return name1+'1'

#�S���k���L
#����]�N��k��ƾ��]�N��k�i�H��__add__�o�ئr ��class�i�H���ܼư��B��


#�զX

class Bill():
    def __init__(self, description):
      self.description=description
class Tail():
    def __init__(self, length):
        self.length=length

class merge():
    def __init__(self, bill,tail):
        self.bill=bill
        self.tail=tail
    def about(self):
        print('merge test',self.bill.description,self.tail.length)

bill=Bill('sheldon')
tail=Tail(30)
merge_test=merge(bill,tail)
merge_test.about()

#��Wtuple �޲�...�S�Ƥ��n��
#�i�Hreplace�b�o�̤��갵
from collections import namedtuple

tuple_test=namedtuple('duck','bill tail')
# wide orange->bill long->tail �Ϊťդ��}
tuple_test2=tuple_test('wide orange','long')
print(tuple_test2)
print(type(tuple_test2))
print(tuple_test2.bill)
print(tuple_test2.tail)