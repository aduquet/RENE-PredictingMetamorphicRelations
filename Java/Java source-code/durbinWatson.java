

public class durbinWatson {
    public static double durbinWatson_m(Double[] elements) {
        int size = elements.length;
        double run = 0;
        for (int i = 1; i < size; ++i) {
            double x = elements[i] - elements[i - 1];
            run += x * x;
        }
        return run;
    }
}