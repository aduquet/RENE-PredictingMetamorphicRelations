#include <iostream>

int*  find_diff(int a[], int b[], int na) {
    static int c[1000];
    for (int i = 0; i < na; i++) {
        c[i] = a[i] - b[i];
    }
    return c;
}
