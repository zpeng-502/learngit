import math
# 将华氏温度转换为摄氏温度
'''
f = float(input('请输入华氏温度:'))
c = (f-32) / 1.8
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')


#输入半径计算圆的周长和面积
p = math.pi
radius = float(input('请输入半径：'))
perimeter = 2 * p * radius
area = p * radius * radius
print(f'{perimeter = :.2f}')
print(f'{area =:.2f}')


#输入一个 1582 年以后的年份，判断该年份是不是闰年

year = int(input("请输入年份："))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 ==0
print(f'{is_leap = }')

'''
#match-case

status_code = int(input('响应码状态：'))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _:   description = 'Unknown Status Code'
print('状态码描述：',description)
