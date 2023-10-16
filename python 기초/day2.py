# 진법 변경

# print(bin(12))
# print(oct(12))
# print(hex(12))

# f-string 응용
# greeting = 'hi'
# print(f'{greeting:^10}') # 총 10칸 중에 가운데를 차지하겠다.
# print(f'{greeting:>10}') # 총 10칸 중에 오른쪽을 차지하겠다. 


# decimal = 10

# # 2진수로
# binary = bin(decimal) 
# print(binary[2:])
# # 8진수로
# octal = oct(decimal)
# print(octal[2:])
# # 16진수로
# hexa = hex(decimal)
# print(hexa[2:])

# a = 3.2 - 3.1
# b = 1.2 - 1.1

# #부동 소수점 값 출력할 때 f-string 활용하여 정확도 제어 가능

# num_a = f'{a: .1f}'
# num_b = f'{b: .1f}'
# print(num_a, num_b)

# print(314e-2)
# # 산술 연사자를 사용하여 표현식을 바꿔보기
# print(314 * 10**-2)

# greeting = 'hi'
# print(f'{greeting:^10}') # 총 10칸 중에 가운데를 차지하겠다. 가운데 정렬
# print(f'{greeting:>10}') # 총 10칸 중에 오른쪽 끝부분을 차지하겠다. 우측 정렬
# print(f'{greeting:<10}') # 총 10칸 중에 왼쪽 끝부분부터 차지하겠다. 좌측 정렬

# hw = "hello world"

# # 1. 인덱싱 -> 알파벳 w를 출력
# print(hw[6])
# # 2-1. 슬라이싱 -> hello를 출력
# print(hw[:5])
# # 2-2. 슬라이싱 -> world를 출력
# print(hw[6:])
# # 2-3. 슬라이싱 -> 거꾸로 출력
# print(hw[::-1])
# # 3. 내장함수를 사용해서 문자열의 길이를 출력
# print(len(hw))
# # 4. for 문을 활용하여 hello world 출력(2가지 방법)
# for i in hw:
#     print(i, end='')
# print()
# for i in range(len(hw)):
#     print(hw[i], end='')

# for k in hw:
    
'''
깨알 vs code 단축키: 동일한 문자를 여러곳에 채워넣을 때 alt를 누른 상태로 커서를 주면 여러 군데가 선택됨
'''


# print('다음은 이형기 시인의 "낙화"의 한 구절이다.\n- 1연\n    가야할 때 언제인가를\n    분명히 알고 가는 이의\n    뒷모습은 얼마나 아름다운가.\n\n나는 이 시를 보며 \'나는 내가 가야할 때가 언제일까?\' 를 생각해 보았다.')
# author_1 = '권필'
# author_2 = '허균'
# book_1 = '주생전'
# book_2 = '홍길동전'

# print(f'{book_1}의 작가는 {author_1}이고,\n{author_2}는 {book_2}를 집필하였다.')

# array = [[1,2,3], [4,5,6], [7,8,9]]

# # 3출력
# print(array[0][2])3

# # 7출력
# print(array[2][0])


# 2차원 리스트를 입력 받는 방법
# rows = int(input('행의 개수를 입력하세요.'))
# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)
# for row in rows:
#     print(row)


# 튜플 사용 예시: 방향배열

# def move_arround(position):
#     x, y = position
    # directions = [(0, 1), (0,-1), (1,0), (-1,0)] # 상, 하, 우, 좌
    # directions = [(-1,1), (1, -1), (1,1), (-1,-1)] # 대각선 방향

# range 함수
# range(start, end, step)
# start > end: start부터 end+1까지 step만큼 감소


# my_dict = {
#     'a1' : {'b1' : 1, 'b2' : 2, 'b3' : 3},
#     'a2' : {'b1' : 4, 'b2' : 5, 'b3' : 6},
#     'a3' : {'b1' : 7, 'b2' : 8, 'b3' : 9},
# }

# print(my_dict['a2']['b2'])
# print(my_dict.get('a2').get('b2'))

# set_1 = {1, 2, 3, 4, 5, 6}
# set_2 = {4,5,6,7,8,9}

# print(set_1|set_2)

# print(set_1 - set_2)

# print(set_1&set_2)


# 세트의 사용 예시: 로또 번호 추첨
# import random

# lotto = set()

# while len(lotto) < 6:
#     number = random.randint(1, 45)
#     lotto.add(number)

# lotto_list = list(lotto)
# lotto_list.sort()
# print(lotto_list)


# numbers = [1, 2, 3, 4, 5]

# total = 0

# for num in numbers:
#     total += num

# print(total)

# vowels = 'aeiou'

# # print(('a' and 'b') in vowels)
# # print(('a' or 'b') in vowels)

# print(3 and 5)
# print(3 and 0)
# print(0 and 3)
# print(0 and 0)

# print(5 or 3)

