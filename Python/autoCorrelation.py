def autoCorrelation(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance

