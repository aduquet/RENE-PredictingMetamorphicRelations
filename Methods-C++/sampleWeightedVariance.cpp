#include <iostream>
#include <math.h>

double sampleWeightedVariance(double data[], double weights[], int n) {
    double sumOfWeights = 0;
    double sumOfProducts = 0;
    double sumOfSquaredProducts = 0;
    for (int i = 0; i < n; i++) {
        sumOfWeights += weights[i];
        sumOfProducts += data[i] * weights[i];
        sumOfSquaredProducts += data[i] * data[i] * weights[i];
    }
    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1);
}
