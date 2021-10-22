#include <iostream>

double* power(double data[], int k, int n) {
    for (int i = 0; i < n; i++) {
        data[i] = pow(data[i], k);
    }
    return data;
}
