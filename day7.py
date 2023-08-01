# my_dict = {
#     'name' : 'Alice',
#     'age' : 25
# }

# for key in my_dict.keys():
#     print(key)

# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     print(key, value)

# print(my_dict.pop('age'))



# my_dict .setdefault('country', 'Korea')
# print(my_dict)


# 딕셔너리 키에 따른 값을 조회할 때, [], .get(), .setdefault()는 문제만 없다면 모두 같은 기능을 함

blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

from collections import Counter
c = Counter(blood_types)
print(c)

# []
# new_dict = {}
# for blood_type in blood_types:
#     if blood_type not in new_dict: # 기존에 키가 존재하지 않는다면 값을 1로 설정
#         new_dict[blood_type] = 1
#     else: # 키가 존재한다면 1 증가시키기
#         new_dict[blood_type] += 1
# print(new_dict)

#  .get()
# new_dict = {}
# for blood_type in blood_types:
#      new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
# print(new_dict)

# .setdefault
# new_dict = {}
# for blood_type in blood_types:
#       new_dict.setdefault(blood_type, 0)
#       new_dict[blood_type] += 1
# print(new_dict)

# import copy

# original_list = [1, 2, [1,2]]
# deep_copied_list =copy.deepcopy(original_list)
# deep_copied_list[2][0] = 999

# print(original_list, deep_copied_list)


# 세트 가변형 비시퀀스 -> 중복을 허용하지 않는다 -> 집합과 같은 특징
'''
list1 = [1,2,3,4]
list2 = [4,5,6,7,8,9]
set1 = set(list1)
set2 = set(list2)

# 1. set1에 4추가
set1.add(4)
print(set1)
# 2. set1에 [5,6,7] 추가
set1.update([5,6,7])
print(set1)
# 3. set1에서 7제거(2가지 방법)
set1.remove(7)
set1.discard(7)
print(set1)
# 4. set1에서 차집합 set2
print(set1.difference(set2))
# 5. set1 교집합 set2
print(set1.intersection(set2))

# 6. set1 합집합 set2
print(set1.union(set2))
'''

# set1.pop() -> 주소값이 작은 것부터 제거


# english_korean = {
#     'plus' : ['더하기', '장점'],
#     'minus' : ['빼기', '적자'],
#     'multiply' : ['곱하기', '다양하게'],
#     'division' : ['나누기', '분열']
# }

# 1번 문제. 영어 단어를 입력하면 단어의 뜻을 보여주는 프로그램(3가지 방법)
# word = input()
# print(english_korean[word])
# print(english_korean.get(word))
# print(english_korean.setdefault(word))


# 2번. 영한사전에서 단어들의 목록을 출력
# print(english_korean.keys())

# 3번. 단어와 뜻을 추가하고, 사전에 있는 모든 단어와 뜻을 출력(3가지 방법)

# english_korean.setdefault('square', ['제곱', '사각형'])
# english_korean['square'] = ['제곱', '사각형']
# my_dict = {'square': ['제곱', '사각형']}
# english_korean.update(my_dict)
# print(english_korean)


# 3번. 입력받은 단어와 뜻 모두 삭제
# word = input()
# english_korean.pop(word)
# del english_korean[word]
# print(english_korean)
# def add_item_to_dict(dict1, key, value):
#     new_dict = dict1.copy()
#     new_dict.setdefault(key, value)
#     return new_dict

# my_dict = {'name': 'Alice', 'age': 25}
# result = add_item_to_dict(my_dict, 'country', 'USA')
# print(result)

# 할당은 메모리 주소가 같다.
# list1 = [1, 2, 3, 4]
# list2 = list1
# list2[0] = 5
# print(id(list1))
# print(id(list2))
# print(list1, list2)

# 얕은 복사
# list1 = [1, 2, [3,4]]
# list2 = list1[:]
# list2 = list1.copy()

# list2[0] = 5
# list2[2][0] = 5
# print(id(list1[2]), id(list2[2]))

# print(list1, list2)

# 깊은 복사
import copy
list1 = [1, 2, [3,4]]
list2 = copy.deepcopy(list1)

list2[2][0] = 5
print(id(list1[2]), id(list2[2])) # 메모리 주소가 다르다.

print(list1, list2)