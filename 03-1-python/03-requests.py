import requests  # requests 라이브러리 설치 필요

r = requests.get(
    'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

# print(rjson)
# print(rjson['RealtimeCityAir']['row'][0]['NO2'])  # 중구의 NO2 값

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    print(gu['MSRSTE_NM'], gu['IDEX_MVL'])


# r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# rjson = r.json()

# gus = rjson['RealtimeCityAir']['row']

# for gu in gus:
#     if gu['IDEX_MVL'] < 60:
#         print (gu['MSRSTE_NM'], gu['IDEX_MVL'])
