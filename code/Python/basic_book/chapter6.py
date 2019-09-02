# coding=big5
#OO
#空類別
class person():
    #建構子
    def __init__(self,name):
        #相當於是在class裡面增加變數
       self.name=name
hunter=person('Allen')
print(hunter.name)

#繼承

class car():
    def __init__(self):
        pass
    def exclaim(self):
        print('i m car')
    
#繼承car        
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
   
    
    
#覆蓋car        
class yogo2(car2):
    def exclaim2(self):
        print('i m morethan a111 car')
#可以自定義父類別沒有的method modular
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
#用Super呼叫父類別的方法
       super().__init__(name)
       self.email=email
bob=Eperson('bob','123.gmail')
print(bob.name,bob.email)

#property,getter setter 

#兩種自訂義property的方法
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
#自訂義property可以定義設定跟取直的行為
fowl=Duck('howard')
print(fowl.name)
fowl.name='fuck'
print(fowl.name)

class Duck2():
     def __init__(self,input_name):
         self.hidden_name=input_name
#特殊裝飾子
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


#不能被外部用到的名字請加雙底線
class Duck2():
     def __init__(self,input_name):
         self.__name=input_name
#特殊裝飾子
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

#多型 可以有很多相同方法名稱

class Multi1():
      def a(self,name1):
        return name1+'3'
class Multi2():
      def a(self,name1):
        return name1+'2'
class Multi3():
      def a(self,name1):
        return name1+'1'

#特殊方法掠過
#比較魔術方法跟數學魔術方法可以用__add__這種字 讓class可以跟變數做運算


#組合

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

#具名tuple 詭異...沒事不要用
#可以replace在這裡不實做
from collections import namedtuple

tuple_test=namedtuple('duck','bill tail')
# wide orange->bill long->tail 用空白分開
tuple_test2=tuple_test('wide orange','long')
print(tuple_test2)
print(type(tuple_test2))
print(tuple_test2.bill)
print(tuple_test2.tail)