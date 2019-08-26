#兩種方法
#有指令哪個modular就可以直接使用等同在原本位置寫上function
def get():
    from random import choice
    possible=['rain','snow','sleet','fog']
    return choice(possible)

import random
def get2():
     possible=['rain','snow','sleet','fog']
     return random.choice(possible)