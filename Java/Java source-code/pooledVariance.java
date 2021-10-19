

public class pooledVariance {
    public static double pooledVariance_m(Double[] data1, Double[] data2) {
        double sum1 = 0;
        double sumSq1 = 0;
        for (int i = 0; i < data1.length; i++) {
            sum1 += data1[i];
            sumSq1 += data1[i] * data1[i];
        }
        double mean1 = sum1 / data1.length;
        double var1 = (sumSq1 - mean1 * sum1) / data1.length;
        double sum2 = 0;
        double sumSq2 = 0;
        for (int i = 0; i < data2.length; i++) {
            sum2 += data2[i];
            sumSq2 += data2[i] * data2[i];
        }
        double mean2 = sum2 / data2.length;
        double var2 = (sumSq2 - mean2 * sum2) / data2.length;
        return (data1.length * var1 + data2.length * var2) / (data1.length + data2.length);
    }
}