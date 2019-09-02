#資料的去處
# r 讀取 w 寫入 x當空白時寫入 a附加寫入
# t代表文字 b代表二進位
#obj=open(filename,mode)

poem="There was a young lady named Bright   \n   \
      Whose speed was far faster than light  \n   She sets out one day \n \
      In a relative way \n \
      And returned on the previous night\n"
print(len(poem))

#write
fout=open('relativity','wt')
print('write function:',fout.write(poem))
#用法一樣選一個就好
#print(poem,file=fout)
fout.close()

#print 在預設會加空白及換行
#sep分隔負號 end換行符號
#print(poem,file=fout,sep='',end='') 這樣等同使用 fout.write(poem)


#如果字串很大
#fout.write(poem[a:b])分段寫入最後在close

poem=''
fin=open('relativity','rt')
#fin.readline()
for line in fin:   
    poem+=line
fin.close()
print(len(poem))



poem=''
fin=open('relativity','rt')
#fin.readline()
lines=fin.readlines()
print(len(lines)," lines read")
for line in lines:   
    print(line,end='')
   # print(line)
fin.close()


#byte write

bdata=bytes(range(0,256))
print(len(bdata))
fout=open('bfile','wb')
fout.write(bdata)
fout.close()
#一樣可以分段寫入

fin=open('bfile','rb')
bdata=fin.read()
fin.close()
print(bdata)

#下方範例會自動關閉檔案
with open('relativity','wt') as fout:
    fout.write(poem)


#tell 當前位置 seek 跳到XX位置
fin=open('bfile','rb')
print(fin.tell())
print(fin.seek(255))
bdata=fin.read()
print('data',bdata[0],'len:',len(bdata))

#seek(offset,orgin)
#orgin=0 起點 orgin=1目前位置 orgin=2從結尾算
print(fin.seek(-1,2))

#這些讀檔最好是適用於 asii 因為 utf-8每個字的byte數不一

#csv

import csv
villains=[
    ['doctor','no'],
    ['rosa','klebb'],
    ['mister','big'],
    ['auric','goldfinger'],
    ['ernst','blofeld']
    ]
#不加newline=''會換行符號錯誤
with open('villains','wt', newline='') as fout:
    csvout=csv.writer(fout)
    csvout.writerows(villains)

import csv
with open('villains','rt') as fin:
    cin=csv.reader(fin)
    villains=[row for row in cin]

print(villains)

#字典的寫法
with open('villains','rt') as fin:
    cin=csv.DictReader(fin,fieldnames=['first','last'])
    villains=[row for row in cin]

print(villains)

import csv
villains=[
    {'first':'doctor','last':'no'},
    {'first':'rosa','last':'klebb'},
    {'first':'mister','last':'big'},
    {'first':'auric','last':'goldfinger'},
    {'first':'ernst','last':'blofeld'}
    ]
with open('villains2','wt', newline='') as fout:
    cout=csv.DictWriter(fout,['first','last'])
    cout.writeheader()
    cout.writerows(villains)

import csv
with open('villains2','rt') as fin:
    cin=csv.DictReader(fin)
    villains=[row for row in cin]
print(villains)    

#xml
import xml.etree.ElementTree as et
print("XML analysis test")
tree=et.ElementTree(file='menu.xml')
root=tree.getroot()
print(root.tag)
for child in root:
    print("tag:",child.tag,'attrubutes:',child.attrib)
    for grandchild in child:
         print("\ttag:",grandchild.tag,'attrubutes:',grandchild.attrib)
#number of section
print(len(root))
#number of item
print(len(root[0]))

#另外有xml.dom及xml.sax兩種工具(自己去查書本沒有)

#json
menu = \
{
 'breakfast':{
     "hour":"7-11",
     "items":{
         "burritos":"$6.00",
         "pancake":"$4.00"
         }
     },
 'lunch':{
     "hour":"11-3",
     "items":{
         "hambuger":"$5.00"         
         }
     },    
 'dinner':{
     "hour":"3-10",
     "items":{
         "spaghetti":"$8.00"
         
         }
     }   
        
}

import json
#json未定義時間類型需要你自己定義
#另外key的取值不是固定順序的
#轉成json格式字串
menu_json=json.dumps(menu)
print(menu_json)
menu2=json.loads(menu_json)
#格式互轉
print(menu2)

with open('menu2.json','wt', newline='') as fout:
    fout.write(menu_json)

#YAML類似JSON 目前不可以用
#如果沒有要自行安裝pip3 install pyyaml
#import yaml

#with open('mcintyre.yaml','rt') as fin:
#    text=fin.read()
#data=yaml.load(text)    
#print(data['details'])
#print(len(data['poems']))
#print(data['poem'][1]['title'])

#設定檔 cfg檔

import configparser
cfg=configparser.ConfigParser()
cfg.read('setting.cfg')
print(cfg)
print(cfg['french'])
print(cfg['french']['greeting'])
print(cfg['files']['bin'])


#其他交換格式 msgpack,protocol buffers,avro,thrift
#把資料結構存成檔案的過程稱為序列化
#pickle 序列化處理

import pickle
import datetime
now1=datetime.datetime.utcnow()
pickled=pickle.dumps(now1)
now2=pickle.loads(pickled)
print(now1)
print(now2)
print(pickled)

class Anon():
    def __init__(self):
     self.foo=''
import pickle
a = Anon()
a.foo = 'bar'
pickled = pickle.dumps(a)
unpickled = pickle.loads(pickled)
print(unpickled.foo)
#pickle可以儲存變數內容(包含格式)十分適合用在中斷回復或傳資料

#二進位讀寫有 HDF5和 XLRD需要的話自己查

#關聯資料庫=>用資料表格式顯示相互關係

#SQL 
#DB-API 提供PYTHON存取各種資料庫
#SQLITE

import sqlite3

conn=sqlite3.connect('enter.db')
curs=conn.cursor()
curs.execute('''CREATE TABLE if not exists zoo (critter VARCHAR(20) PRIMARY KEY,count INT,damage FLOAT)''')
curs.execute('INSERT INTO zoo VALUES("duck",5,0.0)')
curs.execute('INSERT INTO zoo VALUES("BEAR",2,1000.0)')
INS='INSERT INTO zoo (critter,count,damage) VALUES(?,?,?)'
curs.execute(INS,('weasel',1,2000.0))

curs.execute('SELECT * FROM zoo')
rows=curs.fetchall()
print(rows)

curs.execute('SELECT * FROM zoo ORDER BY count')
rows=curs.fetchall()
print(rows)

curs.execute('SELECT * FROM zoo ORDER BY count DESC')
rows=curs.fetchall()
print(rows)

curs.execute('SELECT * FROM zoo WHERE damage =(SELECT MAX(damage) FROM zoo)')
rows=curs.fetchall()
print(rows)
curs.close()

#mysql,postgresql,sqlalchemy
#sqlalchemy ORM?? object relation mapper
#我的理解就是可以快速加入 連結 建立的功能 先不要管以後用到再說

#NOSQL 不支援SQL 有點像是字典?

import dbm
db=dbm.open('define','c')
db['mustard']='yellow'
db['pesto']='green'
print(len(db))
db.close()
db=dbm.open('define','r')
print(db['mustard'])

#memcached
#redis(把資料存在記憶體可以之後玩玩看)
#import redis
#conn=redis.Redis()