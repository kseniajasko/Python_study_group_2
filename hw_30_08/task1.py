#За допомогою циклу вивести зашифроване шифром Цезаря своє ім’я в один рядок.
# Зміщення дорівнює довжині імені

alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

name = str(input("Your name: ")).upper()
key = len(name)
result = ''

for i in name:
    index_name = alphabet.find(i)
    new_index_name = index_name + key
    if i in alphabet:
        result += alphabet[new_index_name]
    else:
        result += i

print(result)