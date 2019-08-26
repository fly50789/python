pass
import sys
#cant use chinesse 
print('sys arg:',sys.argv)

#modular test
#need to specify the modual you call
import chapter5_report
description=chapter5_report.get()
print("test 1:",description)

#as=>nickname
import chapter5_report as wr
description=wr.get()
print("test 2:",description)

from chapter5_report import get as do
description=do()
print("test 3:",description)

# env variable
#for place in sys.path:
#    print(place)
#

#package use file level to sperate

from source import chapter5_day,chapter5_week
print("day",chapter5_day.get())
for number,out in enumerate(chapter5_week.get(),1):
  print(number,out)

dict_test={"name":"sheldon","city":"taipei"}
#add carboon to dict_test by function setdefault
dict_end=dict_test.setdefault('carboon',12)
print(dict_end)
print(dict_test)
#defaultdict every new input has a default value=0
from collections import defaultdict
dict_test2=defaultdict(int)
dict_test2['hydrogen']=1
dict_test2['oxygen']
print(dict_test2)

def no_idea():
  return "WTF"
# self define default value
dict_test3=defaultdict(no_idea)
dict_test3['hydrogen']="ha"
dict_test3['oxygen']
print(dict_test3)

#lambda
dict_test4=defaultdict(lambda:"WTF2")

dict_test4['hydrogen']="haAAAA"
dict_test4['oxygen']
print(dict_test4)

#COUNTER
dict_test5=defaultdict(int)
for food in ['egg','spam','veg','egg','egg']:
  dict_test5[food]+=1
for food,count in dict_test5.items():
  print(food,count)

dict_test6={}
for food in ['egg','spam','veg','egg','egg']:
  if not food in dict_test6:
    dict_test6[food]=1
  else:  
    dict_test6[food]+=1
for food,count in dict_test6.items():
  print(food,count)

 #counter function transfer to counter type 
 #import need to specify the captial of upper or lower case

from collections import Counter 
egg_input=['egg','spam','veg','egg','egg']
egg_result= Counter(egg_input)
egg_result2= Counter(egg_input)
print(egg_result)
#counter type can do mathmatics 
egg_result+egg_result2
egg_result-egg_result2
egg_result&egg_result2
print(type(egg_result))
print("result or ",egg_result|egg_result2)



#OrderedDict will remember the order of input to dict
from collections import OrderedDict
quotes=OrderedDict([
('Name','Sheldon'),
('City','TAIPEI'),
('SAL','55555')
])

for key,value in quotes.items():
  print(key,value)


#deque push= extend,append pop=pop
def pal(word):
  from collections import deque
  dq =deque(word)
  while len(dq)>1:
    if dq.popleft()!=dq.pop():
      return False
  return True  
print(pal('aca'))
print(pal('ca'))


import collections
d1=collections.deque()
d1.extend('abcdefg')
print ('extend:',d1)
d1.append('h')
print ('append:',d1)
# add to left
d2=collections.deque()
d2.extendleft(range(1,6))
print ('extendleft:',d2)
d2.appendleft(6)
print ('appendleft:',d2)


#itertools
import itertools
for item in itertools.chain([1,2],['a','b']):
  print(item)
#for item in itertools.cycle([1,2]):
#  print(item)
for item in itertools.accumulate([1,2,3,4]):
  print(item)

#pprint
from pprint import pprint
pprint(quotes)
print(quotes)

