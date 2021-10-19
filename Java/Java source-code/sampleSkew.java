

public class sampleSkew {
    public static double sampleSkew_m(Integer size, Double moment3, double sampleVariance) {
        int n = size;
        double s = Math.sqrt(sampleVariance);
        double m3 = moment3 * n;
        return n * m3 / ((n - 1) * (n - 2) * s * s * s);
    }
}