#include <iostream>

double chebyshevDistance(double p1[], double p2[], int n1, int n2){
    if (n1 !=  n2)
    {
        cout << "Error!" << endl;
        return 0;
    }

    double maxDiff = abs(p1[0] - p2[0]);
    for (int i = 1; i < n1; i++)
    {
        double diff = p1[i] - p2[i];
        if (maxDiff < diff)
        {
            maxDiff = diff;
        }
    }
    return maxDiff;        
}
