# #為註解用...
#/為延續下一行的符號
a=  5\
    +3\
    +8
print(a)

furry=True
small=False

if furry:
    if small:
        print("test1")
    else:
        print("test4")
else :
    if small:
        print("test2")
    elif small and True:
        print("test 3")

x=6
x==5
5>3
10<3
5<3 and 10>3
5<3 or 10>3
5<3 and not 10>3
print(5<x<10)

#0跟空的list tuple dict set都視為false
empty_list=[]
if empty_list:
    print("something")
else :
    print("nothing")

count=1
while count<=5:
    print(count)
    count+=1
#break continue只用在for while上
while True:
    count+=1
    if count>10:
        break
    if count%2==0:
        continue
    print(count)
    
numbers=[1,4,3,5]
pos=0
while pos<len(numbers):
    number=numbers[pos]
    if number%2==0:
        print("even num",number)
        break
    pos+=1
else:#break not use
    print("no even number")
print("pos:",pos)


word='cat'
for letter in word:
    print(letter)

test_dict={'name':'sheldon','city':'taipei'}
for keys in test_dict.keys():
    print(keys)
for values in test_dict.values():
    print(values)
for item in test_dict.items():
    print(item)
for key,value in test_dict.items():
    print("key",key,"value",value)
#for 跟while依樣 break 取消 continue 跳過 else來檢查中斷

#特殊function zip會根據最短list來用

day=["day1","day2","day3","day4"]
fruit=["fruit1","fruit2","fruit3","fruit4",]
drink=["tea","coffee","wine"]
print(list(zip(day,fruit)))
#for loop 使用的變數值結束後依然可以使用 命名上需要注意

for dayss,fruitss,drinkss in zip(day,fruit,drink):
    print("list test",dayss,fruitss,drinkss)
print(list(zip(day,fruit)))
x=100
#0,2,4,6,8,10
#名字一樣他會直接使用而不是創建一個
for x in range(0,11,2):
    print(x)
print(x)

#串列生成式
numbers=[]
counterssss=123
for number in range(0,6):
    counterssss=5
    numbers.append(number)
print(numbers)
print(counterssss)

numbers_list=list(range(0,6))
print(numbers_list)                  
numbers_list=[number for number in range(1,6)]
print(numbers_list) 
numbers_list=[number*2 for number in range(1,6)]
print(numbers_list) 
a_list=[number for number in range(1,6) if number%2==0]
print("special list",a_list) 

