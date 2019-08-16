#!/usr/bin/python3

name="sheldon copper"


print(len(name))
print(name.upper())
upname=name.upper()
print(upname.lower())

str ='abcdefgh'
print(str[-1])
print(str[1])
print(str[1::3] )

str="aaa,bbb,ccc"
print(str.split(','))
print(str.replace('a','b'))
print(str.replace("a","b",2))
print(str)

print("test {}".format(str)+ " add test")


s='hello'
a,b,c,d,e=s
print(e)