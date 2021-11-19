#include <iostream>
#include <math.h>
#include <algorithm>

double*  ebeMultiply(double a[], double b[], int n1, int n2) {
    if (n1 != n2) {
        return 0;
    }
    static double  result[1000];
    for (int i = 0; i < n1; i++) {
        result[i] =  a[i]*b[i];
    }
    return result;
}