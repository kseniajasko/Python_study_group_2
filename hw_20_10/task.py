def linear_shift(array: list, shift: int) -> list:
    '''
    array = [1, 2, 3, 4] shift = 1 => [0, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [0, 0, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [0, 0, 0, 1]
    '''
    num_list = []

    for num in array:
        numbers = num - shift
        if numbers <= 0:
            num_list.append(0)
        else:
            num_list.append(numbers)
    return num_list



def circular_shift(array: list, shift: int) -> list:
    '''
    array = [1, 2, 3, 4] shift = 1 => [4, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [3, 4, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [2, 3, 4, 1]
    '''

    try:
        for item in range(shift):
            array.insert(0, (array.pop(-1)))
        return array
    except:
        raise ValueError('Empty start list')

print(circular_shift([1, 2, 3, 4], 3))



def nested_parentheses(incoming: str) -> bool:
    '''
    Функція отримує рядок, який складається тільки зі знаків "(" або ")"
    Рядок вважається таким, що містить коректно вкладені скобки, якщо для
    кожної скобки "(" існує відповідна ")".
    Функція повертає булевську змінну, яка показує, чи містить вхідний рядок
    тільки правильно вкладені скобки - True, чи ні - False

    incoming = "((())(())())" => True
    incoming = "" => True
    incoming = "(((())))" => True
    incoming = "())" => False
    incoming = "(()()(())" => False
    '''
    empty_list = []
    balanced = True
    index = 0
    while index < len(incoming) and balanced:
        token = incoming[index]
        if token == "(":
            empty_list.append(token)
        elif token == ")":
            if len(empty_list) == 0:
                balanced = False
            else:
                empty_list.pop()

        index += 1

    return balanced and len(empty_list) == 0

# if __name__ == '__main__':
    # print(linear_shift([1, 2, 3, 4], 5))
    # print(circular_shift([], 3))
    # print(nested_parentheses('((())(())())'))
    # print(nested_parentheses(''))
    # print(nested_parentheses('(((())))'))
    # print(nested_parentheses('())'))
    # print(nested_parentheses('(()()(())'))