#include <iostream>

int count_k(int a[], int k, int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == k) {
            cnt++;
        }
    }
    return cnt;
}
