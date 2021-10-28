#include <iostream>
#include <math.h>
#include <algorithm>

double distanceInf(double p1[], double p2[], int n) {
    double maxi = 0;
    for (int i = 0; i < n; i++) {
        maxi = max(maxi, abs(p1[i] - p2[i]));
    } 
    return maxi;
}