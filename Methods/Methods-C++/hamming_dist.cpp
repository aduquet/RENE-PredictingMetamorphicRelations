#include <iostream>
#include <math.h>
#include <algorithm>

int hamming_dist(int a[], int b[], int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] != b[i]) {
            cnt++;
        }
    }
    return cnt;
}