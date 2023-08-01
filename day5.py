import requests

# url = 'https://fakestoreapi.com/carts'

# response = requests.get(url)

# print(response.json())


# import json # 내장 모듈

# json_data = '''
# {
#     "name" : "김싸피",
#     "age" : 28,
#     "hobbies" : [
#         "공부하기",
#         "복습하기"
#     ]

# }

# '''

# data = json.loads(json_data)

# name = data.get('name')
# print(name)

api_keys = 'f6dc324db5555a1227df37593b5dc10c'

lat = 37.56

lon = 126.97

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_keys}'

response = requests.get(url)

print(response.json())