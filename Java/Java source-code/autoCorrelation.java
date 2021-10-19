

public class autoCorrelation {
    public static double autoCorrelation_m(Double[] data, Integer lag, Double mean, Double variance) {
        int N = data.length;
        double run = 0;
        for (int i = lag; i < N; ++i) {
            run += (data[i] - mean) * (data[i - lag] - mean);
        }
        return run / (N - lag) / variance;
    }
}