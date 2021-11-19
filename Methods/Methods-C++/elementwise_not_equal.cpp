#include <iostream>
#include <math.h>
#include <algorithm>

bool* elementwise_not_equal(int a[], int b[], int n){
    static bool r[1000];
    for (int i = 0; i < n; i++) {
        if (a[i] != b[i]) {
            r[i] = true;
        } else {
            r[i] = false;
        }
    }
    return r;
}