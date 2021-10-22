#include <iostream>

double* computeDividedDifference1(double x[], double y[], int n) {
    double divdiff[1000];
    static double a[100];
    a[0] = y[0];
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            double denominator = x[j + i] - x[j];
            y[j] = (y[j + 1] - y[j]) / denominator;
        }
        a[i] = y[0];
    }
        return a;
    }
