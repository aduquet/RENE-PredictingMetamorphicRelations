#include <iostream>

int* reverse(int a[], int n) {
    static int r[1000];
    int cnt = 0;
    for (int i = n - 1; i >= 0; i--) {
        r[cnt] = a[i];
        cnt++;
    }
    return r;
}