# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def talk(self):
#         print(f'안녕, {self.name}입니다.')


# class Professor(Person):
#     def __init__(self, name, age, department):
#         super().__init__(name, age)
#         self.department = department

# class Student(Person):
#     def __init__(self, name, age, gpa):
#         super().__init__(name, age)
#         self.gpa = gpa
    
# p1 = Professor('박교수', 49, '컴공')
# s1 = Student("김학생", 20, 3.5)

# p1.talk()
# s1.talk()

# try:
#     num = int(input('100으로 나눌 값을 입력하시오 : '))
#     print(100 / num)
# except ValueError:
#     print('숫자를 입력하라고')
# except ZeroDivisionError:
#     print('왜 0을 입력하는거야? 빡대가리야?')

# except:
#     print('에러 발생함')


# 클래스 Car 정의, 부모클래스

# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
    
#     def info(self):
#         print(f'Model : {self.model}, color : {self.color}')

# class CarDrive(Car):
#     def speedchange(self, speed):
#         self.speed = speed
#         print(f'speedchange : {self.speed}')

# # info 메서드 호출
# kia = CarDrive('sorento', 'green')
# kia.info()

# # speedchange 메서드 호출
# kia.speedchange(100)


# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

# class CarDrive(Car):
#     def __init__(self, model, color, speed):
#         super().__init__(model, color)
#         self.speed = speed

#     def info(self):
#         print(f'model : {self.model}, color : {self.color}, speed : {self.speed}')

# # info 메서드 호출

# tesla = CarDrive('mars', 'blue', 500)
# tesla.info()

# class Car:
#     def __init__(self, model):
#         self.model = model
# class Hyundai(Car):
#     color = 'white'
#     def speed(self):
#         return '80km/h'

# class Kia(Car):
#     color = "black"
#     def engine(self):
#         return "1.6 turbo"
    
# class CarDrive(Hyundai, Kia):
#     def speed(self):
#         return '100km/h'
    
#     def power(self):
#         return '1.999cc'
# print(CarDrive.mro())    
# # speed 메서드 호출
# musk = CarDrive('mars')
# print(musk.speed())
# # engine
# print(musk.engine())
# # power
# print(musk.power())
# # color
# print(musk.color)



# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

#     def info(self):
#         print(f'Model : {self.model}, color : {self.color}')

# class CarDrive(Car):
#     # 실습 1. info 메서드를 오버라이딩
#     def info(self):
#         print(f'Model명은 {self.model}이고, 색상은 {self.color}입니다.')

# samsung = CarDrive('galaxy', 'purple')

# samsung.info()

# print(CarDrive.mro())

def calculate_sum(a, b):
    return a+b

numbers = [1, 2, 3, 4, 5]

total_sum = 0
for i in range(len(numbers)):
    total_sum = calculate_sum(total_sum, numbers[i])
print(f"종합 : {total_sum}")