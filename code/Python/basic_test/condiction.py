#change type
print(3.5%1)
#x=int(input("type number:"))
x=5
if(x>10):
    print("bigger")
elif(x>0):
    print('small')
else:
     print('negative')
y=100
i=0
while(i<6):
    print("{}".format(i*10))
    i+=1

for j in range(10):
    print(j)

l=[31,32,33,"hi","sh"]    
for item in l:
    print(item)
for i in range(5):
    print(l[i])

word="python"
for letter in word:
    if(letter=='t'):
        continue
    if(letter=='o'):
        break
    print(letter)

for i in range(5):

   print(i)

print("i:{}".format(i))

