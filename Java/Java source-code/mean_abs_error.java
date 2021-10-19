

public class mean_abs_error {
    public static double mean_abs_error_m(Integer[] a, Integer[] b) {
        int sum = 0;
        for (int i = 0; i < a.length; i++) {
            sum += Math.abs(a[i] - b[i]);
        }
        return (double) sum / a.length;
    }
}