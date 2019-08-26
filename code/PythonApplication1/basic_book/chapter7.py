
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

#split
m=re.split('n',source)
print('m=',m,'length=',len(m))

#split
m=re.sub('n','?',source)
print('m=',m,'length=',len(m))