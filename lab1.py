# 1
integer = int(input())
# 2
print(integer)
# 3
integer += 0.8
print(integer)
# 4 якщо потрібно зберегти ціле число то ...
# integer = int(integer)
print(int(integer))

# 5
print(str(integer) * 3)

# 6
st = 'student'
for i in range(100):
    print('zalik zdalo')
    if (i % 10) in range(5, 10) or i % 100 in range(11, 20) or i % 10 == 0:
        print(i, st, "iv")
    elif i % 10 in range(2, 5):
        print(i, st, "y")
    else:
        print(i, st)

# 7
import math

number_a = abs(float(input()))
number_b = abs(float(input()))
x = (math.sqrt(number_a * number_b) / math.e * number_b) + number_a * pow(
    math.e, (2 * number_a / number_b))

print(x)

# 8
number = float(input())
count = int(input())
output = number
for i in range(count):
    output *= number

print(output)

# 9
num = int(input())
for i in range(2, int(math.sqrt(num))):
    if num % i == 0:
        print('number not Prime')
        break

else:
    print('number is prime')

# 10
print(sum([int(i) for i in input()]))

# 11
[print(i, end='') for i in input() if not i.isdigit()]

# 12
word = input()
# method1
print(word[::-1] == word[::])
# method2
print(all(
    [word[i] == word[len(word) - (i + 1)] for i in range(int(len(word) / 2))]))


# 13
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
