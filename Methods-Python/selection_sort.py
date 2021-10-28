def selection_sort(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
