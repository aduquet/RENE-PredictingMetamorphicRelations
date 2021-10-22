#include <iostream>

double evaluateInternal(double x[], double y[], double z, int n) {
    int nearest = 0;
    double c[1000];
    double d[1000];
    double min_dist = INFINITY;
    for (int i = 0; i < n; i++) {
        c[i] = y[i];
        d[i] = y[i];
        double dist = abs(z - x[i]);
        if (dist < min_dist) {
            nearest = i;
            min_dist = dist;
        }
    }
    double value = y[nearest];
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            double tc = x[j] - z;
            double td = x[i + j] - z;
            double divider = x[j] - x[i + j];
            double w = (c[j + 1] - d[j]) / divider;
            c[j] = tc * w;
            d[j] = td * w;
        }
        if (nearest < 0.5 * (n - i + 1)) {
            value += c[nearest];
        } else {
            nearest--;
            value += d[nearest];
        }
    }
    return value;
}
