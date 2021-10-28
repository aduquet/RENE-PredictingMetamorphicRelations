#include <iostream>

double* calculateDifferences(double x[], double y[], int n){

    static double z[100];

    for (int i = 0; i < n; i++)
    {
        z[i] = y[i] - x[i];
    }
    
    return z;
}
