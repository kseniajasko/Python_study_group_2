# 1. Якщо ми запишемо всі натуральні числа, що кратні 3 або 5, та менші 10, ми отримаємо 3, 5, 6 та 9. Сума цих чисел буде дорівнювати 23. Знайти суму всіх чисел, що кратні 3 або 5, та менші 1000.

n = 1000
suma = 0
while n > 0:
    if n % 5 == 0 or n % 3 == 0:
        suma += n
    n -= 1

# print(suma)

# 2. Для числа 13195 існують такі прості дільники (прості числа, на яке задане число ділиться без залишку):
# 5, 7, 13, 29. Знайти найбільший простий дільник числа 600851475143.

def Largest_Prime_Factor(n):
    prime_factor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n

    return int(prime_factor)

# print(Largest_Prime_Factor(10))



# 3. 2520 найменше число, що ділиться на будь-яке число від 1 до 10 без залишку. Яке найменше позитивне число ділиться без залишку на всі числа від 1 до 20?
import functools
import math

#print(functools.reduce(lambda x,y: x*y//math.gcd(x, y), range(1, 21)))


# 4. Триплет Піфагора - це набір з трьох натуральних чисел a < b < c, для якого a**2 + b**2 = c**2. Наприклад,  3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# Існує тільки один триплет Піфагора, для якого a + b + c = 1000. Знайти добуток a*b*c лдя цього триплету.
from math import sqrt

d = []
for z in range(1, 1001):
    z2 = z**2
    for x in range(1, z//2 + 1):
        x2 = x**2
        y = round(sqrt(z2 - x2))
        if x2 + y**2 == z2 and x + y + z == 1000:
            d.append((x, y, z))
# print(d)


# 5. Сумою простих чисел менших 10 є 2 + 3 + 5 + 7 = 17. Знайти суму всіх простих чисел, менших за 2 мільйони.

from math import sqrt
from itertools import count, islice

def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

def sum_prime(x):
    sum = 0
    for n in range(1, x+1):
        if is_prime(n):
            sum += n
    return sum

# print(sum_prime(10))
# print(sum_prime(2000000))


