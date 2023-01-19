fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']


def count_fruits(target):
    count = 0
    for fruit in fruits:
        if fruit == target:
            count += 1
    print(count)


count_fruits('사과')

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]


def get_age(name):
    for person in people:
        if person['name'] == name:
            return person['age']


print(get_age('bob'))
