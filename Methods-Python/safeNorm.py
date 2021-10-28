import math


def safeNorm(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm
