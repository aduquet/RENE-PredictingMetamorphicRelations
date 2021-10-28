def tanimotoDistance(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
