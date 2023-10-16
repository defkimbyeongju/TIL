'''
class Person:
    # 속성(변수)
    blood_color = 'red'

    # 메서드
    def __init__(self, name): # __는 매직 메서드라고 하는데, 이는 개발자가 직접 호출 x. 
                              # init은 초기화하면서 시작한다는 의미. 생성자 메서드.
        self.name = name      # self는 인스턴스 자기 자신을 의미함
    
    def singing(self):
        return f'{self.name}가 노래합니다.'
    
# 인스턴스 생성
singer1 = Person('iu') # name 위치인자가 하나 필요함. 
singer2 = Person('BTS')

# singer1,2는 독립적임.

# 메서드 호출
print(singer1.singing())
print(singer2.singing())
print(singer1.blood_color)
print(singer2.blood_color)
'''

'''
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk() # unknown으로 출력됨. name을 설정하지 않으면 
p1.address = 'Korea' # 다른 속성도 추가 가능함. 클래스는 공통의 공간일 뿐. 다만, 인스턴스에서 메서드(행동)을 만들 수는 없음
print(p1.address)

p2 = Person()
p2.name = 'Kim'
p2.talk()

# p3 = Person('Lee') # 오류가 발생. 그 이유는 클래스의 메서드에서 self 이외에 위치 인자를 설정하지 않았기 때문!
# p3.talk()
'''

# class Person:
#     name = 'kai' # 클래스 변수 == 멤버 변수

# 실습1. 클래스 변수에 접근하여 kai 출력

# p1 = Person()
# print(p1.name)
# print(Person.name)


# class Person:
#     def say(self): # 인스턴스 메서드
#         print("Welcome.")

# # 실습2. say()메서드를 호출
# kai = Person() # 인스턴스 생성부터
# kai.say() # 인스턴스 메서드 호출


# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def say(self):
#         print(f'Welcome. {self.name}')

# kai = Person('kai')
# kai.say()


# 클래스 -> Car
# 객체 -> Hyundai, Kia, Ssangyong

# class Car:
#     model = 'Sonata'
#     color = 'white'

#     def speedchange(self, v):
#         print(f'speed : {v}')
#         self.speed = v

# # Sonata, white, speed : 80 출력

# Hyundai = Car() # 인스턴스 생성
# print(Hyundai.model) # 클래스 변수에 접근
# print(Hyundai.color) # 22
# Hyundai.speedchange(80) # 인스턴스 메서드 호출

# ---> 생성자 메서드 구조로 바꾸기
# model : sonata, color : white, speed : 80

# class Car:

#     def __init__(self, model, color, speed):
#         self.model = model
#         self.color = color
#         self.speed = speed
#     def info(self):
#         print(f'model : {self.model}, color : {self.color}, speed : {self.speed}')

# hyundai = Car('sonata', 'white', 80)
# hyundai.info() # 인스턴스.메서드()

# class Singer:
#     def __init__(self, job, birthday, country):
#         self.job = job
#         self.birthday = birthday
#         self.country = country

#     def rap(self):
#         print(f'직업이 {self.job}이기 때문에 랩을 한다')

#     def dance(self):
#         print(f'직업이 {self.job}이기 때문에 춤을 잘춰야 한다')

#     def cow(self):
#         print(f'{self.country} {self.job}들은 소몰이 창법을 사용한다')


# iu = Singer('singer', '1993-05-16', 'Korea')
# iu.name = "아이유"
# iu.rap()
# iu.dance()
# iu.cow()


# class Person():
#     count = 0 # 클래스 변수

#     def __init__(self, name):  # 생성자 함수
#         self.name = name # 인스턴스 변수
#         Person.count += 1

# # 인스턴스를 생성할 때마다 count가 1씩 증가
# person1 = Person('에스파')
# person2 = Person('BTS')

# print(Person.count)

# class Singer:
#     job = '가수'
#     birthday = "1993-05-16"
#     country = "Korea"
    
#     @staticmethod
#     def rap():
#     print('랩')
    
#     @staticmethod
#     def dance():
#         print(f'댄스')
    
#     @staticmethod
#     def cow():
#         print('소몰이 부르기')
    
# Singer.dance()

    
