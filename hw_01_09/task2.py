from collections import Counter

def probability(m: int, n: int)->float:
    return m / n

experiments = [2, 11, 3, 5, 3, None, 1, 9, 9, 8, 12, 7, 4, None, 6, 2, 1, 3, 8, 3, 12, 4, 6, None, 11, 2, 5, 7, 3, 9]

exp_2 = [i for i in experiments if isinstance(i, int)]

max_elem = max(exp_2)

if max_elem in range(0, 7, 1):
    print('6-, 12-, 20-face cube')
elif max_elem in range(7, 13, 1):
    print('12- or 20-face cube')
else:
    print('20-face cube')

b = Counter(exp_2)

exp_3 = []

for i in exp_2:
    if i not in exp_3:
        exp_3.append(i)

exp_3.sort()
print(exp_2)
print(exp_3)
for i in exp_3:
    print(f'Probability face {i} of cube is equal {probability(b[i], len(exp_2))}')



