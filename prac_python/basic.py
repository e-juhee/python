a = 3
print(a)
b = a
print(b)
a = 5
print(a, b)

name = 'juhee'
name.upper()
print(name)  # juhee
print(name.upper())  # JUHEE

a = True
b = False

print(not a)  # False
print(a and b)  # False
print(a or b)  # True

# 리스트
a_list = []
a_list.append(2)
print(a_list)  # [2]
print(len(a_list))  # 1

# 리스트 덧셈/곱셈
a = [3, 3, 1]
b = [5, 2]
print(a+b)  # [3, 3, 1, 5, 2]
print(a*2)  # [3, 3, 1, 3, 3, 1]

# 딕셔너리
a_dict = {}
a_dict = {'name': 'juhee', 'age': 25}
a_dict['height'] = 168
print(a_dict)  # {'name': 'juhee', 'age': 25, 'height': 168}

# 함수


def f(x):
    return 2*x+3


print(f(2))  # 7


def sum(a, b):
    return a+b


print(sum(1, 2))  # 3


# 조건문
def is_adult(age):
    if age > 20:
        print('성인입니다')
    elif age >= 13:
        print('청소년이에요')
    else:
        print('어린이네요!')


is_adult(30)  # 성인입니다


# 반복문
fruits = ['사과', '배', '감', '귤']

for fruit in fruits:
    print(fruit)
