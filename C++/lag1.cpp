#include <iostream>

double lag1(double elements[], double mean, int n){
    double r1;
    double q = 0;
    double v = (elements[0] - mean) * (elements[0] - mean);
    for (int i = 1; i < n; i++) {
        double delta0 = elements[i - 1] - mean;
        double delta1 = elements[i] - mean;
        q += (delta0 * delta1 - q) / (i + 1);
        v += (delta1 * delta1 - v) / (i + 1);
    }
    r1 = q / v;
    return r1;