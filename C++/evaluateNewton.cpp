#include <iostream>

double evaluateNewton(double a[], double c[], double z, int nc) {
    int n = nc - 1;
    double value = a[n];
    for (int i = n - 1; i >= 0; i--) {
        value = a[i] + (z - c[i]) * value;
    }
    return value;
}