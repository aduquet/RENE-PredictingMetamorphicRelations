#include <iostream>
#include <math.h>

int* shell_sort(int a[], int n) {
    int j;
    int i;
    int k;
    int m;
    int mid;
        
    for (m = n/2; m > 0; m /= 2) {
        for (j = m; j < n; j++) {
            for (i = j - m; i >= 0; i -= m) {
                if (a[i + m] >= a[i]) {
                    break;
                } else {
                    mid = a[i];
                    a[i] = a[i + m];
                    a[i + m] = mid;
                }
            }
        }
    }
    return a;
}