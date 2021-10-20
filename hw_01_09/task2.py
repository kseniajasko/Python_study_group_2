from collections import Counter

def probability(m: int, n: int)->float:
    return m / n

experiments = [2, 11, 3, 5, 3, None, 1, 9, 9, 8, 12, 7, 4, None, 6, 2, 1, 3, 8, 3, 12, 4, 6, None, 11, 2, 5, 7, 3, 9]

exp_2 = [i for i in experiments if isinstance(i, int)]

max_elem = max(exp_2)

if max_elem in range(0, 7, 1):
    list_all_event = [x for x in range(1, 7, 1)]
    print(f'6-face cube')
elif max_elem in range(7, 13, 1):
    list_all_event = [x for x in range(1, 13, 1)]
    print(f'12-face cube')
else:
    list_all_event = [x for x in range(1, 21, 1)]
    print('20-face cube')

b = Counter(exp_2)


for i in list_all_event:
    print(f'Probability face {i} of cube is equal {probability(b[i], len(exp_2))}')

# sum_probability = 0
# for i in list_all_event:
#     sum_probability += probability(b[i], len(exp_2))
#
# print(sum_probability)