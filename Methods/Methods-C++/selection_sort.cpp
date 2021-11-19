#include <iostream>
#include <math.h>

int* selection_sort(int list[], int n) {
    int i;
    int j;
    int min;
    for (i = 0; i < n - 1; i++) {
        min = i;
        for (j = i + 1; j < n; j++) {
            if (list[j] < list[min]) {
                min = j;
            }
        }
        int tmp = list[i];
        list[i] = list[min];
        list[min] = tmp;
    }
    return list;
}