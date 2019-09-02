# list tuple dict set

#tuple 不可變更
#tuple list只差別在 () [],lisy可以不同類型同時存在
a_tuple=("dog","cat","bird")
empty_list=[]
empty_list2=list()
test_list=['1','2','3','4']
#string 快速轉換list
print(list('cat'))
print(a_tuple)
print(list(a_tuple))
#split會切成 list
birth_day='1/6/1952'
print(birth_day.split('/'))
#可以用index來取直有點像array 可以用-1~-n來取直 用n和-(n+1)都會溢位爆掉
print(test_list[2])
print(test_list[-1])

listA=['HUMMINGBIR','FINCH']
listB=['dodo','pgienon','ojkopj']
listC=[3,'test1',5,'test8']
all_list=[listA,listB,'MACAW',listC]
#長得像這樣[['HUMMINGBIR', 'FINCH'], ['dodo', 'pgienon', 'ojkopj'], 'MACAW', [3, 'test1', 5, 'test8']]
print(all_list)
print(all_list[1][0])

test_list[2]="change"
print(test_list)
#012 輸出20 slice本身輸出也是list
print(listB[::-2])

listB.append("fuck off")
print(listB)
#extend 跟+=用途一樣
listB.extend(listA)
print(listB)
listB+=listC
print(listB)

listB.insert(1,"insert test")
print(listB)

del listB[-2]
print(listB)
#remove很特別可以用值來刪除
listB.remove("insert test")
print(listB)
#可以用值查index
print(listB.index("FINCH"))
#pop會顯示同時刪除 預設值是-1
listB.pop(2)
print(listB)

#條件判斷式可以用IN 有存在回傳TRUE
print("abc" in listB)
#計算出現次數
print(listB.count("test"))
#把list用"XX"串接起來 tuple也可以 中間有數字會fail
print(", ".join(a_tuple))

sort_list=['C','B','E']
print(sorted(sort_list))
sort_listB=sorted(sort_list)
print(sort_listB)
#print(sort_list.sort())
#sorted會回傳值 sort自身就會改寫
sort_list.sort()
print(sort_list)
print(len(sort_list))

sort_list.clear()
print("clear the sort list:",sort_list)


a=[1,2,3]
#感覺好像pointer...
b=a
a[0]='fuck'
print(b)
#下面三種方式都是重新給予值
a1=[1,2,3]
b1=a1[:2].copy()
c=list(a1)
d=a1[:]

print(b1,c,d)

#tuple比較接近常數串列
empty_tuple=()
#可以不加誇號
one_tuple='test',
one_tuple2=('test',)
print(one_tuple)
print(one_tuple2)

#下面手法被稱為unpacking
marx='aaa','bbbb','ccccc',

q,w,e=marx
print(q)


password='uofwhouf'
icecream='chocolate'
#使用tuple交換數值
password,icecream=icecream,password
print(password)

t1=0
t2=100
t1,t2=t2,t1
print(t1)

#dict用{}來創建 下面是兩個創建dict的方法\
empty_dict={}
test_dict=dict([["name","sheldon"],["age",18]])
test_dict2={"city":"taipei","salary":50000000}
print(test_dict)
print(test_dict2)
#下面四個都會轉換成 a:b,c:d,e:f的dict
#lot=[(a,b),(c,d)]
#lot=([a,b],[c,d])
#los=[ab,cd,ef]
#los=(ab,cd,ef)
#dict(lot) #dict(los)

#以key替換value值 key值必須獨一無二只能多對一
test_dict["age"]=1000
print(test_dict)
#updata是合併
test_dict.update(test_dict2)
test_dict.update({"dog":"male"})
print(test_dict)

del test_dict["dog"]
print(test_dict)
test_dict.clear()
print(test_dict)
print("city" in test_dict2)
print(test_dict2["city"])
#.keys跟.values會回傳dict_key()這個特殊形態需要透過list再轉一次
print(list(test_dict2.keys()))
print(list(test_dict2.values()))
print(list(test_dict2.items()))
copy_fail=test_dict2
#copy後面沒加()會錯但不會顯示語法錯誤
copy_pass=test_dict2.copy()
test_dict2["city"]="南部"
print(copy_fail)
print(copy_pass)

#set

empty_set=set()
print(empty_set)
even={0,2,4,6,8}
odd={1,3,5,7,9}
#{'r', 'l', 't', 'e'} 集合裡面只會有一種元素所以是用來檢查某種東西存不存在其他不在意的情況下使用
print(set("letter"))
#list
print(set(["a","b","c"]))
#tuple
print(set(("a","b","c")))

drink={'martini':{'vodka','vermouth'},
       'black russian':{'vodka','kahlua'},
       'white russian':{'vodka','kahlua','cream'},
       'manhattan':{'rye','vermouth','bitter'},
       'screwdriver':{'orange juice','vodka'}

    }

for name, contents in drink.items():
    if 'vodka' in contents:
        print("normal test",name)

for name, contents in drink.items():
    if 'vodka' in contents and not ('vermouth' in  contents or 'cream' in  contents):
        print("not test",name)
#加強版
for name, contents in drink.items():
    if 'vodka' in contents and not ({'vermouth','cream'} &  contents ):
        print("not test2",name)

for name, contents in drink.items():
    if contents & {'vermouth',"orange juice"} :
        print("and test",name)


bruss=drink['black russian']
wruss=drink['white russian']
print(bruss|wruss)
#{}可以創造set or dict
aa1={1,2}
bb1={2,3}
print(aa1&bb1)
print(aa1.intersection(bb1))

print(aa1|bb1)
print(aa1.union(bb1))

print(aa1-bb1)
print(aa1.difference(bb1))

print(aa1^bb1)
print(aa1.symmetric_difference(bb1))
#子集合檢查 所有集合都是自身的subset
print(aa1<=bb1)
print(aa1.issubset(bb1))
print(aa1.issubset(aa1))
#真子集 個數一定比較多且包含
print(aa1<bb1)
#超集合
print(aa1>=bb1)
print(aa1.issuperset(bb1))
print(aa1.issuperset(aa1))
#超真集合
print(aa1>bb1)