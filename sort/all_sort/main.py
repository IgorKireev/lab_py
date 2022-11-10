from typing import List

def pyin():
    while True:
        try:
            print("Введите массив чисел для сортировки:", end = ' ')
            array = [int(i) for i in input().split()]
            break
        except ValueError:
            print("Массив некорректен")
    return array

def menu():
    while True:
        try:
            value = int(input("1. Пузырьковая сортировка\n"
                     "2. Сортировка вставками\n"
                     "3. Сортировка слиянием\n"
                     "4. Сортировка выбором\n"
                     "5. Быстрая сортировка\n"))
            break
        except ValueError:
            print('значение некорректно')
    match value:
        case 1:
            return bubble_sort
        case 2:
            return insertion_sort
        case 3:
            return merge_sort
        case 4:
            return selection_sort
        case 5:
            return quick_sort
        case _:
            menu()

def bubble_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j+1] = buff
    return array

def insertion_sort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def merge_sort(array: List[int]) -> List[int]:
    def merge(array1, array2):
        array = []
        len_array1 = len(array1)
        len_array2 = len(array2)
        index1, index2 = 0, 0
        while index1 < len_array1 and index2 < len_array2:
            if array1[index1] <= array2[index2]:
                array.append(array1[index1])
                index1 += 1
            else:
                array.append(array2[index2])
                index2 += 1
        while index1 < len_array1:
            array.append(array1[index1])
            index1 += 1
        while index2 < len_array2:
            array.append(array2[index2])
            index2 += 1
        return array
    mid = len(array) // 2
    array1 = array[:mid]
    array2 = array[mid:]
    if len(array1) > 1:
        array1 = merge_sort(array1)
    if len(array2) > 1:
        array2 = merge_sort(array2)
    return merge(array1, array2)

def selection_sort(array: List[int]) -> List[int]:
    def find_big(array: List[int]) -> int:
        smallest = array[0]
        smallest_index = 0
        for i in range(1, len(array)):
            if array[i] < smallest:
                smallest = array[i]
                smallest_index = i
        return smallest_index
    newArray = []
    for i in range(len(array)):
        newArray.append(array.pop(find_big(array)))
    return newArray

def quick_sort(array: List[int]) -> List[int]:
    if len(array) < 2:
        return array
    else:
        value = array[0]
        less = [i for i in array[1:] if i < value]
        greater = [i for i in array[1:] if i > value]
        ravn = [i for i in array[1:] if i == value]
        return quick_sort(less) + [value] + ravn + quick_sort(greater)

def main():
    array = pyin()
    sort = menu()
    with open("file.txt", 'w') as file:
        sort = sort(array)
        for i in sort:
            file.write(f'{i}.') if i == sort[-1] else file.write(f'{i}, ')

if __name__ == '__main__':
    main()