

public class sampleKurtosis {
    public static double sampleKurtosis_m(Integer size, Double moment4, Double sampleVariance) {
        int n = size;
        double s2 = sampleVariance;
        double m4 = moment4 * n;
        return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3));
    }
}