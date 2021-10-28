#include <iostream>

double meanDeviation(double elements[], double mean, int n) {
    int size = n;
    double sum = 0;
    for (int i = size; --i >= 0; ) {
        sum += abs(elements[i] - mean);
    }
    return sum / size;
}