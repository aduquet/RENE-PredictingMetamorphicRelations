#include <iostream>

double winsorizedMean(double sortedElements[], int left, int right, int n) {

    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += sortedElements[i];
    }
    double mean = sum / n;
    double leftElement = sortedElements[left];
    for (int i = 0; i < left; ++i) {
        mean += (leftElement - sortedElements[i]) / n;
    }
    double rightElement = sortedElements[n - 1 - right];
    for (int i = 0; i < right; ++i) {
        mean += (rightElement - sortedElements[n - 1 - i]) / n;
    }
    return mean;
}