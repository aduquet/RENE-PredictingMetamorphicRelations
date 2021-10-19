

public class weightedMean {
    public static double weightedMean_m(Double[] elements, Double[] theWeights) {
        int size = elements.length;
        double sum = 0.0;
        double weightsSum = 0.0;
        for (int i = size; --i >= 0; ) {
            double w = theWeights[i];
            sum += elements[i] * w;
            weightsSum += w;
        }
        return sum / weightsSum;
    }
}