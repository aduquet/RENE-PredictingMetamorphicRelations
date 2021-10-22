#include <iostream>

double weightedRMS(double data[], double weights[], int n) {
    double sumOfProducts = 0;
    double sumOfSquaredProducts = 0;
    for(int i = 0; i < n; i++) {
        sumOfProducts += data[i] * weights[i];
        sumOfSquaredProducts = data[i] * data[i] * weights[i];
    }
    return sumOfProducts / sumOfSquaredProducts;
}