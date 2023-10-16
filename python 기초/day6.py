# ws_5_5.py

# 아래 함수를 수정하시오.
# def even_elements(input_list):
#     even_list = []
#     for i in range(len(input_list)):
#         if b[i] % 2 == 0:
#             new_list.extend([input_list.pop(i)])
#     return new_list

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)


# a = "Practice makes perfect"

# #1. 문자열 a에서 'e'의 개수 세기
# print(a.count('e'))
# #2. 문자열 a에서 'i'의 위치 찾기(2가지 방법)
# print(a.find('i')) # 'i'가 존재하지 않으면 -1 반환
# print(a.index('i')) # 'i'가 존재하지 않으면 에러
# #3. 문자열 a의 문자 사이에 .(점) 삽입
# print('.'.join(a))
# #4. 문자열 a를 공백 기준으로 분리하여 출력
# print(a.split())
# #5. 문자열 a에서 'makes'를 'made'로 바꿔서 출력
# print(a.replace('makes', 'made'))

# # 6. 문자열 a를 대문자와 소문자로 변환하여 출력
# print(a.lower())
# print(a.upper())

# #7. 문자열 a에서 양쪽 공백 삭제하기
# print(a.strip())



a = ['b', 'a', 'n', 'a', 'n']

# 반환하지 않는 메서드(void methods) -> 주로 원본을 변경한다
# 리스트 맨 마지막에 'a'추가하고 출력
a.append('a')
print(a)

# 리스트 a를 오름차순으로 정렬, a출력
a.sort()
print(a)
# 리스트 a를 내림차순으로 정렬, a출력
a.sort(reverse=True)  # sort()는 원본을 변경하지만, sorted()는 원본을 변경하지 않는다. 
print(a) 
# 리스트 a를 역순으로 뒤집기, a출력
a.reverse()
print(a)
# 리스트 a에서 문자 'a' 삭제하기, a출력
a.remove('a')
print(a)

# 반환하는 메서드(Return methods) -> 주로 원본을 변경하지 않는다
# 리스트 a의 마지막 요소를 꺼내서 삭제하고 출력
print(a.pop())
# 리스트 a에서 문자 'n'의 개수를 출력
print(a.find('n'))