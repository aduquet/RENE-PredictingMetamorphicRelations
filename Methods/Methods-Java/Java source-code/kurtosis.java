

public class kurtosis {
    public static double kurtosis_m(Double[] data) {
        double sum = 0;
        double sumPD = 0;
        double sumSq = 0;
        for (int i = 0; i < data.length; i++) {
            sum += data[i];
            sumSq += data[i] * data[i];
        }
        double mean = sum / data.length;
        double standardDeviation = Math.sqrt((sumSq - mean * sum) / data.length);
        for (int i = 0; i < data.length; i++) {
            sumPD += Math.pow(data[i] - mean, 4);
        }
        double moment4 = sumPD / data.length;
        return -3 + moment4 / (standardDeviation * standardDeviation * standardDeviation * standardDeviation);
    }
}