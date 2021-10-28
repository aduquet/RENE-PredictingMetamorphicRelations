#include <iostream>

double manhattanDistance(double p1[], double p2[], int n) {
    double result = 0.0;
    for (int i = 0; i < n; i++) {
        result += abs(p2[i] - p1[i]);
    }
    return result;
}
