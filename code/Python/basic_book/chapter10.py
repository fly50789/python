#系統

import os

def p(func):
    def new_function(*args,**kwargs):
        print("name",func.__name__)
        print("argument",args)
        print("keyword argument",kwargs)
        result=func(*args,**kwargs)
        print("result",result)
        return result
    return new_function


try:
    os.chmod('oops.txt',0o777)
except:
    pass

fout=open('oops.txt','wt')
#下方為特殊寫法要記
print('creat a file ',file=fout)
fout.close()

print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.txt'))
print(os.path.exists('waffles'))
#.代表當層目錄 .. 上層目錄
print(os.path.exists('.'))
print(os.path.exists('..'))

name='oops.txt'
print(os.path.isfile(name))
print(os.path.isdir(name))
print(os.path.isdir('..'))

print('abs test:',os.path.isabs(name))
#目錄一律用 /表示
print('abs test:',os.path.isabs("c:/"))

import shutil
shutil.copy('oops.txt','oops1.txt')
#move會刪除原本檔按
#shutil.move('oops.txt','oops1.txt')

#link看不懂有啥用?
#os.link('oops.txt','yikes.txt')
print(os.path.isfile('yikes.txt'))
#symlink類似建立桌面捷徑 可以任意命名
print(os.path.islink('yikes.txt'))
#os.symlink('oops.txt','jeepers.txt')
print(os.path.islink('jeepers.txt'))
#chmod更改權限
os.chmod('oops.txt',0o777)
#stat有放很多常數
import stat
#找不到下面常數可能是unix獨有?
#os.chmod('oops.txt',stat,S_IRUSR)

uid=5
gid=22
#變更擁有權 unix,mac獨有
#os.chown('oops',uid,gid)


print(os.path.abspath('oops.txt'))
#realpath用來取 symlink 但不知道為什麼顯示錯誤...
print(os.path.realpath('jeepers.txt'))

os.remove('oops.txt')

#os.mkdir('poems')

os.mkdir('poems') if not os.path.exists('poems') else 1







print(os.path.exists('poems'))


try:
    os.rmdir('poems')
except:
    pass

print(os.path.exists('poems'))



try:
    os.mkdir('poems')
except:
    pass

print(os.listdir('poems'))



try:
    os.mkdir('poems/mcintyre')
except:
    pass


fout= open('poems/mcintyre/test.txt','wt')
fout.write('this is a simple test')
fout.close()

print(os.listdir('poems/mcintyre'))

#更換目前位置
os.chdir('poems')
print(os.listdir('.'))

import glob
#非正規表示法搜尋
#只有*? [abc] [!abc]
print(glob.glob('m*'))
print(glob.glob('??'))
print(glob.glob('m?????e'))
print(glob.glob('[klm]*e'))


print(os.getpid())
#取當前位置
print(os.getcwd())
#unix 獨有
#print(os.getuid())
#print(os.getgid())

import subprocess
ret=1
#ret = subprocess.getoutput('date')
#binary輸出不知道為啥不能用?
#ret = subprocess.check_output(['data'])

print(ret)
#list輸出
#ret = subprocess.getstatusoutput('date')

print(ret)
#退出的狀態 不能用
#ret = subprocess.call('date')
print(ret)

#multiprocessing 請看 temp.py




import calendar
#閏年判定
print(calendar.isleap(1900))

from datetime import date
halloween =date (2014, 10, 31)
print(halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)

now=date.today()

print(now)
      
from datetime import timedelta
#這代表時間運算不能直接+-
one_day = timedelta(days=1)
tomorrow=now+one_day
print(tomorrow)

from datetime import time
noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)


from datetime import datetime

someday=datetime(2014,1,2,3,4,5,6)
print(someday)
print(someday.isoformat())

now=datetime.now()
print(now)

from datetime import datetime,time,date
noon=time(12)
thisday=date.today()
noon=datetime.combine(thisday,noon)
print(noon)
print(noon.date())
print(noon.time())


import time
#utc
now=time.time()
print(now)
#c time會幫忙轉換\
print(time.ctime(now))
#local
tm=time.localtime(now)
print(tm)
print(time.mktime(tm))
#建議用utc就好

#時間格式
# %Y年 %m月 %B月名稱 %b月縮寫
#%H %M %S 時分秒 還有很多自己查

fmt="STRUCTURE %A %B %d %Y,LOCAL %I:%M:%S%p"
t=time.localtime()
#strftime
print(time.strftime(fmt,t))
someday= date(2014,7,4)
print(someday.strftime(fmt))
from datetime import time
sometime=time(10,35)
print(sometime.strftime(fmt))

import time
fmt="%Y-%m-%d"
print('strp:',time.strptime('2012-01-29',fmt))


#locale.setlocale(locale.LC_TIME,"LANG COUNTRY")
#import locale
#name=locale.locale_alias.key() 區域瑪