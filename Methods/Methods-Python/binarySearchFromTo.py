def binarySearchFromTo(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)/2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)

