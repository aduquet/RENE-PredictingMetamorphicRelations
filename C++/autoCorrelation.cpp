#include <iostream>

double autoCorrelation(double data[], int lag, double mean, double variance, int n){
    double run = 0;
    for (int i = lag; i < n; i++)
    {
        run += (data[i] - mean) * (data[i - lag] - mean);
    }
    
    return run / (n - lag) / variance;
}