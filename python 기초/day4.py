# num = int(input("숫자를 입력하세요: "))

# # if statement
# # num이 홀수라면

# if num % 2 == 1:
#     print('홀수입니다.')
# else:
#     print('짝수입니다')


# 홀수만 들어있는 리스트 만들기

# odd_list = [i for i in range(1, 11) if i % 2 ==1]
# print(odd_list)

# result = ['a', 'b', 'c']
# print(list(enumerate(result)))

# names = ['kai', 'jane', 'bob']
# print(*names)


# def my_function(x, y, z):
#     print(x, y, z)

# dict_values = {'x':1, 'y':2, 'z':3}
# my_function(**dict_values)

# from math import pi, sqrt
# print(pi)
# print(sqrt(4))

# from random import *

# print(randint(1, 10))

# from my_math import add

# print(add(1, 6))

# from my_package.math import my_math
# from my_package.statistics import tools

# print(my_math.add(1, 2))
# print(tools.mod(1,2))

# import requests

# url = "https://random-data-api.com/api/v2/users"
# response = requests.get(url).json()

# print(response)
# print(response['address']['country'])


# print(response.get('address').get('country'))


# def add_numbers(x, y):
#     return x + y

# add_numbers(3, 5)


# dust = int(input())

# if dust > 150:
#     print('매우 나쁨')
# elif dust > 80:
#     print('나쁨')
# elif dust > 30:
#     print('보통')
# else:
#     print('좋음')

# 실습1. 정수를 입력받아 짝수면 'EVEN', 홀수면 'ODD' 출력

# num = int(input())
# if num % 2 == 0:
#     print('EVEN')
# else:
#     print('ODD')

# 실습2. 윤년 판별하기, 윤년이면 'leap year'. 그렇지 않으면, 'common year' 출력
# 윤년의 조건 1. 연도가 4로 나누어 떨어지지만 100으로는 나누어 떨어지면 안된다
# 윤년의 조건 2. 연도가 400으로 나누어 떨어진다

'''
y = int(input())
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print('leap year')
else:
    print('common year')
'''

# 실습1. 구구단 출력
'''
for i in range(2, 10):
    print(f'<{i}단>')
    for k in range(1, 10):
        print(f'{i} X {k} = {i*k}')
'''
# 실습2. 정수 n을 입력 받아 n단의 왼쪽 직각 이등변 삼각형을 그리는 프로그램 작성
'''
n = int(input())

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()
'''


# 실습 1. continue 이용하여 1부터 10까지 정수 중 홀수만 출력


# i = 0
# while i <10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)



# 실습 2. break 이용하여 shall we clos? (y/n) 문구에 y를 입력해야 탈출하고, 'The end'를 출력

'''
while True:
    reply = input('shall we close? (y/n)')
    if reply == 'y':
        print('The end')
        break
'''        

# 실습 3. 정수를 입력받아 그 정수가 몇 자리수 숫자인지 알아내는 프로그램

# n = int(input())
# cnt = 0
# while n>0:
#     cnt += 1
#     n //= 10
# print(cnt)

# 실습 1. 
'''
import math
numbers = [1, 4, 9, 16, 25]
sqrt_numbers = [int(math.sqrt(number)) for number in numbers]
print(sqrt_numbers)
'''
# 실습 2. if 추가해서 짝수만 리스트에 담기

# import math
# numbers = [1, 4, 9, 16, 25]
# sqrt_numbers = [int(math.sqrt(number)) for number in numbers if number % 2 == 0]
# print(sqrt_numbers)
