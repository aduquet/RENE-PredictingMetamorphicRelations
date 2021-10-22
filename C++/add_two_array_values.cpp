#include <iostream>

double add_two_array_values(int a[], int i, int j, int n)
{
    if (i < 0 || i >= n || j < 0 || j >= n)
    {
        return -100000;
    }
    else {
        return (a[i] + a[j]) / 2;
    }
    
}
