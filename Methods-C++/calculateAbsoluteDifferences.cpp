#include <iostream>

double* calculateAbsoluteDifferences(double z[], int n){

    if (n == 0)
    {
        return NULL;
    }
    
    static double zAbs[100];
    for (int i = 0; i < n; i++)
    {
        zAbs[i] = abs(z[i]);
    }
    return zAbs;
}
