# 함수 정의, 함수 선언


'''
def 함수명(매개변수):
    code....
    code....  # 함수 바디

    return 반환값
'''

# 함수 호출

'''
함수명(함수 인자)

매개변수, 반환값은 있을수도 있고, 없을수도 있음 --> 총 4가지 유형의 함수가 존재
'''

# def get_sum(num1, num2):
#     return num1+num2

# num1 = 5
# num2 = 3
# result = get_sum(num1, num2)
# print(result)

# 1. 매개변수가 없는 함수로 변형
# def get_sum():
#     num1 = 5
#     num2 = 3
#     return num1 + num2
# print(get_sum())



# 2. return 반환값이 없는 함수로 변형


# 3. 기본 인자 -> default인자는 반드시 뒤에서부터 할당

# def greet(name, age = 40):
#     print(f'안녕하세요, {name}님! {age}살 이시군요.')

# greet("원빈")


# 4. 키워드 인자 => 키워드 인자와 위치인자는 같이 사용할 수 없다.

# def greet(name, age):
#     print(f'안녕하세요. {name}님! {age}살 이시군요!')

# greet(age =33)

# # 5번 가변인자 목록. 튜플로 반환
# def calculate_sum(*args):
#     print(args)
#     total = sum(args)
#     print(f'합계: {total}')
# calculate_sum(1, 2, 3, 4, 5)

# 6번 가변 키워드 인자. 딕셔너리로 반환
# def print_info(**kwargs):
#     print(kwargs)

# print_info(name='Eve', age=30, height=175.3)

'''
def outer():
    x = 1 # outer 함수 기준으로는 local 변수, inner 함수 기준으로는 enclosed scope
    def inner():
        y = 2 # local 변수
        result = x + y # x는 로컬 안에 없으니까 enclosed scope으로 올라가서 x 찾음
        print(result)
    inner()

outer() # 헷갈려서 이렇게 사용하는걸 권장하지는 않음
'''

# built-in scope -> 내장함수 len(), print(), input() 등등

'''
list_1 = [1, 2, 3, 4]
print(sum(list_1)) # sum은 built-in 

sum = 5 # global
print(sum) 
print(sum(list_1))
'''

# LEGB Rule
'''
a, b, c = 1, 2, 3

def enclosed():
    a, b, c = 4, 5, 6
    def local():
        print(a, b, c) # 4, 5, 500
    local(500) 
    print(a,b,c) # 4, 5, 6
enclosed()
print(a,b,c) # 1, 2, 3
'''

# 재귀함수 -> 자기 자신을 호출하는 함수(※주의: 종료 조건을 반드시 포함)
# 예시
'''
def factorial(n):
    if n == 0:
        return 1  # 종료조건 명시
    return n * factorial(n-1)  # 반복되는 호출이 종료조건을 향하도록

print(factorial(10))
'''

# map(function, iterable)
# a = list(map(int, input().split()))


# zip(*iterables) -> iterables를 튜플을 원소로 하는 zip 객체 반환

'''
names = ['kai', 'jane', 'bob']
ages = [30, 31, 27]
cities = ['seoul', 'london', 'paris']

for name, age, city in zip(names, ages, cities):
    print(f'저는 {name}이고, {age}세이고, {city}에 살고 있습니다.')
'''

# lambda 함수 -> lambda 매개변수: 표현식. 1회성이기 때문에 함수명 필요 없음
# map 함수를 사용하여 numbers 리스트의 요소가 제곱된 값들로 이루어진 새로운 리스트 생성

'''
numbers = [1, 2, 3, 4, 5]
sqrt_list = list(map(lambda x: x**2, numbers))
print(sqrt_list)
'''