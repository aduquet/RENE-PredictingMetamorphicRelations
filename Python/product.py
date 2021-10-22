def product(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, -1, -1):
        product1 *= elements[i]

    return product1
