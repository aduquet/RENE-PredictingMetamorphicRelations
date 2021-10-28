

public class meanDeviation {
    public static double meanDeviation_m(Double[] elements, Double mean) {
        int size = elements.length;
        double sum = 0;
        for (int i = size; --i >= 0; ) {
            sum += Math.abs(elements[i] - mean);
        }
        return sum / size;
    }
}