

public class elementwise_min {
    public static int[] elementwise_min(Integer[] a, Integer[] b) {
        int[] r = new int[a.length];
        for (int i = 0; i < a.length; i++) {
            if (a[i] < b[i]) {
                r[i] = a[i];
            } else {
                r[i] = b[i];
            }
        }
        return r;
    }
}