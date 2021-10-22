#include <iostream>

double polevl(double x, double coef[], int N){    
    double ans1;
    ans1 = coef[0];
    
    for (int i = 1; i <= N; i++) {
        ans1 = ans1 * x + coef[i];
    }
    return ans1;
}