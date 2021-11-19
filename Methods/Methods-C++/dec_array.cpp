#include <iostream>

int* dec_array(int a[], int k, int n) {
    for (int i = 0; i < n; i++) {
        a[i] -= k;
    }
    return a;
}