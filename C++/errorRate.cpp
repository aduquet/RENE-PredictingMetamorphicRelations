# include <iostream>


double errorRate(double labels[], double predictions[], int n) {
    double nberrors = 0;
    double datasize = 0;
    for (int index = 0; index < n; index++) {
        if (predictions[index] == -1) {
            continue;
        }
        if (predictions[index] != labels[index]) {
            nberrors++;
        }
        datasize++;
    }
    return nberrors / datasize;
}