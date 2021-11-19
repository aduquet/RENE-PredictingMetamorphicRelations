#include <iostream>

double evaluateWeightedProduct( double values[],  double weights[],  int begin, int lengths, int n) {
    double product = 1.0;
     
    for (int i = begin; i < begin + lengths; i++) {
        product *= pow(values[i], weights[i]);
    }
    return product;
}