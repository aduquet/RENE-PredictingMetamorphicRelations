#include <iostream>
#include <math.h>

double varianceDifference(double sample1[], double sample2[], int n) {
    double sum1 = 0;
    double sum2 = 0;
    double diff = 0;
    double sumDifference = 0;

    for (int i = 0; i < n; i++) {
        sumDifference += sample1[i] - sample2[i];
    }
    
    double meanDifference = sumDifference / n;
    for (int i = 0; i < n; i++) {
        diff = sample1[i] - sample2[i];
        sum1 += (diff - meanDifference) * (diff - meanDifference);
        sum2 += diff - meanDifference;
    }
    return (sum1 - sum2 * sum2 / n) / (n - 1);
}