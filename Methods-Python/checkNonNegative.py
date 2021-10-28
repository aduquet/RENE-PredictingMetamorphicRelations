def checkNonNegative(n):

    for i in range(0, len(n)):
        if n[i] < 0:
            return False
    return True
