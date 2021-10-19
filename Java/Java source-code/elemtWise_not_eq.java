

public class elemtWise_not_eq {
    public static boolean[] elemtWise_not_eq_m(Integer[] a, Integer[] b) {
        boolean[] r = new boolean[a.length];
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                r[i] = true;
            } else {
                r[i] = false;
            }
        }
        return r;
    }
}