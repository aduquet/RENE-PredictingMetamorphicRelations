#include <iostream>
#include <math.h>
#include <algorithm>

double distance1(double p1[], double p2[], int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += abs(p1[i] - p2[i]);
    }
    return sum;
}