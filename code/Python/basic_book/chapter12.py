# pylint pyflakes pep8 三個套件可以檢查語法


#unittest可以用assert搭配去看看輸出是否正確
#doctest比較方便可以在docstring裡面去撰寫測試
#nose 替代unuttest的方案
#用裝飾器來除錯顯示完整的資訊

#pdb=>有ide了我暫時不想用這個



#計時

from time import time,sleep
t1=time()
a=5
a*=2
sleep(0.001)
print(t1)
print(time()-t1)

#from timeit import timeit
#可以repeat數次執行(部過我覺得用上面那個就好)

#print test

s=print("abc")
print(s)
test_file=open('log.txt','wt')

print("123",file=test_file)
print("123")
test_file.close()

#logging
#debug info warn error critical

import logging
#logging.basicConfig(filename='log_examp.log',level=logging.WARN)
#logging.basicConfig(filename='log_examp.log',level=logging.INFO)
logging.basicConfig(level=logging.INFO)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')




import logging

logger = logging.getLogger()  # 不加名称设置root logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

# 使用FileHandler输出到文件
fh = logging.FileHandler('log.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# 使用StreamHandler输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# 添加两个Handler
logger.addHandler(ch)
logger.addHandler(fh)
logger.info('this is info message')
logger.warn('this is warn message')

#docstring test
import docstring

docstring.test("123")
print(docstring.test.__doc__)
help(docstring.test)