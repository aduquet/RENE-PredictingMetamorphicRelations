#include <iostream>

bool equals(double x[], double y[], int nx, int ny) {

    if (nx != ny) {
        return false;
    }
    for (int i = 0; i < nx; ++i) {
        if (abs(y[i] - x[i]) > 0.0001) {
            return false;
        }
    }
    return true;
}