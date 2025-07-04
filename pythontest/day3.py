'''
#输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出。
sentence = input("请输入一段话：")
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch,0) + 1
sorted_keys = sorted(counter,key=counter.get,reverse=True)
for key in sorted_keys:
    print(f'{key}出现了{counter[key]}次')



#在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)


#设计一个函数，传入任意多个参数，对其中int类型或float类型的元素实现更多的甚至是自定义的二元运算
def calc(init_value,op_func,*args,**kwargs):   #接收一个初始值 init_value 和一个操作函数 op_func  通过 *args 和 **kwargs 接收任意数量的位置参数和关键字参数
    items = list(args) + list(kwargs.values())  #将所有参数合并成一个列表 items，并遍历其中的数值（int 或 float
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)   #使用 op_func 对 init_value 和每个数值进行计算，最终返回结果。
    return  result

def add(x,y):
    return x + y

def mul(x,y):
    return x *y

print(calc(1,mul,1,2,3,4,5))



#Lambda函数
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(lambda x:x ** 2, filter(lambda x:x % 2 == 0,old_nums)))
print(new_nums)

'''

import random
import time

def download(filename):
    #下载文件
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

def upload(filename):
    #上传文件
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')