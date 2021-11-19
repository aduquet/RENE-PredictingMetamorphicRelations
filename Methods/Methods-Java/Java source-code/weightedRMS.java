

public class weightedRMS {
    public static double weightedRMS_m(Double[] data, Double[] weights) {
        double sumOfProducts = 0;
        double sumOfSquaredProducts = 0;
        for (int i = 0; i < data.length; i++) {
            sumOfProducts += data[i] * weights[i];
            sumOfSquaredProducts = data[i] * data[i] * weights[i];
        }
        return sumOfProducts / sumOfSquaredProducts;
    }
}