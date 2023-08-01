import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

dummy_data = []
for i in parsed_data:
    lat = float(i['address']['geo']['lat'])
    lng = float(i['address']['geo']['lng'])
    if -80 < lat < 80 and -80 < lng < 80:
        dummy_data.append({'company': i['company']['name'], 'lat': i['address']['geo']['lat'], 
                           'lng':i['address']['geo']['lng'], 'name':i['name']})


def create_user(lst):
    censored_user_list = []
    for k in lst:
        censored_user_list.append({k['company']: k['name']})
    print(censored_user_list)


def censorship(list):
    black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']
    not_black = []
    for j in list:
        if j['company'] in black_list:
            print(f"{j['company']} 소속의 {j['name']} 은/는 등록할 수 없습니다. ")
        else:
            print('이상 없습니다')
            not_black.append(j)
    # print(not_black)
    create_user(not_black)

censorship(dummy_data)