try:
    array = list(map(float, input("Введите последовательность чисел в любом порядке, через пробел: ").split()))
    if len(array) < 2:
        raise ValueError("Короткая последовательность!")
    if len(set(array)) == 1:
        raise ValueError("Число не попадает в последовательность с соблюдением условий.")
    element = float(input("Введите любое число из заданного диапазона: "))
except ValueError as ve:
    print('Ошибка!!!', ve)
else:
    def bubble_sorting(arr):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def binary_search(arr, elem, left, right):
        if left > right:
            return right
        middle = (right + left) // 2
        if arr[middle] < elem and (middle == len(arr) - 1 or arr[middle + 1] >= elem):
            return middle
        elif elem < arr[middle]:
            return binary_search(arr, elem, left, middle - 1)
        else:
            return binary_search(arr, elem, middle + 1, right)

    array = bubble_sorting(array)
    left = float(array[0])
    right = float(array[-1])
    if element < left or element > right:
        print('Числа нет в диапазоне')
    else:
        index = binary_search(array, element, 0, len(array) - 1)
        if index is False:
            print('Число не найдено в диапазоне')
        else:
            print('Индекс элемента, соответствующего условиям ', index)