rows=range(1,4)
cols=range(1,3)
cells=[(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)
#字典生成式

word='letters'
letter_counts={letter:word.count(letter) for letter in set(word)}


print("count test",word.count('t'))


#集合生成式
a_set={number for number in range(1,6) if number %3==1}
print(a_set)
#產生器生成式 不存在tuple生成式

number_thing=(number for number in range(1,6) if number %2==1)
print(type(number_thing))
for number in number_thing:
    print(number)
#可以用list fun轉成list
list(number_thing)

#函式
def do_nothing():
    pass
def sound():
    print("sound")
sound()
def agree():
    return agree
if agree():
    print("pass")
else:
    print("fail")

def echo(anything):
    return anything
print(echo('mjijrg'))

#特殊值 none
thing=None
if thing:
    print("something")
else:
    print("nothing")
#創建字典 可以預設default值 沒使用的話就會直接使用default值
def menu(wine,entree,dessert='pudding'):
    return {'wine':wine,'entree':entree,'dessert':dessert}
#可以直接指定名字就無視順序
print(menu(dessert='bagel',wine='bordeaux',entree='beef'))
print(menu(wine='bordeaux',entree='beef'))
#下方是一個小bug可以看到list疊加
#他不只是定義變數而且創建變數可能是直億器的特色
def buggy(arg,result=[]):
    result.append(arg)
    print(result)
buggy('a')
buggy('b')

def nobuggy(arg,result=None):
    if result ==None:
        result=[]
  
    result.append(arg)
    print(result)
nobuggy('a')
nobuggy('b')

#python不存在指標
#*特殊用法
def print_args(*args):
    print("tuple:",args)

print_args("this","is","tuple")
#正常用法要把該變數放最後
def print_more(a,b,*args):
    print("paraA",a,"paraB",b,"tuple:",args)
print_more("test","case",1,2,3,4)   
#**可以用來快速創建字典
def print_kwargs(**kwargs):
    print("key argument:",kwargs)
print_kwargs(name="sheldon",city="taipei")

#docstring 函式內部使用用來說明函式用途 可以用3個單引號做範圍註解
def print_if_true(thing,check):
    '''
    this function is print "thing"
    if "check" is true

    '''
    if check:
        print(thing)

#help可以用來看保留字根function功能 或用內建function__doc__

#help(echo)

#print(echo.__doc__)

#python所有東西都是物件 函數也可以當成物件

def answer():
    print(123)
def run_something(fun):
    fun()
run_something(answer)
type(run_something)

def add_args(arg1,arg2):
    print(arg1+arg2)
type(add_args)
def run_with_arg(func,arg1,arg2):
    func(arg1,arg2)
run_with_arg(add_args,5,9)
def sum_arg(*args):
    return sum(args)
def run_with_star(fun,*arg):
    return fun(*arg)
print(run_with_star(sum_arg,1,2,3,4))


#內部函數 在函數裡面再定義函數
a,b,c,d=1,1,1,1
def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)
print(outer(3,5))
#閉包（Closure）. 閉包是函式記得並存取語彙範疇的能力，
#可說是指向特定範疇的參考，因此當函式是在其宣告的語彙範疇之外執行時也能正常運作

def knight(say):
   def inner2(test):
     return "WTF '%s'"% say+test
   return inner2
a=knight("test")
b=knight("function")
print(type(a))
print(a("wffffff"))

#lambda

def edit_story(words,func):
    for word in words:
        print(func(word))
stair=["thud","meow","thud","hiss"]
edit_story(stair,lambda word:word.capitalize()+'!')

list_num=[1,2,3,4,5]

#產生器 yield來使用 yield實際上是return的用途但他會跑完function把所有的值
def my_range(first=0,last=10,step=1):
    number=first
    while number<last:
        yield number
        number+=step
print(my_range)
print("type of yiled:",type(my_range(1,5)))
ranger=my_range(1,5)
print(ranger)

for num in ranger:
    print(num)

#裝飾器 decorator
#不更動原有function下去變更 除錯器 計數器

def document_it(func):
    def new_function(*args,**kwargs):
        print("name",func.__name__)
        print("argument",args)
        print("keyword argument",kwargs)
        result=func(*args,**kwargs)
        print("result",result)
        return result
    return new_function

def add_int(a,b):
    return a+b
print(add_int(3,5))
add_new=document_it(add_int)
print(add_new(3,5))

@document_it
def add_int2(a,b):
    return a+b
print(add_int2(5,6))

def square_it(func):
    def new_function(*args,**kwargs):
         result=func(*args,**kwargs)
         return result*result
    return new_function
#裝飾子可以兩個以上但要注意順序
@square_it
@document_it
def add_int3(a,b):
    return a+b
print(add_int3(5,6))

#全域變數 可以直接使用 加 global表示是使用全域變數而且可以修改 locals globals可以用來看可使用變數
animel="bird"
def change_global():
    global animel
    animel="pig"
    a=1
    b=2
    print("local:",locals())
change_global()
print(animel)
#太長有空自己看
#print("global:",globals())


#try except做例外處理 只適用於會系統錯誤的情況
short_list=[1,2,3]
position=5
try:
    short_list[position]
except:
    print("pos need in range 0~",len(short_list)-1,"not use pos of ",position)

#製作例外處理 用raise exceptfunction(XXX)