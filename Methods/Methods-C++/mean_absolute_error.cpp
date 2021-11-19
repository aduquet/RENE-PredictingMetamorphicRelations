#include <iostream>

double mean_absolute_error(int a[], int b[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += abs(a[i] - b[i]);
    }
    return (double) sum / n;
}
