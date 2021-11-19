#include <iostream>

int* array_calc1(int a[], int k, int n){
    int i;
    static int b[n];
    for (int i = 0; i < n; i++)
    {
        b[i] = a[i]/k;
    }
    return b; 
}
