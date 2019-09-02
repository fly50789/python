_a=50


x,y=1,2
x,y=y,x

x,*y,z=1,2,3,4,5

print("a {} b {}".format(x,y))

list=[100,"twpijt",True,[1,2,3]]

print(list[3])
print(list[3][2])

test_dict=dict([["name","sheldon1"],["age",18]])
print(test_dict.items())
for key,value in test_dict.items():
    print(key,value)
string="123456789"
local=string[::2]

for n in range(1,4):
    print('string test:',string[::n])

print('string test:',string[::2])
print("area %s"%local)
print("area %s"%string[0])

a=10
cal_string="(5+2)*8*%d"%a
print( eval(cal_string) )

print(10**100)

print(string[-3:])



a = 5 + 3
a = (1, 2, 3)