from random import randrange

# 1
lst = list()
lst.extend([input() for i in range(int(input()))])
print(lst)
print(len(lst))
print(lst.pop(0))

# 2
number = int(input())
lst_comph = [i ** 2 for i in range(number)]
print(lst_comph)

# 3


n = int(input())
rand_list = [randrange(1, 10) for i in range(n)]
lst_comph.extend(rand_list)

# 4
word_to_list = [i for i in input()]

# block 2
# 1
try:
    1 / int(input())

except ZeroDivisionError:
    print('Division on 0')

finally:
    print('calculation finish')

# 2
dict_elem = {1: 'create list', 2: 'add element', 3: 'preview', 4: 'exit'}
for k, v in dict_elem.items():
    print(f'{k}:{v}')

# block 3
while True:
    try:
        p = int(input())
        if p == 1:
            lst = []
            print('Done')

        elif p == 2:
            print('Element - ', end='')
            num = int(input())
            lst.append(num)

        elif p == 3:
            print(lst)

        elif p == 4:
            break

        elif p == 5:
            generate_lst = [i for i in range(p)]

        elif p == 6:

            try:
                item_lst = int(
                    input('input number for destroy item of list - '))
                lst.pop(item_lst)

            except IndexError:
                print('out of range')

        else:
            print('out of range')

    except ValueError:
        'Please input number, not string'

    except NameError:
        'input number 1 for creating list'
