#include <iostream>

int binarySearchFromTo(double elements[], double key, int from, int to){
    int low = from;
    int high = to;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        double midVal = elements[mid];

        if (midVal < key)
        {
            low = mid + 1;
        } else{
            if (midVal > key)
            {
                high = mid -1;
            } else
            {
                return mid;
            }          
        }
    }
    return - (low +1);
}
