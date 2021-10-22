#include <iostream>
#include <math.h>

double sumOfLogarithms(double elements[], int n) {
    double logsum = 0;
    for(int i = 0; i < n; i++) {
        logsum += log(elements[i]);
    }
    return logsum;
}
