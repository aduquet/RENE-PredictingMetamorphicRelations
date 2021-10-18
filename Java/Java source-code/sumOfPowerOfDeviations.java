

public class sumOfPowerOfDeviations {
    public static double sumOfPowerOfDeviations(Double[] data, Integer k, Double c) {
        double sum = 0;
        for (int i = 0; i < data.length; i++) {
            sum += Math.pow(data[i] - c, k);
        }
        return sum;
    }
}