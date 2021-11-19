

public class harmonicMean {
    public static double harmonicMean_m(Double[] data) {
        double sumOfInversions = 0;
        for (int i = 0; i < data.length; i++) {
            sumOfInversions += 1 / data[i];
        }
        return data.length / sumOfInversions;
    }
}