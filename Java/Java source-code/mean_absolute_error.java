

public class mean_absolute_error {
    public static double mean_absolute_error(Integer[] a, Integer[] b) {
        int sum = 0;
        for (int i = 0; i < a.length; i++) {
            sum += Math.abs(a[i] - b[i]);
        }
        return (double) sum / a.length;
    }
}