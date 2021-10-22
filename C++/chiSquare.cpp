#include <iostream>

double chiSquate(double expected[], double observed[], int n){
    double sumExpected = 0;
    double sumObserved = 0;
    for (int i = 0; i < n; i++) {
        sumExpected += expected[i];
        sumObserved += observed[i];
        }
    double ratio = 1.0;
    bool rescale = false;
    if (abs(sumExpected - sumObserved) > 10E-6) {
        ratio = sumObserved / sumExpected;
        rescale = true;
    }
    double sumSq = 0.0;
    for (int i = 0; i < n; i++) {
        if (rescale) {
            double dev = observed[i] - ratio * expected[i];
            sumSq += dev * dev / (ratio * expected[i]);
        } else {
            double dev = observed[i] - expected[i];
            sumSq += dev * dev / expected[i];
            }
        }
        return sumSq;
    }