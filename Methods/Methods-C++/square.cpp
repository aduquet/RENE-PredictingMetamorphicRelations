#include <iostream>
#include <math.h>

double* square(double data[], int n) {
    for (int i = 0; i < n; i++) {
        data[i] = data[i] * data[i];
    }
    return data;
}
