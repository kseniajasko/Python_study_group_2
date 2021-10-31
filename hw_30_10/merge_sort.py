def insertion_sort(array):
    for i in range(1, len(array)):
        element = array[i]
        j = i-1
        while j >= 0 and element < array[j] :
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = element

recursion_depth = 3
def merge_sort(array):
    global recursion_depth
    if recursion_depth == 0:
        insertion_sort(array)
    else:
        recursion_depth -= 1
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    array[k] = left_half[i]
                    i = i + 1
                else:
                    array[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                array[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                array[k] = right_half[j]
                j = j + 1
                k = k + 1


array_1 =  [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
merge_sort(array_1)
print(array_1)