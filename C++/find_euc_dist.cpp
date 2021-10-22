#include <iostream>

double find_euc_dist(int a[], int b[], int na) {
    double sum = 0;
    for (int i = 0; i < na; i++) {
        sum += (a[i] - b[i]) * (a[i] - b[i]);
    }
    double result = sqrt(sum);
    return result;
}