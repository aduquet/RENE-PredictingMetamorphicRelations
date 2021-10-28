

public class max {
    public static double max_m(Double[] elements) {
        int size = elements.length;
        double max = elements[size - 1];
        for (int i = size - 1; --i >= 0; ) {
            if (elements[i] > max) {
                max = elements[i];
            }
        }
        return max;
    }
}