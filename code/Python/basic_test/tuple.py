#()tuple
age=(1,2,3,4,5) #cant not change
print(age)
print(age[0])
print(age[0:2])
#age[0]=100 change will fail
#mutable
age2=[1,2,3,4,5] #cant not change
age2[0]=100
age2.append(101)
age2.insert(2,99)

print(age2)
print(age2[0])
print(age2[0:2])

#split test
msg= "welcome to python world"
word=msg.split(" ")
print(word)

