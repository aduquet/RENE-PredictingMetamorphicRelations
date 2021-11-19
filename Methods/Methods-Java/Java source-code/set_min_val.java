

public class set_min_val {
    public static Integer[] set_min_val_m(Integer[] a, Integer k) {
        int i;
        for (i = 0; i < a.length; i++) {
            if (a[i] < k) {
                a[i] = k;
            }
        }
        return a;
    }
}