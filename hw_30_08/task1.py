#За допомогою циклу вивести зашифроване шифром Цезаря своє ім’я в один рядок.
# Зміщення дорівнює довжині імені

name = str(input("Your name: ")).upper()
key = len(name)
result = ''

for character in name:
    x = ord(character)
    result += chr(x + key)

print(result)

# alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in name:
#     index_name = alphabet.find(i)
#     new_index_name = index_name + key
#     if i in alphabet:
#         result += alphabet[new_index_name]
#     else:
#         result += i

