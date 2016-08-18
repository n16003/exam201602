import math
from datetime import date



# 'hello, {name}!'と出力してください 。
def hello(name):
    print('hello, ' + name + '!')


# sentence の文字数を出力してください
def length(sentence):

    print(len(sentence))


# sentence の2文字目から5文字目まで(5文字目は含まない)を出力してください
def slicing2to5(sentence):

    print(sentence[2:5])

# number の符号を出力してください。ただし、0は'0'と出力してください
def number_sign(number):

    if number == 0:
        print("0")
    elif number > 0:
        print("+")
    else:
        print("-")

# number が素数なら'ok',そうでないなら'ng'と出力してください
def prime_number(number):
    count = 0
    for i in range(1,number):
        if number % i == 0:
            count+=1
    print('{0}'.format('ok' if count == 1 else 'ng'))


# 1からnumberまでの合計を出力してください

def sum_from_1_to(number):
    total = 0
    for i in range(1,number+1):
        total += i
    print(total)

# numberの階乗(factorial)を出力してください
def factorial(number):
    fac = 1
    for i in range(1,number+1):
        fac *= i
    print(fac)

# リストdataの各要素(整数)を3乗した結果をリスト型として返してください
def cubic_list(data):
    a = [x ** 3 for x in data]
    return a

# 底辺x,高さyの直角三角形(right angled triangle)の残り1つの辺の長さを返してください
def calc_hypotenuse(x, y):
    a = math.sqrt(x ** 2 + y ** 2)
    return a


# 底辺x,斜辺vの直角三角形の残り1つの辺の長さを返してください
def calc_subtense(x, v):
    a = math.sqrt(v ** 2 - x ** 2)
    return a

# 三辺の長さがそれぞれx,y,zの三角形の面積を返してください
def calc_area_triangle(x, y, z):
    s =(x + y + z) / 2
    a = math.sqrt(s *((s-x)*(s-y)*(s-z)))
    return a

# 引数a,b,cを小数点以下2桁表示で空白切りで表示してください
def point_two_digits(a, b, c):
    A =format(a,'.2f')
    B =format(b,'.2f')
    C =format(c,'.2f')
    print(A,B,C)
# リストdataの内容を小さい順でソートした結果を返してください
def list_sort(data):
    data.sort()
    a = data
    return a




# 文字列の並びを逆にしたものを返してください
def reverse_string(sentence):
    a = sentence[::-1]
    return a


# dateから2016年4月1日までの日数を返してください
def days_from_date(point):
    now = date(2016, 4, 1)
    a = now - point
    x = a.days
    return x