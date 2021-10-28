def durbinWatson(elements):
    run = 0

    for i in range(1, len(elements)):
        x = elements[i] - elements[i - 1]

        run += x * x

    return run
