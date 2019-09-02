#字串跟變數


a=0b10
b=0o10
c=0x10
print(a)
print(b)
print(c)
print("trans test:",int(1.256))
print("trans test+:"+str(int(1.256)))
print(1.52e3)

googol=10**100
print(float("153.5"))
print(str(True))
start='na'*4+'\n'
end='good'*3+'\n'
print(start+end)

letter='abcdefghijklmnopqrstuvwxyz'
print(letter[3])

print(letter[:])
print(letter[3:])
print(letter[:3])
#只會顯示 3~5-1
print(letter[3:5])
print("-6~-2",letter[-6:-2])

print("開始到結束間隔2字元",letter[::2])
print("反轉",letter[::-1])

print("len function",len(letter))

name='henny'
#name[0]='s' 不能用這種寫法只能用function改變
name.replace('n','z')
print(name)


todo="a,b,c,d,e,f"
print(todo.split(','))

test_list=['my','name','is','sheldon']
test_string=' '.join(test_list)
print("join string test:",test_string)

print("start with:",letter.startswith('abc'))
print("end with:",letter.endswith('xyz'))
print(letter.find("def"))
print(letter.find("aef"))
print(letter.rfind("def"))
print(letter.count("bcd"))
print("如果只有字母和數字就true:",letter.isalnum())

setup='a duck goes into a bar'
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.capitalize().swapcase())
#30表示有30個空格
print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))
#2表示替換數量 不填就全部替換
print(setup.replace("a ","fuck "))
print(setup.replace("a ","fuck ",1))
print(setup.replace("a ","fuck ",-1))
