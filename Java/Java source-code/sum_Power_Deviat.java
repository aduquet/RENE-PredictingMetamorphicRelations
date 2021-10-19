

public class sum_Power_Deviat {
    public static double sum_Power_Deviat_m(Double[] data, Integer k, Double c) {
        double sum = 0;
        for (int i = 0; i < data.length; i++) {
            sum += Math.pow(data[i] - c, k);
        }
        return sum;
    }
}