
#資料處理

print('test','test2',456)


#python字串是unicode
def unicode_test(value):
    import unicodedata
    #name是給人看的名稱
    name=unicodedata.name(value)
    #lookup會翻譯name
    value2=unicodedata.lookup(name)
    #print 另外一種用法
    print('value="%s", name="%s", value2="%s"'%(value,name,value2))

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
#所用的字形可能沒有包含所有的unicode
unicode_test('\u2603')

place='caf\u00e9'
print(place)
unicode_test('\u00e9')
#可以用 \N{NAME} 的方式加上去 
u_umlaut='caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(u_umlaut)

print(len('$'))
#len會計算字元數不是byte數 U改成u的話會變成byte數?原因不明
print(len('\U0001f47b'))


#UTF-8（8-bit Unicode Transformation Format）每個字元使用1~4個BYTE
#ASCII 1個BYTE
#拉丁語 2個BYTE
#其他基本語 3個BYTE
#其他4個BYTE 包含一些亞洲語言和符號


#編碼
#'ascii','utf-8','latin-1','cp-1252','unicode-escape'


snowman='\u2603'
#根據字元數量 print
print('length test:',len(snowman))
#encode function會轉成byte

ds=snowman.encode('utf-8')
print('ds:',ds,'len:',len(ds))

#亂用編碼除非位元正確不然會報錯 下面是忽略錯誤以及把不能理解的字轉成?兩種寫法
print(snowman.encode('ascii','ignore'))
print(snowman.encode('ascii','replace'))
#網頁 unicode 轉義序列
print(snowman.encode('ascii','xmlcharrefreplace'))

#解碼

place_byte=place.encode('utf-8')
#byte不能與他串接
print('byte:',place_byte,'type:',type(place_byte))

place2=place_byte.decode('utf-8')
#print用 逗號代表 空格及串接,+號則只有串接的效果 
print('decode test:'+place2)
#用錯誤的解碼會報錯

#格式
#%s 字串
#%d 十進位
#%x 十六進位
#%o 八進位
#%f 十進位浮點數
#%e 指數浮點數
#%g 十進位或指數幅點數
#%% %字元
#舊的用法
print('%x'%42)
print('%d%%'%100)

n=42
f=0.25456
#10代表欄位寬度
print('%10d %10f'%(n,f))
#-代表左對齊
print('%-10d %-10f'%(n,f))
#.4表示位元數
print('%-10.4d %-10.4f'%(n,f))

print('%.4d %.4f'%(n,f))
#可以用*然後在後面定義
print('%*.*d %*.*f'%(10,4,n,10,4,f))

#新的用法
print("{} {}".format(n,f))
#可以在{}給值變更順序
print("{1} {0}".format(n,f))
#可以自訂義變數
print("{f} {n}".format(n=55,f=77.77))

d={'n':42,'f':7.03,'s':'string cheese'}
#這裡的0代表變數位置的0
#單獨一個變數可以用 多個就不知道了
print("{[s]} ".format(d))
print("{0[s]:30} {0[f]:30} {0[n]:30} {1}".format(d, 'pos 1'))

#{index:legacy type} type不能錯不然不給pirnt
print("{0:d} {1:f}".format(n,f))
#可以給名字當index 有點像是dict 但除了增加可讀性外沒啥用...
#tuple=dict(nss=100,fss=5.7777)
print("{nss:d} {fss:f}".format(nss=100,fss=5.7777))
#靠右 靠右(比較明顯) 靠左 置中
print("{nss:10d} {fss:10f}".format(nss=100,fss=5.7777))
print("{nss:>10d} {fss:>10f}".format(nss=100,fss=5.7777))
print("{nss:<10d} {fss:<10f}".format(nss=100,fss=5.7777))
print("{nss:^10d} {fss:^10f}".format(nss=100,fss=5.7777))
#依然可以用.2表示 精確度 但是"整數"不能使用
print("{nss:^10d} {fss:^10.2f}".format(nss=100,fss=5.7777))

#再對齊符號前加任意字符=填充符號
print("{0:!^20s}".format('Document'))


#正規表示法 以下所有function都在re裡面
#match 只可以比較開頭
import re
source='young sister frank ank'
m=re.match('you',source)
print('match type',type(m))
if m:
    print(m.group())
m=re.match('frank',source)
if m:
    print(m.group())
#用正規表示法去搜尋
#.=任何單一字元
#*=任意數量
m=re.match('.*frank',source)
if m:
    print(m.group())
