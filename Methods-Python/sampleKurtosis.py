def sampleKurtosis(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
