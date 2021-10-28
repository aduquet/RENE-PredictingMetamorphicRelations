#include <iostream>

double covariance(double elements1[], double elements2[], int n) {

    double sumx = elements1[0];
    double sumy = elements2[0];
    double Sxy = 0;
    
    for (int i = 1; i < n; ++i) {
        double x = elements1[i];
        double y = elements2[i];
        sumx += x;
        Sxy += (x - sumx / (i + 1)) * (y - sumy / i);
        sumy += y;
    }
    return Sxy / (n - 1);
}
