

public class sum_labeled {
    public static double sum_labeled_m(int[] a, int i, int j) {
        if (i < 0 || i >= a.length || j < 0 || j >= a.length) {
            return -100000;
        } else {
            return a[i] + a[j] / 2.0;
        }
    }
}