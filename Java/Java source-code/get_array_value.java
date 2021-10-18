

public class get_array_value {
    public static int get_array_value(Integer[] a, Integer k) {
        if (k - 1 >= a.length || k - 1 < 0) {
            return -100000;
        } else {
            return a[k - 1];
        }
    }
}