#search不用在字首
m=re.search('frank',source)
if m:
    print(m.group())

import datetime
print(type(datetime.datetime.now()))
print('{:%Y%m%d}'.format(datetime.datetime.now()))

#findall 找所有
m=re.findall('n',source)
print('m=',m,'length=',len(m))

m=re.findall('n.',source)
print('m=',m,'length=',len(m))

#split 切割
m=re.split('n',source)
print('m=',m,'length=',len(m))

#sub 替換
m=re.sub('n','?',source)
print('m=',m,'length=',len(m))

#特殊字元 
#\d 數字 \D非數字 \w 英數 \W非英數
#\s空白 \S非空白 \b 一個單字範圍 \B非單字
import string

printable=string.printable
print('len:',len(printable))
print('print',printable[0:50])
print('print2',printable[50:])

print(re.findall('\d',printable))
print(re.findall('\w',printable))
print(re.findall('\s',printable))
print(re.findall('\b',printable))
#\d
#正規表示法會搜尋unicode所有數字不只asii的0~9


#主要模式指定符
#請參考 https://codertw.com/%E4%BC%BA%E6%9C%8D%E5%99%A8/145364/

source= 'i wish i have i wish i might Have a dish of fish tonight'

print(re.findall('wish',source))
print(re.findall('wish|fish',source))
print(re.findall('^wish',source))
#找開頭^
print(re.findall('^i wish',source))
#找結尾$
print(re.findall('dish tonight$',source))
#^ $被稱為 錨點anchor
print(re.findall('[wf]ish',source))
print(re.findall('[wsh]+',source))
print(re.findall('ght\W',source))
print(re.findall('i (?=wish)',source))
#會有bug 因為\b是 pyhton的轉義字元代表倒退建
print(re.findall('\bdish',source))
#+r的話會取消python的轉義字元
print(re.findall(r'\bdish',source))

#m=re.search(r'(dish\b).*(\bfish)',source)
m=re.search(r'(dish\b).*(\bfish)',source)
print(m.group())
#groups會跟據 .*切開
print(m.groups())
#用?P <name > expr可以存成變數值
m=re.search(r'(?P<DISH>dish\b).*(?P<FISH>\bfish)',source)
print(m.groups())
#可以找出特定值
print('TEST',m.group('DISH'))

print(re.findall('^[0-z]{4}$','bCaDaaa'))
print(re.findall('[0-z]{4}','bCaDaaa'))

#至少有一個數字
#至少有一個小寫英文字母,大寫英文字母
#字串長度在 6 ~ 30 個字母之間
# ^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,30}$



# 練習抓abbbbc, bc
test_string = 'find abbbbc, bc, skip c, acc'
pattern = 'a*b+c'
ans=re.findall(pattern,test_string)
print(ans)
# 練習找數字
test_string = '12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping'
pattern = '[0-9]+'
ans=re.findall(pattern,test_string)
print(ans)
# 練習找文字
test_string = 'find: can, man, fan, skip: dan, ran, pan'
pattern = '[cmf]an'
ans=re.findall(pattern,test_string)
print(ans)
# 練習跳脫符號
test_string = 'find: 591., dot., yes., skip: non!'
pattern = '.{3}\.'
ans=re.findall(pattern,test_string)
print(ans)
# 條件式搜尋
test_string = 'find: I love cats, I love dogs, skip: I love logs, I love cogs'
pattern = 'I love cats|I love dogs'
ans=re.findall(pattern,test_string)
print(ans)




#byte
blis=[1,2,3,255]
the_blis=bytes(blis)
print(the_blis)
#不允許更改變數
#the_blis[0]=2
the_blis_array=bytearray(blis)
the_blis_array[0]=2
#byte array允許更改
print(the_blis_array)


ALL_ARRAY=bytes(range(0,256))

#二進位可以用 import struct來使用(有用到在查)


#binascii()
import binascii

trans=b'TEST'
print(type(trans),trans[0])
trans2=binascii.hexlify(trans)
trans3=binascii.unhexlify(trans2)
print("trans:",trans2)
print("trans again:",trans3)

print()


#b'input\n' # bytes字节符，打印以b开头。
#r'input\n' # 非转义原生字符，经处理'\n'变成了'\\'和'n'。也就是\n表示的是两个字符
#u'input\n' # unicode编码字符，python3默认字符串编码方式。
string_test='123'
print(string_test[0])