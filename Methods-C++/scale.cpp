#include <iostream>
#include <math.h>

double* scale(double val, double arr[], int n) {
    static double  newArr[1000];

    for (int i = 0; i < n; i++) {
        newArr[i] = arr[i] * val;
    }
    return newArr;
}