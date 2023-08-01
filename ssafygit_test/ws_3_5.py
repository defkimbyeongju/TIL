many_user = None
names = ['김시습', '허균', '남영로', '임제', '박지원']
ages = [20, 16, 52, 36, 60]

import book
def rental_book(name, number_of_rental):
    book.decrease_book(number_of_rental)
    print(f"{name}님이 {number_of_rental}권의 책을 대여하였습니다.")
    
def create_user(names, ages):
    user_info = {}
    for i in range(len(names)):
        print(f"{names[i]}님 환영합니다!")
    user_info['name'] = names
    user_info['age'] = ages
    return user_info

user_info = create_user(names, ages)

many_user = list(map(lambda x, y : {'name': x, 'age': y}, user_info['name'], user_info['age']))

for i in range(len(many_user)):
    rental_book(many_user[i]['name'], (many_user[i]['age']//10))

