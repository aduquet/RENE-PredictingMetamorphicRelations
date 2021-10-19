

public class min {
    public static double min_m(Double[] elements) {
        int size = elements.length;
        double min = elements[size - 1];
        for (int i = size - 1; --i >= 0; ) {
            if (elements[i] < min) {
                min = elements[i];
            }
        }
        return min;
    }
}