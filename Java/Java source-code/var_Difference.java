

public class var_Difference {
    public static double var_Difference_m(final Double[] sample1, final Double[] sample2) {
        double sum1 = 0d;
        double sum2 = 0d;
        double diff = 0d;
        int n = sample1.length;
        double sumDifference = 0;
        for (int i = 0; i < n; i++) {
            sumDifference += sample1[i] - sample2[i];
        }
        double meanDifference = sumDifference / n;
        for (int i = 0; i < n; i++) {
            diff = sample1[i] - sample2[i];
            sum1 += (diff - meanDifference) * (diff - meanDifference);
            sum2 += diff - meanDifference;
        }
        return (sum1 - sum2 * sum2 / n) / (n - 1);
    }
}