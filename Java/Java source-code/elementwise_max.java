

public class elementwise_max {
    public static int[] elementwise_max(Integer[] a, Integer[] b) {
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