from lab3_and_lab4 import text

import random
import math

a = [0] * 5
a_1 = [1] * 10
b = [i for i in range(1, 15)]
b_1 = [i * i for i in range(10)]
c = [i for i in range(1, 14, 2)]
dict_1 = {i: pow(i, 2) for i in b[:5]}
dict_2 = {i: i % 10 for i in [45, 67, 24, 45]}
dict_3 = {i: len(i) for i in ['ddf', 'dsfs', 'dsdfdsf', 'dsfsdf']}
lst_without_0 = [i for i in [5, 0, 4, 8] if not i]
doubling = [i * 2 for i in 'fefdsfdsfsa']
triplication = [i * 3 for i in 'dfswwfewfwf' if i != 's']
''.join(triplication)
st = [k for k, v in {'a': 10, 'b': 60, 'c': 22, 'd': 77}.items() if v >= 50]
only_digits = [i for i in 'dsfs43erg54gb45' if i.isdigit()]
word_len = [len(i) for i in text.split(' ')]
rand_numbers = [random.randrange(0, 9) for i in range(10)]
zeros_matrix = [[0] * 5 for i in range(4)]
matrix = [[i * j for i in range(5)] for j in range(5)]
matrix_2 = [i for i in range(5) for j in range(5)]
matrix_3 = [[i for i in range(5)] for j in range(5)]
matrix_4 = [[i + int(j / 1.5) for i in range(5)] for j in range(5)]  # 19 +-
dict_revers = {v: k for k, v in {'a': 1, 'b': 2, 'c': 3, 'd': 3}.items()}


def func(first, second, third=2):
    return first + second + third


print(f'function return - {func(1, 2)}')
print(f'function return - {func(1, 2, 3)}')
print(f'function return - {func(first=1, second=2)}')
# print(f'function return - {func(a = 1, c =6)}') error miss b
def_a = lambda n: abs(n)
l_2 = lambda k: k ** 2
l_3 = lambda number: False if number % 2 else True


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, b):
        return self.y == b.x and self.y == b.y

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)


class Vector:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return '({p1}, {p2})'.format(p1=self.p1, p2=self.p2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(
                (self.p1.x + other.p2.x),
                (self.p1.y + other.p2.y),
            )
        else:
            raise Exception("Not type")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(
                (self.p1.x - other.p2.x),
                (self.p1.y - other.p2.y),
            )
        else:
            raise Exception("Not type")

    def __len__(self):
        return self.mag()

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                self.p1.x * other,
                self.p1.y * other
            )
        elif isinstance(other, Vector):
            return Vector(
                self.p1.x * other.p2.x,
                self.p1.y * other.p2.y)

    def mag(self):
        return int((self.p1.x ** 2 + self.p1.y ** 2) ** 0.5)


if __name__ == '__main__':
    myPoint1 = Point(1, 4)
    myPoint2 = Point(300, 3)

    myPoint3 = Point(10, 45)
    myPoint4 = Point(30, 8)

    print(myPoint1, myPoint2)
    print(myPoint1 == myPoint2)

    Vector1 = Vector(myPoint1, myPoint2)
    Vector2 = Vector(myPoint3, myPoint4)

    Vector1.__str__()
    print(Vector2)

    print(Vector1 + Vector2)
    print(Vector2 - Vector2)

    print(Vector1 * Vector2)
    print(Vector2 * 4)

    print(len(Vector1))
    print(len(Vector2))


class Student:
    def __init__(self, name, surname, progres):
        self.__name = name
        self.__surname = surname
        self.__progress = progres

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name=''):
        if name.isalpha():
            self.__name = name
        else:
            print("Недопустимий формат імені")

    @property
    def surname(self):
        return self.__name

    @surname.setter
    def surname(self, surname=''):
        if surname.isalpha():
            self.__name = surname
        else:
            print("Недопустимий формат прізвища")

    def __repr__(self):

        return '({p1}, {p2}, {progress})'.format(p1=self.__name,
                                                 p2=self.__surname,
                                                 progress=self.__progress)

    def __str__(self):
        return self.__repr__()

    def gpa_semester(self, number_semester):
        if number_semester not in self.__progress:
            return "error"
        else:
            for i in self.__progress:
                if i == number_semester:
                    return sum(self.__progress[i]) / len(self.__progress[i])

    def gpa_for_all_years(self):
        sum_all_years = 0
        for i in self.__progress:
            sum_all_years += sum(self.__progress[i]) / len(self.__progress[i])
        return sum_all_years / len(self.__progress)

    def gpa_max(self):
        return max([sum(self.__progress[i]) / len(self.__progress[i]) for i in
                    self.__progress])

    def gpa_min(self):
        return min([sum(self.__progress[i]) / len(self.__progress[i]) for i in
                    self.__progress])


progress = {"Semester" + str(i): [random.randint(50, 100) for j in range(10)]
            for i in range(5)}
studentA = Student('Ivan', 'Popuk', progress)
print(studentA)
print(studentA.gpa_semester('Semester1'))
print(studentA.gpa_for_all_years())
print(studentA.gpa_max())
print(studentA.gpa_min())


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def give_raise(self, persent: int) -> None:
        self.pay += persent * self.pay

    def __str__(self):
        return f'[{self.name}] {self.job} - {self.pay}'


class Manager(Person):
    def __init__(self, name: str, pay: int):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, persent, bonus=100):
        Person.give_raise(self, persent + bonus)


class Triangle:
    def __init__(self, st_a, st_b, st_c):
        self.a = st_a
        self.b = st_b
        self.c = st_c

    def __repr__(self):
        return '({p1}, {p2}, {p3})'.format(p1=self.a, p2=self.b, p3=self.c)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def area(self):
        p = self.a + self.b + self.c
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s

    def is_direct(self):
        return (self.a ** 2 == self.b ** 2 + self.c ** 2) or \
               (self.b ** 2 == self.a ** 2 + self.c ** 2) or \
               (self.c ** 2 == self.b ** 2 + self.a ** 2)

    def is_isotonic(self):
        return (self.a == self.b) or (self.b == self.c) or (self.a == self.c)


tr1 = Triangle(2, 3, 4)
tr2 = Triangle(4, 4, 5)
print(tr1 == tr2)
print(tr1.area())
print(tr1.is_direct())
print(tr1.is_isotonic())
print(tr2.is_isotonic())
print(tr1)
