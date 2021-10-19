

public class geometric_mean {
    public static double geometric_mean_m(Integer[] a) {
        long product = 1;
        for (int i = 0; i < a.length; i++) {
            product *= a[i];
        }
        return Math.pow(product, (double) 1 / a.length);
    }
}