#include <iostream>
#include <math.h>

int sequential_search(int a[], int key, int n) {
    int i;
    for (i = 0; i < n; i++) {
        if (a[i] == key) {
            return i;
        }
    }
    return -1;
}