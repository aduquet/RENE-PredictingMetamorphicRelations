

public class elemtWise_max {
    public static int[] elemtWise_max_m(Integer[] a, Integer[] b) {
        int[] r = new int[a.length];
        for (int i = 0; i < a.length; i++) {
            if (a[i] > b[i]) {
                r[i] = a[i];
            } else {
                r[i] = b[i];
            }
        }
        return r;
    }
}