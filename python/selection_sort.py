def bubble_sort(lst):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                flag = True

    return lst            
lst = [1, 7, 2, 5, 4, 3]
print(bubble_sort(lst))

