#include <iostream>

bool check_equal(double a[], double b[], int n1, int n2){
    if (n1 != n2)
    {
        return false;
    }
    for (int i = 0; i < n1; i++)
    {
        if (a[i] != b[i])
        {
            return false;
        }
    }
    return true; 
}
