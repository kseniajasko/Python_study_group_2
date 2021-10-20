# Факторіал числа n - добуток всіх цілих позитивних чисел, які менши або дорівнюють n.
# Наприклад, 3! = 1*2*3 = 6. Знайти факторіал числа, яке дорівнює довжині прізвища студента.
# Результат вивести у вигляді рядка “5! = 120”.

s_name = 'Oksana'

n = len(s_name)

factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print(f'{len(s_name)}! = {factorial}')

# def factorial(n: int)-> int:
#     if n == 0:
#         return 1
#     return n*factorial(n-1)
#
# print(f'{n}! = {factorial(n)}')

