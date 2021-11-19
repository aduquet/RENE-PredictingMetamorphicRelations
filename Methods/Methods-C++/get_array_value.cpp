#include <iostream>
#include <math.h>
#include <algorithm>

int get_array_value(int a[], int k, int n) {
    if(k - 1 >= n || k - 1 < 0) {
        return -100000;
    } else {
        return a[k - 1];
    }
}