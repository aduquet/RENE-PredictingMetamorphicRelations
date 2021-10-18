

public class array_calc1 {
    public static int[] array_calc1(Integer[] a, Integer k) {
        int i;
        int[] b = new int[a.length];
        for (i = 0; i < a.length; i++) {
            b[i] = a[i] / k;
        }
        return b;
    }
}