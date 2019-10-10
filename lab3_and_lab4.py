import random

# 1
prise = [2, 3, 4, 5, 6]
goods = ['banana', 'apple', 'kiwi', 'cucumber', 'tomato']
prise_goods = list(zip(goods, prise))
# print(prise_goods)
print(f'first item - {list(prise_goods[0])}')
[print(list(i)) for i in prise_goods]
print(len(prise_goods))

# 2
commodity, size = input().split()
[print(i[1] * int(size)) for i in prise_goods if commodity == i[0]]

a = [input() for i in range(int(input()))]
print(a)

full_lst = [(item[0],) for i, item in enumerate(prise_goods)]
print(full_lst)

full_lst = []
for i in range(int(input())):
    name, count = input().split()
    for j in prise_goods:
        if name in j:
            full_lst.append((name, int(count) * j[1]))

total_sum = sum([i[1] for i in full_lst])
print(*full_lst, f'Total - {total_sum}', sep='\n')

# 3


first_name = ["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina",
              "paul", "ringo", "ally", "nicky", "cam", "ari", "trudie", "cal",
              "carl", "lady", "lauren", "ichabod", "arthur", "ashley", "drake",
              "kim", "julio", "lorraine", "floyd", "janet", "lydia", "charles",
              "pedro", "bradley"]

generate_evaluation = [
    [random.randrange(40, 100) for i in range(random.randrange(5, 10))] for j
    in
    range(10)]

students_dict = dict(zip(first_name, generate_evaluation))

lst_name_students = [k for k, v in students_dict.items()]
print(*lst_name_students)


def average(lst: list) -> int:
    return round(sum(lst) / len(lst), 2)


print()
average_lst = map(average, students_dict.values())
for i in average_lst:
    print(i, end=' ')

print()
count = 0
students_evaluate = [i for i in students_dict.values()]
dict_arreas = {}

for number, i in enumerate(students_evaluate):
    count = 0
    for n, j in enumerate(i):
        if j < 50:
            count += 1
    dict_arreas[lst_name_students[number]] = count

print(dict_arreas)

st_average = zip(lst_name_students, map(average, students_dict.values()))
print(dict(st_average))

# 3
group = [{'surname': 'liv', 'name': 'vavmaria', 'marks': [5, 5, 4]},
         {'surname': 'ddassdliv', 'name': 'masadasdria', 'marks': [15, 25, 4]},
         {'surname': 'lidadv', 'name': 'masdasaria', 'marks': [53, 52, 24]},
         {'surname': 'liasdasdv', 'name': 'maasdasdria',
          'marks': [54, 52, 24]},
         {'surname': 'gwgliv', 'name': 'mawwria', 'marks': [5, 53, 43]}, ]

print(group)
print(group[0].values())
for i in group:
    print(i['surname'].ljust(18, '.'), i['name'].ljust(15, '.'), i['marks'])

average_all = []
for i in group:
    average_all.append(average(i["marks"]))
    print(f'{i["surname"]} ------ {average(i["marks"])}')

lst_last_name = [i['surname'] for i in group]
average(average_all)

# 4
lst_1 = [1, 4, 3, 5]
lst_2 = [-2, 1, 3]
tuple_intersection = tuple(set(lst_1) & set(lst_2))
tuple_symmetric_difference = tuple(set(lst_1) ^ set(lst_2))


# 5
def happy_number(numeric: int) -> bool:
    """
    function that checks (in this case )if sum digits of
        list [:3] == sum digits list [3:] return True else False
    """
    return True if sum(
        map(int, str(numeric)[:int(len(str(numeric)) / 2)])) == sum(
        map(int, str(numeric)[int(len(str(numeric)) / 2):])) else False


print(happy_number(123321))

text = "jay, jim, roy, axel, billy, charlie, jax, gina, paul, ringo, ally, " \
       "nicky, cam, ari, trudie, cal, carl, lady, lauren, ichabod, arthur," \
       " ashley, drake, kim, julio, lorraine, floyd, janet, lydia, charles, " \
       "pedro, bradley"
# print(str(text).replace('"', '').replace('\'', ''))
first_word = text.split(', ')[0]
print(first_word)
word_count = len(text.split())
print(word_count)
word_to_lst = text.split(', ')
print(text.replace(', ', ''))

# 6
tuple_1 = tuple('hello world')
tuple_2 = tuple('sddsd')
tuple_father = (tuple_1, tuple_2)
print(len(tuple_father[1]))
