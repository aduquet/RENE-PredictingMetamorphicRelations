#include <iostream>
#include <math.h>

double sampleSkew(int size, double moment3, double sampleVariance) {
    int n = size;
    double s = sqrt(sampleVariance);
    double m3 = moment3 * n;

    return n * m3 / ((n - 1) * (n - 2) * s * s * s);
}
