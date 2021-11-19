def errorRate(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
