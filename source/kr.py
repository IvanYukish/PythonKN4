# 1
text = "jay, jim,roy, roy, axel, billy, charlie, jax, gina, paul, ringo, ally, " \
       "nicky, cam, ari, trudie, cal, carl, lady, lauren, ichabod, arthur," \
       "ashley, drake, kim, julio, lorraine, floyd, janet, lydia, charles, " \
       "pedro, bradley"

max_len = len(max(text.replace(',', '').split()))
for i in text:
    if len(i) == max_len:
        print(i)
        break

# 2
numeric = int(input())
print(sum(map(int, str(numeric)[:int(len(str(numeric)))])))

# 3
lst = [3, 3, 5, 6, 7, 8]
print(set(lst))


# 4
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
