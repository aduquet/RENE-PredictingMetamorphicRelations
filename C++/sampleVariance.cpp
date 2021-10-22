#include <iostream>
#include <math.h>

double sampleVariance(double elements[], double mean, int n) {
    int size = n;
    double sum = 0;
    for (int i = size; --i >= 0; ) {
        double delta = elements[i] - mean;
        sum += delta * delta;
    }
    return sum / (size - 1);
}