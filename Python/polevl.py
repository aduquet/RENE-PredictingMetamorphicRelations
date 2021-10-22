def polevl(x, coef, N):
    ans = coef[0]

    for i in range(0, N):
        ans = ans * x + coef[i]

    return ans
