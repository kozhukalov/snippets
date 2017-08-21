def insertion_sort(array):
    for i in range(1, len(array)):
        for j in reversed(range(i)):
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
            else:
                break
    return array

array = [7, 2, 1, 3, 4, 6, 5]
print(insertion_sort(array))

