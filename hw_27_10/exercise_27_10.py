#1. Відсортувати тварин за віком
animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
]

animals_sorted = sorted(animals, key = lambda i: i['age'])
#print(animals_sorted)

#2. З використанням list comprehension cтворити список квадратів непарних елементів вхідного списку numbers
numbers = [4, 2, 1, 6, 9, 7]

list_square = [i*i for i in numbers if i%2]
#print(list_square)

#3. Реалізувати функцію послідовного пошуку, який шукає потрібний елемент, починаючи з кінця вхідного списку
names = ['Joe', 'Mary', 'Ann', 'Andrew', 'Stephan', 'Rosie']
element_to_find = 'Stephan'

def find_reverse(element, list):
    index = len(list) - 1
    while index > 0:
        if list[index] == element:
            return True
        else:
            index -= 1

# print(find_reverse(element_to_find, names))


'''
4. Реалізувати клас Container, який відповідає наступним умовам:
   - кожен об'єкт цього класу має атрибут elements, який при створенні нового об'єкту класу є пустим списком
   - об'єкт має метод add(), який додає новий елемент до списку
   - тип елементів, що можуть зберігатися у контейнері, визначається за першим доданим елементом: якщо першим 
   було додано int, всі наступні мають бути int. Якщо першим було додано str, всі наступні також str. 
   Модливі типи даних - примітивні типи мови Python (без колекцій та мапінгів)
   Якщо ця умова не виконується - метод add повертає помилку TypeError
   - elements завжди відсортовано за зростанням
'''

class Container:

    def __init__(self):
        self.elements = []

    def add(self, new_element):
        if len(self.elements) == 0:
            self.elements.append(new_element)
        else:
            if type(new_element) == type(self.elements[0]):
                self.elements.append(new_element)
            else:
                raise TypeError("Anothere type element")

    def __str__(self):
        sorted_list = sorted(self.elements)
        return f'{sorted_list}'



container_1 = Container()
container_1.add('aaabb')
container_1.add('aaad')
container_1.add('aaachh')
print(container_1)