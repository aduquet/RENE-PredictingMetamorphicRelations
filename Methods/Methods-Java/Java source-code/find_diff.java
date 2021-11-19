

public class find_diff {
    public static int[] find_diff_m(Integer[] a, Integer[] b) {
        int i;
        int[] c = new int[a.length];
        for (i = 0; i < a.length; i++) {
            c[i] = a[i] - b[i];
        }
        return c;
    }
}