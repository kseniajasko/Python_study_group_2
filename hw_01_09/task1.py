zoo = [
    ['monkey', 'tiger', 'elephant'],
    ['frog', 'snake'], ['owl', 'pigeon'],
    ['hamster', 'mouse', 'hedgehog']
]
#У цьому перепису зоопарку знайти та вивести назви тварин, у яких є літера ‘a’.

letter = 'a'
d = []

for c in zoo:
    for elem in c:
        if letter in elem:
            d.append(elem)

print(d)