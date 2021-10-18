
'''
Клас SignedInt є моделлю для опису позитивних і від'ємних цілих чисел.
Кожен об'єкт класу описує одне ціле число за такою схемою:
- атрибут modulus містить int, який представляє абсолютне значення (модуль) числа
- атрибут sign містить рядок '-' або '+', який представляє знак числа.
Тож число -3 може бути описане об'єктом SignedInt(3, '-'),
а число 5 буде описане об'єктом SignedInt(5, '+')
Класс Matrix представляє собою список об'єктів SignedInt. Розмір списку задається
при створенні об'єкта класу Matrix, об'єкти SignedInt, які входять у цей список,
генеруються автоматично і додаються до атрибуту elements об'єкту Matrix.
Завдання:
+ реалізувати обмеження на встановлення атрибуту sign. Можливі значення - рядок '-' або '+', інакше - ValueError
+ реалізувати обмеження на встановлення атрибуту modulus. Можливі значення - цілі числа, інакше - ValueError
+ реалізувати людино-читаємий вивід у звичному форматі представлення чисел зі знаком,
    так щоб str(SignedInt(7, '-')) повертало рядок '-7', а str(SignedInt(4, '+')) повертало рядок '4'
+ реалізувати методи потрівняння об'єктів класу SignedInt за звичайною логікою, тобто
    SignedInt(5, '-') < SignedInt(1, '+')
    SignedInt(3, '+') > SignedInt(10, '-')
    SignedInt(2, '+') == SignedInt(2, '+')
    SignedInt(3, '+') <= SignedInt(5, '+')
    SignedInt(7, '-') >= SignedInt(8, '-')

- релізувати протокол ітератора для об'єкту класу Matrix, який дозволить ітерувати його атрибут elements.
Кожен реалізований метод має мати щонайменше один тест. Якщо у методі є розгалуження -
мають бути протестовані усі гілки.
'''

class SignedInt:

    def __init__(self, modulus, sign):
        self.modulus = modulus
        self.sign = sign

    @property
    def sign(self):
        return self._sign

    @sign.setter
    def sign(self, sign):
        if sign != '+' and sign != '-':
            raise ValueError('Error sign')
        else:
            self._sign = sign

    @property
    def modulus(self):
        return self._modulus

    @modulus.setter
    def modulus(self, modulus):
        if type(modulus) != int:
            raise ValueError('Error modulus type')
        else:
            self._modulus = modulus

    def __str__(self):
        if self._sign == '+':
            return f'{self._modulus}'
        else:
            return f'-{self._modulus}'

    def number(self):
        if self.sign == '-':
            return -int(self._modulus)
        else:
            return self._modulus

    def __gt__(self, other):
        return self.number() > other.number()

    def __lt__(self, other):
        return self.number() < other.number()

    def __ge__(self, other):
        return self.number() >= other.number()

    def __le__(self, other):
        return self.number() <= other.number()

    def __eq__(self, other):
        return self.number() == other.number()




class Matrix:
    elements = []
    current = 0

    def __init__(self, size):
        for index in range(size):
            modulus = pow(index, index)
            if index % 2:
                sign = '-'
            else:
                sign = '+'
            self.elements.append(SignedInt(modulus, sign))

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > len(self.elements) - 1:
            raise StopIteration
        else:
            self.current += 1
            return self.elements[self.current - 1]

if __name__ == '__main__':
    a = SignedInt(5, '+')
    b = SignedInt(5, '+')
    m = Matrix(3)

    for element in m:
        print(element)

# print(a > b)
# print(a < b)
# print(a <= b)
# print(a >= b)
# print(a == b)