#include <iostream>

bool check_equal_tolerance(double a[], double b[], double tol, int n1, int n2){
    if (n1 != n2)
    {
        return false;
    }
    for (int i = 0; i < n1; i++)
    {
        if (abs(a[i] - b[i]) >= tol)
        {
            return false;
        }
    }
    return true; 
}
