

public class find_median {
    public static double find_median_m(Integer[] a) {
        int k = a.length / 2 + 1;
        int minIndex = 0;
        int minValue = a[0];
        for (int i = 0; i < k; i++) {
            minIndex = i;
            minValue = a[i];
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < minValue) {
                    minIndex = j;
                    minValue = a[j];
                }
            }
            int temp = a[i];
            a[i] = a[minIndex];
            a[minIndex] = temp;
        }
        if (a.length % 2 == 0) {
            return (double) (a[a.length / 2 - 1] + a[a.length / 2]) / 2;
        } else {
            return a[a.length / 2];
        }
    }
}