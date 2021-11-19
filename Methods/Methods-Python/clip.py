def clip(a, loweLim, upperLim):
    r = []
    for i in range(0, len(a)):
        if a[i] < loweLim:
            r[i] = loweLim
        else:
            if a[i] > upperLim:
                r[i] = upperLim
            else:
                r[i] = a[i]

    return r
