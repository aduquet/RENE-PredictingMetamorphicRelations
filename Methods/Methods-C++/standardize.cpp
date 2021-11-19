#include <iostream>
#include <math.h>

double* standardize(double data[], int n) {
    double sum = 0;
    double sumSq = 0;
    for (int i = 0; i < n; i++) {
        sum += data[i];
        sumSq += data[i] * data[i];
    }
    double mean = sum / n;
    double sd = Math.sqrt((sumSq - mean * sum) / n);
    for (int i = 0; i < n; i++) {
        data[i] = (data[i] - mean) / sd;
    }
    return data;
}
