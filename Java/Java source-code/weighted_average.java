

public class weighted_average {
    public static double weighted_average_m(Double[] a, Double[] b) {
        double sum1 = 0;
        double sum2 = 0;
        for (int i = 0; i < a.length; i++) {
            sum1 += a[i] * b[i];
            sum2 += b[i];
        }
        return sum1 / sum2;
    }
}