#include <iostream>

int find_max2(int a[], int n) {
    int max = a[0] + a[1];
    for (int i = 0; i < n - 1; i++) {
        if (a[i] + a[i + 1] > max) {
            max = a[i] + a[i + 1];
        }
    }
    return max;
}
