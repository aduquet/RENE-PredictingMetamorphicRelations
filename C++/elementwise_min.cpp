#include <iostream>
#include <math.h>
#include <algorithm>

int* elementwise_min(int a[], int b[], int n) {
    static int r[1000];
    for (int i = 0; i < n; i++) {
        if (a[i] < b[i]) {
            r[i] = a[i];
        } else {
            r[i] = b[i];
        }
    }
    return r;
}