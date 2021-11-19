

public class sampleVariance {
    public static double sampleVariance_m(Double[] elements, Double mean) {
        int size = elements.length;
        double sum = 0;
        for (int i = size; --i >= 0; ) {
            double delta = elements[i] - mean;
            sum += delta * delta;
        }
        return sum / (size - 1);
    }
}