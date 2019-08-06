print(10/3)
print(10//3)

print(5//3)
print(5%3)
x=0b111
y=0b101
print(x&y)
print(x|y)

def f(n) : print ("{:04b}".format(n))
f(x&y)
def f(n) : print ("{:08b}".format(n))
f((x&y)<<2)

x=True
y=False
print(x and y)
print(x or y)

print(5>=3)
                
x ="10"
intx=int(x)
float(x)
float(intx)
print(intx)

test=[1]
test[:]=range(10) 
print(test)
test[2:5]=(0,0,0)
print(test)

com=complex(2,3)
print(com)



op= lambda x:x*x
op(5)
