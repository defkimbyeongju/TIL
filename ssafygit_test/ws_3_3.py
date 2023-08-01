# import book
# def rental_book(name, number_of_rental):
#     book.decrease_book(number_of_rental)
#     print(f"{name}님이 {number_of_rental}권의 책을 대여하였습니다.")
    
# rental_book('홍길동', 3)


    
def create_user(names, ages, addresses):
    user_info = {}
    person_dicts = {}
    for i in range(len(names)):
        print(f"{names[i]}님 환영합니다!")
    user_info['name'] = names
    user_info['age'] = ages
    user_info['address'] = addresses
    person_dicts = map(lambda x, y, z: {'name': x, 'age': y, 'address': z}, 
                        user_info['name'], user_info['age'], user_info['address'])
    return list(person_dicts)

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


print(create_user(name, age, address))
