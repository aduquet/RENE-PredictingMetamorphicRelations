#include <iostream>
#include <math.h>

int* set_min_val(int a[], int k, int n) {
    int i;
    for (i = 0; i < n; i++) {
        if (a[i] < k) {
            a[i] = k;
        }
    }
    return a;
}